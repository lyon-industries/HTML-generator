import csv
import sys

reader = csv.DictReader(open("/Users/aashild/Documents/Python/CSV2HTML/images.csv"))

f_html = open('/Users/aashild/Documents/Python/CSV2HTML/formatted2.html',"w")


for row in reader:
    
    f_html.write('<tr>')

    f_html.write('<td>' + row['Dato'] + '</td>')
    f_html.write('<td>' + row['Anledning'] + '</td>')
    
    if row['Link'] != (''):
        f_html.write('<td><a href="' + row['Link'] + '"target="_blank">Link</a></td>')
    else:
        f_html.write('<td>' + '</td>')

    f_html.write('</tr>')
