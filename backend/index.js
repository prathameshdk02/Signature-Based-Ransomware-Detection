// Custom API for Ransomware Detection Frontend....
require('dotenv').config();

// Critical Imports Here...
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();

// Parsing Request Bodies...
app.use(bodyParser.urlencoded());
app.use(bodyParser.json());

// Handling Requests here...
app.get('/', (req, res) => {
    console.log(req.body);
    res.send('<h1>Welcome to our Backend.</h1>');
});

/* 
    Parse incoming request body.
    - Accept list of elements.
    - return the results as json.

*/ 
app.post('/scan', (req, res) => {
    let count = req.body.data.length;
    console.log(req.body.data);
    res.send(
        JSON.stringify({
            results: 'Received.',
            count: count,
        })
    );
});

// MongoDB Connection & App Listen Stuff...

const mongooseOptions = {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    dbName: 'sample_airbnb',
};

mongoose.connect(process.env.MONGODB_URI, mongooseOptions).then(() => {
    // Listening for Requests...
    app.listen(process.env.PORT, () => {
        console.log('Started API...');
    });
});
