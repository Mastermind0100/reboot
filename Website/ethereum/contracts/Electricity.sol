pragma solidity >=0.4.0 <0.6.0;

contract ElectricalBoard{
    mapping(uint=>address) public recipients;
    uint[] public recipientsAadhar;

    address public manager;

    constructor() public payable{
        manager = msg.sender;

    }

    modifier isManager(){
        require(msg.sender==manager);
        _;
    }

    function putEthereum() public isManager payable{

    }

    function getEthereum() public isManager{
        manager.transfer(address(this).balance);
    }

    function newConnection(uint aadhar)public isManager{

        address newConn = new connection(aadhar,msg.sender);
        recipients[aadhar] = newConn;
        recipientsAadhar.push(aadhar);

    }



    function transerCredits(uint aadhar,uint transferAmmount)public isManager{
        address recipientContract= recipients[aadhar];
        recipientContract.transfer(transferAmmount);
    }

    function getRecipients() view public returns(uint[]){
        return recipientsAadhar;
    }

    function() external payable{

    }
}


contract connection{

    uint public aadhar;
    address private provider;
    constructor(uint aadhar1,address provider1) public payable{
        aadhar=aadhar1;
        provider = provider1;
    }

    function pay(uint ammount) public {
        provider.transfer(ammount);
    }
    function() external payable{

    }
}
