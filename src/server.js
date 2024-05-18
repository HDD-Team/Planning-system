import express from 'express'
import bodyParser from 'body-parser'
import cors from 'cors'
import mongoose from 'mongoose'

const app = express()
app.use(bodyParser.json())
app.use(cors())

// Подключение к MongoDB
mongoose.connect('mongodb://localhost:27017/proect', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})

const db = mongoose.connection
db.on('error', console.error.bind(console, 'connection error:'))
db.once('open', () => {
  console.log('Connected to MongoDB')
})

// Модель Teacher
const CardsSchema = new mongoose.Schema({
  _id: String,
  teacher: {
    name: String,
    surname: String
  },
  students: [
    {
      name: String,
      surname: String,
      group: String
    }
  ],
  teamname: String
})

const Cards = mongoose.model('cards', CardsSchema)

// Маршрут для получения данных
app.get('/api/cards', async (req, res) => {
  try {
    const cards = await Cards.find({})
    res.json(cards)
  } catch (err) {
    console.error(err)
    res.status(500).json({ error: 'Server error' })
  }
})

// Маршрут для редактирования данных
app.put('/api/cards/:id', async (req, res) => {
  try {
    const updatedCard = await Cards.findOneAndUpdate(
      { _id: req.params.id },
      {
        $set: {
          teacher: {
            name: req.body.teacher.name,
            surname: req.body.teacher.surname
          },
          students: req.body.students,
          teamname: req.body.teamname
        }
      },
      { new: true }
    )

    if (!updatedCard) {
      return res.status(404).json({ error: 'Card not found' })
    }

    res.json(updatedCard)
  } catch (err) {
    console.error(err)
    res.status(500).json({ error: 'Server error' })
  }
})

// Маршрут для обновления данных
app.put('/api/cards/:id/update', async (req, res) => {
  try {
    const updatedCard = await Cards.findByIdAndUpdate(
      req.params.id,
      {
        teacher: {
          name: req.body.teacher.name,
          surname: req.body.teacher.surname
        },
        students: req.body.students,
        teamname: req.body.teamname
      },
      { new: true }
    )

    if (!updatedCard) {
      return res.status(404).json({ error: 'Card not found' })
    }

    updatedCard.save()
    res.json(updatedCard)
  } catch (err) {
    console.error(err)
    res.status(500).json({ error: 'Server error' })
  }
})

// Маршрут для сохранения данных при редактировании
app.put('/api/cards/:id/save', async (req, res) => {
  try {
    const updatedCard = await Cards.findByIdAndUpdate(
      req.params.id,
      {
        teacher: {
          name: req.body.teacher.name,
          surname: req.body.teacher.surname
        },
        students: req.body.students,
        teamname: req.body.teamname
      },
      { new: true }
    )

    if (!updatedCard) {
      return res.status(404).json({ error: 'Card not found' })
    }

    updatedCard.save()
    res.json(updatedCard)
  } catch (err) {
    console.error(err)
    res.status(500).json({ error: 'Server error' })
  }
})

// Маршрут для сохранения данных при добавлении
app.post('/api/cards', async (req, res) => {
  try {
    const newCard = new Cards({
      teacher: {
        name: req.body.teacher.name,
        surname: req.body.teacher.surname
      },
      students: req.body.students,
      teamname: req.body.teamname
    })

    const savedCard = await newCard.save()
    res.status(201).json(savedCard)
  } catch (err) {
    console.error(err)
    res.status(500).json({ error: 'Server error' })
  }
})
// Запуск сервера
const PORT = process.env.PORT || 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`)
})
