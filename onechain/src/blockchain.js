"use strict";
const CryptoJS = require("crypto-js");
const merkle = require("merkle");
const random = require("random");

const currentVersion = getCurrentVersion();

function getCurrentVersion() {
    const fs = require("fs");

    const packageJson = fs.readFileSync("./package.json");
    const currentVersion = JSON.parse(packageJson).version;
    return currentVersion;
}

class BlockHeader {
    constructor(version, index, previousHash, timestamp, merkleRoot, difficulty, nonce) {
        this.version = version;
        this.index = index;
        this.previousHash = previousHash.toString().toUpperCase();
        this.timestamp = timestamp;
        this.merkleRoot = merkleRoot;
        this.difficulty = difficulty;
        this.nonce = nonce;
    }
}

class Block {
    constructor(header, data) {
        this.header = header;
        this.data = data;
    }
}

function getGenesisBlock() {
    const version = "1.0.0";
    const index = 0;
    const previousHash = '0'.repeat(64);
    const timestamp = 1231006505; // 01/03/2009 @ 6:15pm (UTC)
    const difficulty = 0;
    const nonce = 0;
    const data = ["The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"];

    /**
     * The sort() method sorts the elements of an array in place
     * and returns the array.
     */
    data.sort();

    /**
     * The unshift() method adds one or more elements
     * to the beginning of an array
     * and returns the new length of the array.
     */
    data.unshift("Coinbase");
    const merkleTree = merkle("sha256").sync(data);
    const merkleRoot = merkleTree.root();

    const header = new BlockHeader(version, index, previousHash, timestamp, merkleRoot, difficulty, nonce);
    return new Block(header, data);
}

/**
 * TODO: Use database to store the data permanently.
 * A current implemetation stores blockchain in local volatile memory.
 */
var blockchain = [getGenesisBlock()];

function getBlockchain() { return blockchain; }
function getLatestBlock() { return blockchain[blockchain.length - 1]; }

function generateNextBlock(blockData) {
    const previousBlock = getLatestBlock();
    const difficulty = getDifficulty(getBlockchain());
    const nextIndex = previousBlock.header.index + 1;
    const previousHash = calculateHashForBlock(previousBlock);
    const nextTimestamp = getCurrentTimestamp();

    blockData.sort();
    blockData.unshift("Coinbase");
    const merkleTree = merkle("sha256").sync(blockData);
    const merkleRoot = merkleTree.root();

    const newBlockHeader = findBlock(currentVersion, nextIndex, previousHash, nextTimestamp, merkleRoot, difficulty);
    const newBlock = new Block(newBlockHeader, blockData);
    return newBlock;
}

/**
 * TODO: Implement a stop mechanism.
 * A current implementation doesn't stop until finding matching block.
 */
function findBlock(currentVersion, nextIndex, previoushash, nextTimestamp, merkleRoot, difficulty) {
    var nonce = 0;
    while (true) {
        var hash = calculateHash(currentVersion, nextIndex, previoushash, nextTimestamp, merkleRoot, difficulty, nonce);
        if (hashMatchesDifficulty(hash, difficulty)) {
            return new BlockHeader(currentVersion, nextIndex, previoushash, nextTimestamp, merkleRoot, difficulty, nonce);
        }
        nonce++;
    }
}

function getCurrentTimestamp() {
    return Math.round(new Date().getTime() / 1000);
}

const BLOCK_GENERATION_INTERVAL = 10; // in seconds
const DIFFICULTY_ADJUSTMENT_INTERVAL = 10; // in blocks

function getDifficulty(aBlockchain) {
    const latestBlock = aBlockchain[aBlockchain.length - 1];
    if (latestBlock.header.index % DIFFICULTY_ADJUSTMENT_INTERVAL === 0 && latestBlock.header.index !== 0) {
        return getAdjustedDifficulty(latestBlock, aBlockchain);
    }
    return latestBlock.header.difficulty;
}

function getAdjustedDifficulty(latestBlock, aBlockchain) {
    const prevAdjustmentBlock = aBlockchain[aBlockchain.length - DIFFICULTY_ADJUSTMENT_INTERVAL];
    const timeTaken = latestBlock.header.timestamp - prevAdjustmentBlock.header.timestamp;
    const timeExpected = BLOCK_GENERATION_INTERVAL * DIFFICULTY_ADJUSTMENT_INTERVAL;

    if (timeTaken < timeExpected / 2) {
        return prevAdjustmentBlock.header.difficulty + 1;
    }
    else if (timeTaken > timeExpected * 2) {
        return prevAdjustmentBlock.header.difficulty - 1;
    }
    else {
        return prevAdjustmentBlock.header.difficulty;
    }
}

