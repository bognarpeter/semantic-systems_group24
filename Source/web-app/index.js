'use strict';

const express = require('express');
const path = require('path');
const hbs = require('express-handlebars');
const flash = require('connect-flash');
const session = require('express-session');
const bodyParser = require('body-parser');
const rp = require('request-promise');
const expressValidator = require('express-validator');
const { check, validationResult } = require('express-validator');

//constants
const DB_NAME='';
const DB_URL = '';
const PORT = 8081;


function initialize () {
    let app = express();

    var routes = require('./routes/index');

    // View Engine
    app.set('views', path.join(__dirname, 'views'));
    app.engine('hbs', hbs({extname: 'hbs', defaultLayout: 'layout'}));
    app.set('view engine', 'hbs');

    // BodyParser Middleware
    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({extended: true}));

    // Set Static Folder
    app.use(express.static('public'));

    // Express Session
    app.use(session({
        secret: 'secret',
        saveUninitialized: true,
        resave: true
    }));

    // Express Validator
    app.use(expressValidator({
        errorFormatter:(param, msg, value) => {
            var namespace = param.split('.')
                , root    = namespace.shift()
                , formParam = root;

            while(namespace.length) {
                formParam += '[' + namespace.shift() + ']';
            }
            return {
                param : formParam,
                msg   : msg,
                value : value
            };
        }
    }));

    // Connect Flash
    app.use(flash());

    // Global Vars
    app.use((req, res, next) => {
        res.locals.success_msg = req.flash('success_msg');
        res.locals.error_msg = req.flash('error_msg');
        res.locals.error = req.flash('error');
        res.locals.user = req.user || null;
        next();
    });

    app.use('/', routes);
    app.use((err, req, res, next) => {
        res.status(500).send(err);
    });

    app.listen(PORT, (err) => {
        if (err) {
            console.log(`Fail: ${err}`);
        }
        console.log(`Server is running.\nListening on port ${PORT}...`);
    });
}
initialize();
