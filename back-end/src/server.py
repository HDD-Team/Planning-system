from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from bson.objectid import ObjectId
from pymongo import MongoClient
from datetime import datetime, timedelta
from dateutil import parser


app = Flask(__name__)
CORS(app)

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["proect"]
def format_date(date):
    return date.strftime('%Y-%m-%d') if date else ''

@app.route("/events", methods=["GET"])
def get_events():
    limit = int(request.args.get("limit", 10))
    page = int(request.args.get("page", 1))
    search = request.args.get("search", "")
    start_date_str = request.args.get("startDate", "")
    end_date_str = request.args.get("endDate", "")
    status = request.args.get("status", "")
    skip = (page - 1) * limit

    query = {}
    if search:
        search_regex = {"$regex": search, "$options": "i"}
        query["$or"] = [
            {"nameEvent": search_regex},
            {"cityEvent": search_regex},
            {"teams.teachers.name": search_regex},
            {"teams.teachers.surname": search_regex},
            {"teams.students.name": search_regex},
            {"teams.students.surname": search_regex},
            {"teams.students.group": search_regex}
        ]

    if start_date_str:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        query["startDateEvent"] = {"$gte": start_date}

    if end_date_str:
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        if "startDateEvent" in query:
            query["startDateEvent"]["$lte"] = end_date
        else:
            query["startDateEvent"] = {"$lte": end_date}

    if status:
        query["statusEvent"] = status

    events_cursor = db.events.find(query, {
        "_id": 1,
        "nameEvent": 1,
        "cityEvent": 1,
        "statusEvent": 1,
        "websiteEvent": 1,
        "startDateEvent": 1,
        "endDateEvent": 1,
        "teams": 1
    }).sort([("_id", -1)]).skip(skip).limit(limit)

    events_list = list(events_cursor)

    for event in events_list:
        event["_id"] = str(event["_id"])
        event["startDateEvent"] = format_date(event.get("startDateEvent"))
        event["endDateEvent"] = format_date(event.get("endDateEvent"))
        teams = event.get("teams", [])
        for i in range(len(teams)):
            teams[i]["team_id"] = str(teams[i]["team_id"])
        event["teams"] = teams

    total_events = db.events.count_documents(query)
    total_pages = (total_events + limit - 1) // limit

    response = {
        "events": events_list,
        "total_events": total_events,
        "total_pages": total_pages,
        "current_page": page
    }

    return jsonify(response)
# Маршрут для создания нового документа в коллекции events (POST)
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    if not data:
        abort(400, description="No request data")

    # Преобразование дат в формат datetime
    if 'startDateEvent' in data:
        data['startDateEvent'] = datetime.fromisoformat(data['startDateEvent'])
    if 'endDateEvent' in data:
        data['endDateEvent'] = datetime.fromisoformat(data['endDateEvent'])

    # Добавление нового документа в коллекцию
    result = db.events.insert_one(data)

    # Преобразование ObjectId в строку
    data["_id"] = str(result.inserted_id)

    # Преобразование ответа в JSON-формат
    response_json = jsonify(data)

    # Возврат JSON-ответа с кодом 201 (Created)
    return response_json, 201

@app.route("/events/<string:event_id>/teams/<string:team_id>", methods=["DELETE"])
def remove_team_from_event(event_id, team_id):
    try:
        event_id = ObjectId(event_id)
        team_id = ObjectId(team_id)
    except Exception as e:
        app.logger.error(f"Invalid ObjectId: {e}")
        abort(400, description="Invalid ObjectId")

    app.logger.info(f"Removing team {team_id} from event {event_id}")

    # Проверка наличия события и команды в базе данных
    event = db.events.find_one({"_id": event_id})
    if not event:
        app.logger.error(f"Event not found. Event ID: {event_id}")
        abort(400, description="Event not found")

    team_exists = any(team['team_id'] == team_id for team in event.get('teams', []))
    if not team_exists:
        app.logger.error(f"Team not found in event. Team ID: {team_id}")
        abort(400, description="Team not found in event")

    result = db.events.update_one(
        {"_id": event_id},
        {"$pull": {"teams": {"team_id": team_id}}}
    )

    if result.modified_count == 0:
        app.logger.error(f"Failed to remove team from event. Event ID: {event_id}, Team ID: {team_id}")
        abort(400, description="Failed to remove team from event")

    app.logger.info(f"Successfully removed team {team_id} from event {event_id}")
    return jsonify({"message": "Team removed from event successfully"}), 200