function hashMatchesDifficulty(hash, difficulty) {
    const ut = require("./utils");

    const hashBinary = ut.hexToBinary(hash);
    const requiredPrefix = '0'.repeat(difficulty);
    return hashBinary.startsWith(requiredPrefix);
}

function calculateHashForBlock(block) {
    return calculateHash(
        block.header.version,
        block.header.index,
        block.header.previousHash,
        block.header.timestamp,
        block.header.merkleRoot,
        block.header.difficulty,
        block.header.nonce
    );
}

function calculateHash(version, index, previousHash, timestamp, merkleRoot, difficulty, nonce) {
    return CryptoJS.SHA256(version + index + previousHash + timestamp + merkleRoot + difficulty + nonce).toString().toUpperCase();
}

function addBlock(newBlock) {
    if (isValidNewBlock(newBlock, getLatestBlock())) {
        blockchain.push(newBlock);
        return true;
    }
    return false;
}

function isValidBlockStructure(block) {
    return typeof(block.header.version) === 'string'
        && typeof(block.header.index) === 'number'
        && typeof(block.header.previousHash) === 'string'
        && typeof(block.header.timestamp) === 'number'
        && typeof(block.header.merkleRoot) === 'string'
        && typeof(block.header.difficulty) === 'number'
        && typeof(block.header.nonce) === 'number'
        && typeof(block.data) === 'object';
}

function isValidTimestamp(newBlock, previousBlock) {
    return (previousBlock.header.timestamp - 60 < newBlock.header.timestamp)
        && newBlock.header.timestamp - 60 < getCurrentTimestamp();
}

function isValidNewBlock(newBlock, previousBlock) {
    if (!isValidBlockStructure(newBlock)) {
        console.log('invalid block structure: %s', JSON.stringify(newBlock));
        return false;
    }
    else if (previousBlock.header.index + 1 !== newBlock.header.index) {
        console.log("Invalid index");
        return false;
    }
    else if (calculateHashForBlock(previousBlock) !== newBlock.header.previousHash) {
        console.log("Invalid previousHash");
        return false;
    }
    else if (!isValidTimestamp(newBlock, previousBlock)) {
        console.log('invalid timestamp');
        return false;
    }
    else if (newBlock.data[0] !== "Coinbase") {
        console.log("Invalid data");
        return false;
    }
    else if (merkle("sha256").sync(newBlock.data).root() !== newBlock.header.merkleRoot) {
        console.log("Invalid merkleRoot");
        return false;
    }
    else if (!hashMatchesDifficulty(calculateHashForBlock(newBlock), newBlock.header.difficulty)) {
        console.log("Invalid hash: " + calculateHashForBlock(newBlock));
        return false;
    }
    return true;
}

function isValidChain(blockchainToValidate) {
    if (JSON.stringify(blockchainToValidate[0]) !== JSON.stringify(getGenesisBlock())) {
        return false;
    }
    var tempBlocks = [blockchainToValidate[0]];
    for (var i = 1; i < blockchainToValidate.length; i++) {
        if (isValidNewBlock(blockchainToValidate[i], tempBlocks[i - 1])) {
            tempBlocks.push(blockchainToValidate[i]);
        }
        else { return false; }
    }
    return true;
}

function replaceChain(newBlocks) {
    if (
        isValidChain(newBlocks)
        && (newBlocks.length > blockchain.length || (newBlocks.length === blockchain.length) && random.boolean())
    ) {
        const nw = require("./network");

        console.log("Received blockchain is valid. Replacing current blockchain with received blockchain");
        blockchain = newBlocks;
        nw.broadcast(nw.responseLatestMsg());
    }
    else { console.log("Received blockchain invalid"); }
}

function getBlockVersion(index) {
    return blockchain[index].header.version;
}

module.exports = {
    calculateHashForBlock,
    generateNextBlock,
    getLatestBlock,
    getBlockchain,
    addBlock,
    replaceChain,
    getCurrentVersion,
    getBlockVersion
};
