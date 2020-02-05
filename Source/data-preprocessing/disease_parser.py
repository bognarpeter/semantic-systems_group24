from bs4 import BeautifulSoup as parser
# usage:  python disease_parser.py > ../../Data/diseases_and_symptoms.csv

def col_parser(row, idx):
    value = row.findAll('td')[idx].p.getText()
    if '_' in value:
        value = value.split('_')[1]
        if '^' in value:
            value = value.split('^')[0]
        value = ' '.join(value.split())
    return value

FILE_PATH="../../Data/diseases_and_symptoms.htm"
with open(FILE_PATH, 'r') as file:
    data = file.read()
diseas_html = parser(data, 'html.parser')

table = diseas_html.find( "table", {"class": "MsoTableWeb3"})
symptoms = []
isFirst = True
current_disease = ""
for row in table.findAll("tr"):
    disease = col_parser(row, 0)

    if not disease.isspace() and not isFirst:
        print(current_disease+','+','.join(symptoms))
        current_disease = disease
        symptoms = []

    if isFirst:
        current_disease = disease
        isFirst = False

    symptoms.append(col_parser(row,2))
print(current_disease+','+','.join(symptoms))
