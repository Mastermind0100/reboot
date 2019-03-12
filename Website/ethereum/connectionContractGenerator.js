import web3 from './web3';
import connection from './build/connection.JSON';

class connectionContractGenerator{
  function async getContract(string address){
    const contract = await web3.eth.Contract(
      JSON.parse(connection.interface),
      address
    );
    return contract;
  }

}

export default new connectionContractGenerator();
