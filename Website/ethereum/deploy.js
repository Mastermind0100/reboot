const HDWalletProvider= require('truffle-hdwallet-provider');
const Web3 = require('web3');

const ElectricalBoard = require('./build/ElectricalBoard.json');

const provider = new HDWalletProvider(
    'ship radar climb pattern dice film emotion ask apology few run tunnel',
    'https://rinkeby.infura.io/v3/faa24f693fb64df6bdc6c11eea62c71b'
);

const web3 = new Web3(provider);


const deploy = async () => {
    const accounts = await web3.eth.getAccounts();

    console.log('Attempting to deploy from account ', accounts[0]);

    const result =await new web3.eth.Contract(JSON.parse(ElectricalBoard.interface))
        .deploy({data : '0x'+ElectricalBoard.bytecode})
        .send({gas: 1000000, from:accounts[0]});

    console.log('contract deployed to', result.options.address);
};

deploy();