# Маршрут для удаления существующего документа из коллекции events (DELETE)
@app.route("/events/<string:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # Преобразование строки в ObjectId
    event_id = ObjectId(event_id)

    # Удаление документа из коллекции
    db.events.delete_one({"_id": event_id})

    # Создание ответа
    response = {"message": "Event deleted", "event_id": str(event_id)}

    # Преобразование ответа в JSON-формат
    response_json = jsonify(response)

    # Возврат JSON-ответа с кодом 200 (OK)
    return response_json, 200

# Маршрут для получения всех документов из коллекции teams
@app.route("/teams", methods=["GET"])
def get_teams():
    # Запрос к коллекции teams
    teams = db.teams.find()

    # Преобразование курсора в массив
    teams_list = list(teams)

    # Преобразование ObjectId в строку
    for team in teams_list:
        team["_id"] = str(team["_id"])
        team["teachers"] = [{"name": t["name"], "surname": t["surname"]} for t in team.get("teachers", [])]
        team["students"] = [{"name": s["name"], "surname": s["surname"], "group": s["group"]} for s in team.get("students", [])]

    # Преобразование массива в JSON-формат
    teams_json = jsonify(teams_list)

    # Возврат JSON-ответа
    return teams_json


# Маршрут для получения команд с пагинацией
@app.route("/teams/paginate", methods=["GET"])
def paginate_teams():
    # Получение параметров из запроса
    limit = int(request.args.get("limit", 10))
    page = int(request.args.get("page", 1))
    skip = (page - 1) * limit

    # Запрос с сортировкой по дате добавления (уменьшение)
    teams_cursor = db.teams.find().sort("_id", -1).skip(skip).limit(limit)
    teams_list = list(teams_cursor)

    # Преобразование ObjectId в строку
    for team in teams_list:
        team["_id"] = str(team["_id"])
        team["teachers"] = [{"name": t["name"], "surname": t["surname"]} for t in team.get("teachers", [])]
        team["students"] = [{"name": s["name"], "surname": s["surname"], "group": s["group"]} for s in team.get("students", [])]

    total_teams = db.teams.count_documents({})
    total_pages = (total_teams + limit - 1) // limit

    response = {
        "teams": teams_list,
        "total_teams": total_teams,
        "total_pages": total_pages,
        "current_page": page
    }

    return jsonify(response)

@app.route("/teams/filter", methods=["GET"])
def filter_teams():
    # Получение параметров из запроса
    limit = int(request.args.get("limit", 10))
    page = int(request.args.get("page", 1))
    skip = (page - 1) * limit
    search = request.args.get("search", "")
    search_team_name = request.args.get("searchTeamName", "")
    search_participants = request.args.get("searchParticipants", "")

    # Формирование фильтра запроса
    query = {}
    if search:
        query["$or"] = [
            {"teachers.name": {"$regex": search, "$options": "i"}},
            {"teachers.surname": {"$regex": search, "$options": "i"}}
        ]
    if search_team_name:
        query["teamname"] = {"$regex": search_team_name, "$options": "i"}
    if search_participants:
        query["$or"] = [
            {"students.name": {"$regex": search_participants, "$options": "i"}},
            {"students.surname": {"$regex": search_participants, "$options": "i"}}
        ]

    teams_cursor = db.teams.find(query).skip(skip).limit(limit)
    teams_list = list(teams_cursor)

    # Преобразование ObjectId в строку
    for team in teams_list:
        team["_id"] = str(team["_id"])
        team["teachers"] = [{"name": t["name"], "surname": t["surname"]} for t in team.get("teachers", [])]
        team["students"] = [{"name": s["name"], "surname": s["surname"], "group": s["group"]} for s in
                            team.get("students", [])]

    total_teams = db.teams.count_documents(query)
    total_pages = (total_teams + limit - 1) // limit

    response = {
        "teams": teams_list,
        "total_teams": total_teams,
        "total_pages": total_pages,
        "current_page": page
    }

    return jsonify(response)
# Маршрут для создания нового документа в коллекции teams (POST)
@app.route("/teams", methods=["POST"])
def create_team():
    # Получение данных из запроса
    data = request.get_json()
    if not data:
        abort(400, description="No request data")

    # Добавление нового документа в коллекцию
    result = db.teams.insert_one(data)

    # Преобразование ObjectId в строку
    data["_id"] = str(result.inserted_id)

    # Преобразование ответа в JSON-формат
    response_json = jsonify(data)

    # Возврат JSON-ответа с кодом 201 (Created)
    return response_json, 201

# Маршрут для обновления существующего документа в коллекции events (PUT)
@app.route("/events/<string:event_id>", methods=["PUT"])
def update_event(event_id):
    event_id = ObjectId(event_id)

    data = request.get_json()
    if not data:
        abort(400, description="No request data")

    # Преобразование team_id в ObjectId для каждой команды в списке teams
    if "teams" in data:
        for team in data["teams"]:
            if isinstance(team["team_id"], str):
                team["team_id"] = ObjectId(team["team_id"])

    # Преобразование дат в формат datetime
    if 'startDateEvent' in data:
        data['startDateEvent'] = datetime.fromisoformat(data['startDateEvent'])
    if 'endDateEvent' in data:
        data['endDateEvent'] = datetime.fromisoformat(data['endDateEvent'])

    # Удаление поля _id из данных, если оно присутствует
    if "_id" in data:
        del data["_id"]

    # Обновление документа в коллекции
    db.events.update_one({"_id": event_id}, {"$set": data})

    # Преобразование ObjectId в строку для ответа
    data["_id"] = str(event_id)
    if "teams" in data:
        for team in data["teams"]:
            team["team_id"] = str(team["team_id"])

    response_json = jsonify(data)
    return response_json, 200

# Маршрут для обновления существующего документа в коллекции events (PUT)
@app.route("/teams/<string:team_id>", methods=["PUT"])
def update_team(team_id):
    # Получение данных из запроса
    data = request.get_json()
    if not data:
        abort(400, description="No request data")

    # Преобразование строки в ObjectId
    team_id = ObjectId(team_id)

    # Удаление поля _id из данных, если оно присутствует
    if "_id" in data:
        del data["_id"]

    # Обновление документа в коллекции
    db.teams.update_one({"_id": team_id}, {"$set": data})

    # Преобразование ObjectId в строку
    data["_id"] = str(team_id)

    # Преобразование ответа в JSON-формат
    response_json = jsonify(data)

    # Возврат JSON-ответа с кодом 200 (OK)
    return response_json, 200


# Маршрут для удаления существующего документа из коллекции teams (DELETE)
@app.route("/teams/<string:team_id>", methods=["DELETE"])
def delete_team(team_id):
    # Преобразование строки в ObjectId
    team_id = ObjectId(team_id)

    # Удаление документа из коллекции
    db.teams.delete_one({"_id": team_id})

    # Создание ответа
    response = {"message": "Team deleted", "team_id": str(team_id)}

    # Преобразование ответа в JSON-формат
    response_json = jsonify(response)

    # Возврат JSON-ответа с кодом 200 (OK)
    return response_json, 200


@app.route("/events/<string:event_id>/teams/<string:team_id>", methods=["PUT"])
def add_team_to_event(event_id, team_id):
    event_id = ObjectId(event_id)
    team_id = ObjectId(team_id)

    data = request.get_json()
    if not data or "statusParticipation" not in data:
        abort(400, description="Bad request: Missing statusParticipation")

    existing_team = db.events.find_one(
        {"_id": event_id, "teams.team_id": team_id},
        {"teams.$": 1}
    )

    if existing_team:
        result = db.events.update_one(
            {"_id": event_id, "teams.team_id": team_id},
            {"$set": {"teams.$.statusParticipation": data["statusParticipation"]}}
        )
    else:
        result = db.events.update_one(
            {"_id": event_id},
            {"$push": {"teams": {"team_id": team_id, "statusParticipation": data["statusParticipation"]}}}
        )

    if result.matched_count == 0:
        abort(400, description="Event or team not found")

    team_id = str(team_id)
    response_json = jsonify({"team_id": team_id, "statusParticipation": data["statusParticipation"]})
    return response_json, 201


# Функция для выполнения и отладки агрегационного запроса
def debug_aggregation(pipeline):
    result = list(db.teams.aggregate(pipeline))
    print(f"Aggregation result: {result}")
    return result

@app.route("/stats/top-teams", methods=["GET"])
def get_top_teams():
    try:
        period = request.args.get("period", "all")
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 6))
        skip = (page - 1) * limit
        now = datetime.now()

        if period == "year":
            start_date = now - timedelta(days=365)
        elif period == "month":
            start_date = now - timedelta(days=30)
        else:
            start_date = None

        match_stage = {}
        if start_date:
            match_stage["startDateEvent"] = {"$gte": start_date}

        # Pipeline for aggregation
        pipeline = [
            {"$unwind": "$teams"},
            {"$match": match_stage},
            {"$group": {
                "_id": "$teams.team_id",
                "firstPlace": {"$sum": {"$cond": [{"$eq": ["$teams.statusParticipation", "1 место"]}, 1, 0]}},
                "secondPlace": {"$sum": {"$cond": [{"$eq": ["$teams.statusParticipation", "2 место"]}, 1, 0]}},
                "thirdPlace": {"$sum": {"$cond": [{"$eq": ["$teams.statusParticipation", "3 место"]}, 1, 0]}},
                "lost": {"$sum": {"$cond": [{"$eq": ["$teams.statusParticipation", "Проиграли"]}, 1, 0]}},
                "notParticipated": {"$sum": {"$cond": [{"$eq": ["$teams.statusParticipation", "Не участвовали"]}, 1, 0]}},
                "totalPoints": {"$sum": {
                    "$add": [
                        {"$multiply": [{"$cond": [{"$eq": ["$teams.statusParticipation", "1 место"]}, 3, 0]}, 1]},
                        {"$multiply": [{"$cond": [{"$eq": ["$teams.statusParticipation", "2 место"]}, 2, 0]}, 1]},
                        {"$multiply": [{"$cond": [{"$eq": ["$teams.statusParticipation", "3 место"]}, 1, 0]}, 1]},
                        {"$multiply": [{"$cond": [{"$eq": ["$teams.statusParticipation", "Проиграли"]}, 0, 0]}, 1]},
                        {"$multiply": [{"$cond": [{"$eq": ["$teams.statusParticipation", "Не участвовали"]}, 0, 0]}, 1]}
                    ]
                }}
            }},
            {"$lookup": {
                "from": "teams",
                "localField": "_id",
                "foreignField": "_id",
                "as": "team_info"
            }},
            {"$unwind": "$team_info"},
            {"$project": {
                "_id": 1,
                "teamname": "$team_info.teamname",
                "firstPlace": 1,
                "secondPlace": 1,
                "thirdPlace": 1,
                "lost": 1,
                "notParticipated": 1,
                "totalPoints": 1
            }},
            {"$sort": {"totalPoints": -1}},
            {"$skip": skip},
            {"$limit": limit}
        ]

        top_teams = list(db.events.aggregate(pipeline))

        # Pipeline for counting total teams for the period
        count_pipeline = [
            {"$unwind": "$teams"},
            {"$match": match_stage},
            {"$group": {
                "_id": "$teams.team_id"
            }},
            {"$count": "total_teams"}
        ]

        count_result = list(db.events.aggregate(count_pipeline))
        total_teams = count_result[0]['total_teams'] if count_result else 0
        total_pages = (total_teams + limit - 1) // limit

        for team in top_teams:
            team["_id"] = str(team["_id"])

        response = {
            "teams": top_teams,
            "total_pages": total_pages
        }

        return jsonify(response)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/teams/<string:team_id>", methods=["GET"])
