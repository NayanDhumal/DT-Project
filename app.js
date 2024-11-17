const express = require('express')
const app = express();
const userModel = require("./models/usermodel");
const cookieParser = require('cookie-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const crypto = require("crypto");
const path = require("path");

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({extended:true}));

app.use(cookieParser());
app.use(express.static('public'));

app.get("/", (req,res)=>{
    res.render("HomePage.ejs");
})

app.get("/SignUp", (req,res)=>{
    res.render("SignUp.ejs");
})

app.get("/Login", (req,res)=>{
    res.render("Login");
})

app.post("/SignUP" , async (req,res) =>{
    let {email, password, name, age, contact} = req.body;

    let user = await userModel.findOne({email});
    if(user) return res.status(500).send("user already registered");

    bcrypt.genSalt(10,(err, salt) =>{
        bcrypt.hash(password, salt, async  (err, hash) =>{
            let user = await userModel.create({
                contact,
                email,
                age,
                name,
                password:hash,
            });

            let token = jwt.sign({email: email, userid: user._id},"shhhh");
            res.cookie("token",token);
            res.render("HomePage");

        })
   })
    
});

app.post("/Login" , async (req,res) =>{
    let {email, password} = req.body;

    let user = await userModel.findOne({email});
    if(!user) return res.status(500).send("something went wrong");

    
   bcrypt.compare(password, user.password, function(err, result){
    if(result){
        
        let token = jwt.sign({email: email, userid: user._id},"shhhh");
        res.cookie("token",token);
        res.status(200).redirect("/");

    }
    else res.redirect("/login");

   })
    
});


app.listen(3000);