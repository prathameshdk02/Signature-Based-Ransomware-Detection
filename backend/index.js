// Custom API for Ransomware Detection Frontend....
require('dotenv').config();

// Critical Imports Here...
const express = require('express');
const mongoose = require('mongoose');

const app = express();

// Handling Requests here...
app.get('/', (req, res) => {
    res.send('<h1>Welcome to our Backend.</h1>');
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