def get_team_details(team_id):
    team_id = ObjectId(team_id)
    team = db.teams.find_one({"_id": team_id})

    if not team:
        return jsonify({"error": "Team not found"}), 404

    team["_id"] = str(team["_id"])
    team["teachers"] = [{"name": t["name"], "surname": t["surname"]} for t in team.get("teachers", [])]
    team["students"] = [{"name": s["name"], "surname": s["surname"], "group": s["group"]} for s in team.get("students", [])]

    events_cursor = db.events.find({"teams.team_id": team_id}, {"_id": 1, "nameEvent": 1, "cityEvent": 1, "startDateEvent": 1, "endDateEvent": 1, "websiteEvent": 1, "statusEvent": 1, "teams": 1})
    events_list = list(events_cursor)
    events = []

    statistics = {
        "firstPlace": 0,
        "secondPlace": 0,
        "thirdPlace": 0,
        "lost": 0,
        "notParticipated": 0
    }

    for event in events_list:
        event["_id"] = str(event["_id"])
        for team_info in event["teams"]:
            if team_info["team_id"] == team_id:
                event_status = team_info["statusParticipation"]
                events.append({
                    "nameEvent": event["nameEvent"],
                    "cityEvent": event["cityEvent"],
                    "startDateEvent": event["startDateEvent"],
                    "endDateEvent": event["endDateEvent"],
                    "websiteEvent": event["websiteEvent"],
                    "statusParticipation": event_status
                })
                if event_status == "1 место":
                    statistics["firstPlace"] += 1
                elif event_status == "2 место":
                    statistics["secondPlace"] += 1
                elif event_status == "3 место":
                    statistics["thirdPlace"] += 1
                elif event_status == "Проиграли":
                    statistics["lost"] += 1
                elif event_status == "Не участвовали":
                    statistics["notParticipated"] += 1

    response = {
        "team": team,
        "events": events,
        "statistics": statistics
    }

    return jsonify(response)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    print("Received data:", data)  # Отладочное сообщение

    # Ищем пользователя в коллекции login
    user = db.login.find_one({"email": email, "password": password})

    if user:
        print("User found:", user)  # Отладочное сообщение
        return jsonify({
            "message": "Login successful",
            "user": {
                "email": user["email"],
                "name": user["teacher"][0]["name"],
                "surname": user["teacher"][0]["surname"]
            }
        }), 200
    else:
        print("Invalid credentials")  # Отладочное сообщение
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
