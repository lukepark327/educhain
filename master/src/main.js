/**
 * ToDo: make malicious node
 * ToDo: make light client
 */

"use strict";
const express = require("express");
const bodyParser = require("body-parser");

const nw = require("./network");

// set environment variable
const http_port = process.env.HTTP_PORT || 3000;

/**
 * precondition
 * : all the other nodes are available.
 */
const initialPeers = process.env.PEERS ? process.env.PEERS.split(',') : [];  // > $env:PEERS = "ws://127.0.0.1:6001, ws://127.0.0.1:6002"

// RESTful
function initHttpServer() {
    const app = express();
    app.use(bodyParser.json());

    /**
     * GET example
     */
    /*
        app.get("", function (req, res) {
            res.send();
        });
    */
    app.get("/peers", function (req, res) {
        res.send(nw.getSockets().map(function (s) {
            return s._socket.remoteAddress + ':' + s._socket.remotePort;
        }));
    });
    /*
    app.post("/addPeers", function (req, res) {
        const peers = req.body.peers || [];
        nw.connectToPeers(peers);
        res.send();
    });
    */
    app.post("/stop", function (req, res) {
        res.send({ "msg": "Stopping server" });
        process.exit();
    });

    app.listen(http_port, function () { console.log("Listening http port on: " + http_port) });
}

function getAllPeers() {
    return initialPeers;
}

// main
nw.connectToPeers(initialPeers);
initHttpServer();
nw.initP2PServer();

// console.log(nw.getTable());
