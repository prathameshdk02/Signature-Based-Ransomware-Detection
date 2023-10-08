// Custom API for Ransomware Detection Frontend....
require('dotenv').config();

// Critical Imports Here...
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// User-defined Imports Here...
const { mongoConnect, getMongoDB } = require('./src/util/mongoDB');
// const { formatUptime } = require('./util/utility')

// Parsing Request Bodies...
app.use(bodyParser.urlencoded());
app.use(bodyParser.json());

// Handling Requests here...
app.get('/', (req, res) => {
    console.log(req.body);
    res.send('<h1>Welcome to our Backend.</h1>');
});


app.get('/initial', (req, res) => {
    const db = getMongoDB().db('signatures');
    const collection = db.collection('hashes');

    let resp = {
        status: 'Online',
        connection: 'Active',
        uptime: Math.floor(process.uptime()),
        domain: req.get('host'),
        backend: 'ExpressJS'
    }

    collection.estimatedDocumentCount().then((count) => {
        resp = {
            samples: count,
            ...resp
        }
        res.send(JSON.stringify(resp));
    }).catch(() => {
        resp = {
            samples: 0,
            ...resp
        }
        res.send(JSON.stringify(resp));
    })   
})

// Route to handle & check for matching hash...
app.post('/scan', (req, res) => {
    const db = getMongoDB().db('signatures');
    const collection = db.collection('hashes');

    collection.findOne({ hash: { $eq: `${req.body.hash}` } }).then((doc) => {
        if (doc) {
            doc = {
                isSafe: false,
                fileName: req.body.filename,
                fileSize: req.body.size,
                ...doc
            }
            return res.send(JSON.stringify(doc));
        }
        res.send(
            JSON.stringify({
                isSafe: true,
                fileName: req.body.filename,
                fileSize: req.body.size
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
