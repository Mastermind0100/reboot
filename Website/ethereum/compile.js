const path = require ('path');
const solc = require ('solc');
const fs = require ('fs-extra');

// Paths Resolved
const buildPath = path.resolve(__dirname,'build');
const campaignPath = path.resolve(__dirname,'contracts','Electricity.sol');


//Build Folder removed
fs.removeSync(buildPath);

//Contracts extracted and compile
const source= fs.readFileSync(campaignPath,'utf-8');
const output = solc.compile(source,1).contracts;

//Build path created
fs.ensureDirSync(buildPath);

for(let contract in output) {
  fs.outputJsonSync(
      path.resolve(buildPath,contract.substring(1)+'.json'),
      output[contract]
  );
}
