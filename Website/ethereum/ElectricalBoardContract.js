import web3 from './web3';
import ElectricalBoard from './build/ElectricalBoard.json';

const contract = web3.eth.Contract(
    JSON.parse(ElectricalBoard.interface),
    '0x2E8b6a961B26c0b10f8f74154FeF9e6e9Ad70AF4'
    );

export default contract;
