"use strict";
const WebSocket = require("ws");

// set environment variable
const p2p_port = process.env.P2P_PORT || 6000;  // > $env:P2P_PORT=6003 (windows) || export P2P_PORT=3003 (mac)

// sockets
var sockets = [];

function getSockets() { return sockets; }

// propagation delay table
var table = setTable()

function getTable() { return table; }
function setTable() {
    const fs = require("fs");

    const packageJson = fs.readFileSync("../table.json");
    const table = JSON.parse(packageJson);
    return table;
}

function initP2PServer() {
    const server = new WebSocket.Server({ port: p2p_port });
    server.on("connection", function (ws) { initConnection(ws); });
    console.log("Listening websocket p2p port on: " + p2p_port);
}

function initConnection(ws) {
    sockets.push(ws);
    initMessageHandler(ws);
    initErrorHandler(ws);
}

function initMessageHandler(ws) {
    ws.on("message", function (data) {
        const message = JSON.parse(data);

        // console.log(ws._socket.remoteAddress + ':' + ws._socket.remotePort);
        // console.log("Received message" + JSON.stringify(message));
        console.log("Received message from " + ws._socket.remotePort);

        /**
         * propagation delay
         */
        var from = ws._socket.remotePort.toString()

        // ToDo: use IP address instead of 127.0.0.1 (localhost)
        var neighbors = table[from].map(function (s) {
            return s[0].toString();
        });
        // console.log(neighbors)

        var delay = table[from].map(function (s) {
            return s[1];
        });
        // console.log(delay)

        neighbors.forEach(function (neighbor, idx) {
            var timeout = delay[idx] * 1000.0;  // milli-seconds * 1000.0

            setTimeout(function () {
                write(sockets.find(function (elem) {
                    return elem.url.split(':')[2] == neighbor;
                }), message);
                console.log("Send message to " + neighbor);
            }, timeout);
        });

        /**
         * Do not use 'sleep()'. 비동기가 아님.
         */
        /*
            const sleep = require("sleep");
            sleep.msleep(5000);
        */
    });
}

function closeConnection(ws) {
    console.log("Connection failed to peer: " + ws.url);
    sockets.splice(sockets.indexOf(ws), 1);
}

function initErrorHandler(ws) {
    ws.on("close", function () { closeConnection(ws); });
    ws.on("error", function () { closeConnection(ws); });
}

function connectToPeers(newPeers) {
    newPeers.forEach(
        function (peer) {
            const ws = new WebSocket(peer);
            ws.on("open", function () { initConnection(ws); });
            ws.on("error", function () { console.log("Connection failed"); });
        }
    );
}

function write(ws, message) { ws.send(JSON.stringify(message)); }

module.exports = {
    connectToPeers,
    getSockets,
    getTable,
    initP2PServer
};
