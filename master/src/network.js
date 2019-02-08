"use strict";
const WebSocket = require("ws");

// set environment variable
const p2p_port = process.env.P2P_PORT || 6000;  // > $env:P2P_PORT=6003 (windows) || export P2P_PORT=3003 (mac)

// sockets
var sockets = [];

function getSockets() { return sockets; }

function initP2PServer() {
    // websocket server
    // P2P's peer works both server side and client side.
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
        var timeout = 0;  // milli-seconds

        switch (ws._socket.remotePort) {
            
            case 6001:
                /**
                 * ToDo: load delay from table.
                 */
                timeout = 3000;
                break;
            
            case 6002:
                timeout = 2000;
                break;

        }

        setTimeout(function () {
            switch (ws._socket.remotePort) {
                
                case 6001:
                    /**
                     * find a target socket in sockets.
                     * send massage to the target socket.
                     * 
                     * ToDo: send massage to target socket's'.
                     */
                    write(sockets.find(function(elem){
                        return elem.url.split(':')[2] == "6002";
                    }), message);
                    console.log("Send message to " + 6002);
                    break;
                
                case 6002:
                    write(sockets.find(function(elem){
                        return elem.url.split(':')[2] == "6001";
                    }), message);
                    console.log("Send message to " + 6001);
                    break;

            }
        }, timeout);

        /**
         * Do not use the code below. 비동기가 아님.
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

function broadcast(message) {
    sockets.forEach(function (socket) {
        write(socket, message);
    });
}

function multicast(peers, message) {
    peers.forEach(function (socket) {
        write(socket, message);
    });
}

module.exports = {
    connectToPeers,
    getSockets,
    broadcast,
    multicast,
    initP2PServer
};
