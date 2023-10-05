require('dotenv').config();

const { MongoClient } = require('mongodb');

const client = new MongoClient(process.env.MONGODB_URI);

const getMongoDB = () => {
    if(client){
        return client;
    }
    throw "Client Issue.";
}

const mongoConnect = (callback) => {
    client
        .connect()
        .then(() => {
            callback();
        })
        .catch((err) => {
            console.log('MongoDB connection failed.');
            throw err;
        });
};

exports.mongoConnect = mongoConnect;
exports.getMongoDB = getMongoDB;