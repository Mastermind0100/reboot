var express               = require('express'),
    router                = express.Router() ,
    mongoose              = require("mongoose"),
    passport              = require("passport"),
    User                  = require("../models/user");

router.get('/',(req,res)=>{
   res.render('login.ejs',{query:req.query});
});

router.post("/", passport.authenticate("local", {
    successRedirect: "./",
    failureRedirect: "?error=402",
}));



module.exports= router;