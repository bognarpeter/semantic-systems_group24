'use strict';

var router = require('express').Router();

var query = function(query, res){
    var options = {
        method: 'GET',
        uri: 'https://localhost:XXXX',
        headers: {
            "Content-Type": ''
        },
        query: {
        },
    };

    rp(options)
        .then(function (apiResponse) {
              console.log(apiResponse);
              res.render('/', {res: apiResponse, resClean: apiResponse});
            })
            .catch((err) => console.log(err));
};


// Get Homepage
router.get('/', (req, res) => {
    res.render('index');
});

module.exports = router;
