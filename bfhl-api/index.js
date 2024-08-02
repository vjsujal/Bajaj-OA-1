const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors'); // Ensure this line is present
const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use(cors());

app.get('/bfhl', (req, res) => {
    res.status(200).json({ operation_code: 1 });
});

app.post('/bfhl', (req, res) => {
    const data = req.body.data;
    if (!Array.isArray(data)) {
        return res.status(400).json({
            is_success: false,
            user_id: "your_fullname_dob",
            email: "your_email@xyz.com",
            roll_number: "ABCD123",
            numbers: [],
            alphabets: [],
            highest_alphabet: []
        });
    }

    let numbers = [];
    let alphabets = [];

    data.forEach(item => {
        if (!isNaN(item)) {
            numbers.push(item);
        } else {
            alphabets.push(item);
        }
    });

    res.status(200).json({
        is_success: true,
        user_id: "your_fullname_dob",
        email: "your_email@xyz.com",
        roll_number: "ABCD123",
        numbers: numbers,
        alphabets: alphabets,
        highest_alphabet: alphabets.sort().reverse()[0]
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
