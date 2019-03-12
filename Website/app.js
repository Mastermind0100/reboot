var express           = require("express"),
    bodyParser        = require("body-parser"),
    mongoose          = require("mongoose"),
    expressSanitizer  = require("express-sanitizer"),
    methodOverride    = require("method-override"),
    passport          = require("passport"),
    LocalStrategy     = require("passport-local");

var app=express();

app.use(bodyParser.urlencoded({extended:true}));
app.use(expressSanitizer());
app.set("view engine","ejs");
app.use(express.static('public'));
app.use(methodOverride("_method"));


mongoose.connect("mongodb://localhost/SELECT");


var User = require("./models/user");

app.use(require("express-session")({
    secret: "coding sucks",
    resave: false,
    saveUninitialized: false
}));


app.use(passport.initialize());
app.use(passport.session());

passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

//Middlewares
app.use(function(req,res,next){
    res.locals.currentUser = req.user;
    next();
});



//routes
const login = require('./routes/login');
const newCustomer = require('./routes/newCustomer');





app.get('/',(req,res)=>{
    res.render("home.ejs")
});

app.use('/login',login);            // Login route

app.use('/NewCustomer',newCustomer);


app.get("/logout", function(req, res){
    req.logout();
    res.redirect("/");
});








// Creating the server
app.listen(3000,process.env.IP,function(){
    console.log("The Server has Started");
});


function isLoggedIn(req,res,next){
    if(req.isAuthenticated()) {
        next();
    } else {
        res.redirect('/login');
    }
}

function isManager(req,res,isLoggedIn, next){
    if(req.user[username]==='admin'){
        next();
    } else{
        res.redirect('/logout');
    }
}