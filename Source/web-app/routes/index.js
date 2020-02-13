'use strict';

var fetch = require('isomorphic-fetch')
const {URL} = require('whatwg-url');
var SparqlHttp = require('sparql-http-client')
var router = require('express').Router();
var Q = require('q');


var getDiseases = function(symptoms, res){
  var deferred = Q.defer();

  SparqlHttp.fetch = fetch
  SparqlHttp.URL = URL

  var endpoint = new SparqlHttp({endpointUrl: 'https://localhost:7200'})
  var query =
   ['PREFIX : <http://www.semanticweb.org/christine/ontologies/2020/0/mdb#>',
    'PREFIX foaf: <http://xmlns.com/foaf/0.1/>',
    'SELECT ?name WHERE {?disease foaf:name ?name; :resulting ?symptom. FILTER(']

  var contains = []
  symptoms.map((symptom) => {
    contains.push(`CONTAINS(?symptom, "${symptom}")`)
  });
  contains = contains.join('&&');
  query.push(contains);
  query.push(')}');
  query = query.join('\n');

  endpoint.selectQuery(query).then(function (res) {

    deferred.resolve(res);
    return deferred.promise;

  }).catch(function (err) {
    console.error(err)
  })
};


// Get Homepage
router.get('/', (req, res) => {
    res.render('index');
});

router.post('/query', (req, res) => {
    var query = req.body.query;
    var symptoms = query.split(',');
    var symptoms_cleaned = symptoms.map((s) => {return s.trim();});
    getDiseases(symptoms_cleaned)
      .then((diseases) => {res.render('results', {results: diseases});})
      .catch((err) => {console.log(err)});
});

module.exports = router;
