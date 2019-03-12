var express = require('express');
var router = express.Router();

router.get('/',isManager,(req,res)=>{
   res.render('newCustomer');

});

function isLoggedIn(req,res,next){
    if(req.isAuthenticated()) {
        next();
    } else {
        res.redirect('/login');
    }
}
function isManager(req,res, next) {
    try{
    if (req.user.username === 'admin') {
        next();
    } else {
        res.redirect('/logout');
    }} catch(err){
        res.redirect('/logout')
    }
}

module.exports= router;