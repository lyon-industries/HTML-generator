import csv
import sys

reader = csv.DictReader(open("/Users/aashild/Documents/Python/CSV2HTML/concerts.csv"))

f_html = open('/Users/aashild/Documents/Python/CSV2HTML/formatted.html',"w")


for row in reader:
    
    f_html.write('<tr>')

    f_html.write('<td>' + row['År'] + '</td>')
    f_html.write('<td>' + row['Komponist'] + '</td>')
    f_html.write('<td>' + row['Verk'] + '</td>')
    f_html.write('<td>' + row['Dirigent'] + '</td>')
    f_html.write('<td>' + row['Sted'] + '</td>')
    
    if row['Mer Info'] != (''):
        f_html.write('<td><a href="' + row['Mer Info'] + '"target="_blank">Link</a></td>')
    else:
        f_html.write('<td>' + '</td>')

    f_html.write('</tr>')
