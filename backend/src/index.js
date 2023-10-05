// Custom API for Ransomware Detection Frontend....
require('dotenv').config();

// Critical Imports Here...
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// User-defined Imports Here...
const { mongoConnect, getMongoDB } = require('./util/mongoDB');

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
    const db = getMongoDB().db('signatures');
    const collection = db.collection('hashes');

    collection.findOne({ hash: { $eq: `${req.body.hash}` } }).then((doc) => {
        if (doc) {
            return res.send(JSON.stringify(doc));
        }
        res.send(
            JSON.stringify({
                isSafe: true,
            })
        );
    });
});

app.post('/hashupload', (req, res) => {
    const db = getMongoDB().db('signatures');
    const collection = db.collection('hashes');

    collection.insertMany(req.body.data).then((data) => {
        res.send(
            JSON.stringify({
                results: 'Received.',
                count: data.insertedCount,
            })
        );
    });
});

// MongoDB Connection & App Listen Stuff...

mongoConnect(() => {
    app.listen(3000, () => {
        console.log('Started API...');
    });
});
