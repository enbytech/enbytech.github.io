import csv
import os
import re

root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, 'template', 'person.html')) as fh:
    person_template = fh.read()

with open(os.path.join(root, 'template', 'index.html')) as fh:
    index_template = fh.read()

people = []
with open(os.path.join(root, 'people.csv')) as fh:
    rd = csv.DictReader(fh, delimiter=';') 
    for row in rd:
        people.append(row)

content = ''
for p in people:
    html_snippet = person_template
    html_snippet = re.sub(r'{{name}}', p['name'], html_snippet)
    html_snippet = re.sub(r'{{link}}', p['link'], html_snippet)
    content += html_snippet

html = re.sub(r'{{content}}', content, index_template)
with open('out.html', 'w') as fh:
    fh.write(html)
