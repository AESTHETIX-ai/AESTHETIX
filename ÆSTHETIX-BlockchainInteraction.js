// BlockchainInteraction.js
const Web3 = require('web3');
const fs = require('fs');
const contractABI = JSON.parse(fs.readFileSync('ArtworkStoreABI.json', 'utf8'));
const contractAddress = 'your_contract_address';  // Replace with the deployed contract address

const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));
const contract = new web3.eth.Contract(contractABI, contractAddress);

async function uploadArtwork(imageUrl, description) {
    const accounts = await web3.eth.getAccounts();
    const uploader = accounts[0];

    contract.methods.uploadArtwork(imageUrl, description).send({ from: uploader })
        .then((receipt) => {
            console.log('Artwork uploaded to the blockchain', receipt);
        })
        .catch((error) => {
            console.error('Error uploading artwork:', error);
        });
}

// Example usage
uploadArtwork('http://example.com/generated_artwork.png', 'Generated AI artwork based on Twitter content');
