const express = require('express')
const app = express();
const path = require('path')
const hbs = require('hbs')
const { error } = require('console')
const mongoose = require('mongoose')
bodyparser = require("body-parser");
app.use(bodyparser.urlencoded({ extended: true }));
const port = process.env.PORT || 4000
const { spawn, exec } = require('child_process');
const { data, Callbacks } = require('jquery');
const { query, response } = require('express');
const { json } = require('body-parser');
const { load } = require('netlify-lambda/lib/config');
const { TIMEOUT } = require('dns');
const { PassThrough } = require('stream');
const { PythonShell } = require('python-shell');


require('dotenv').config();
mongoose.set('strictQuery', false);

const templatepath = path.join(__dirname, '../src/templates/views')
const partialpath = path.join(__dirname, "../src/templates/partial");

app.use(express.json());
app.use('/css', express.static(path.join(__dirname, '../node_modules/bootstrap/dist/css')))
app.use('/js', express.static(path.join(__dirname, '../node_modules/bootstrap/dist/js')))
app.use('/jq', express.static(path.join(__dirname, '../node_modules/jquery/dist')))
app.use('/images', express.static(path.join(__dirname, '/templates/images')))
app.use('/partial', express.static(path.join(__dirname, '../styles/partials')))

app.set('view engine', 'hbs')
app.set('views', templatepath)
hbs.registerPartials(partialpath);
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) => {
    res.render('index.hbs')
})
app.get('/index', (req, res) => {
    res.render('index.hbs')
})

app.post('/search', async (req, res) => {  
    const variable1 = req.body.search;
    console.log(variable1)
    try
    {
        const data2 = await myfunction(variable1);
        res.render('price.ejs', {data2: data2});
    }
    catch(error){
        console.log(error)
    }
  });
  
function myfunction(query1) 
{
    return new Promise((resolve, reject) => {
      let options = {
        mode: 'text',
        pythonPath: 'python',
        pythonOptions: ['-u'],
        scriptPath: './',
        args: [query1]
    };
    
    PythonShell.run('access.py', options, function(err, results) {
        if (err) console.log(err);
        let json = JSON.stringify(results)
        let buffer = JSON.parse(json).toString('utf-8')
        let obj = JSON.parse(buffer)
        console.log(obj)
        resolve(obj)
        });
   });
}




app.get('/price', (req, res) => {
    res.render('price.ejs')
})






app.listen(port, (req, res) => {
    console.log("Server is running at 4000")
});

