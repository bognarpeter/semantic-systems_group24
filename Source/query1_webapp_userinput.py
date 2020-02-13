from SPARQLWrapper import SPARQLWrapper, SPARQLWrapper2, JSON,  CSV, TSV
input1="shortness of breath"
input2="pain chest"
# set endpoint and query
endpoint = "http://localhost:7200/repositories/finxd"
if len(input1)>2 and len(input2)>2:
    query = """
PREFIX : <http://www.semanticweb.org/christine/ontologies/2020/0/mdb#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?name
WHERE {
    	?disease foaf:name ?name;
    			:resulting ?symptom.
    FILTER (CONTAINS(?symptom, \"""" + input1 + """\") && CONTAINS(?symptom, \"""" + input2 + """\"))
}
"""
    # get results from endpoint
    sparql = SPARQLWrapper(endpoint)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)
    sparql.setMethod('POST')
    ret = sparql.query()
    dict = ret.convert()

    for i in range(0,50):
        try:
            print(dict["results"]["bindings"][i]["name"]["value"]  )  
        except:
            do="nothing"
else:
    
    print("please enter more than one symptom")