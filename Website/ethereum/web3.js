import Web3 from 'web3';

let web3;

if (typeof window !== 'undefined') {
  //we are in browser

  web3 = new Web3(window.web3.currentProvider);

} else {
  // We are on server
  const provider = new Web3.providers.HttpProvider(
      'https://rinkeby.infura.io/v3/faa24f693fb64df6bdc6c11eea62c71b'
  );
  web3 = new Web3(provider);

}

export default web3;
