import csv
import sys

reader = csv.DictReader(open("concerts.csv"))

f_html = open('formatted.html',"w")


for row in reader:
    
    f_html.write('<tr>')

    f_html.write('<td>' + row['År'] + '</td>')
    f_html.write('<td>' + row['Komponist'] + '</td>')
    f_html.write('<td>' + row['Verk'] + '</td>')
    f_html.write('<td>' + row['Dirigent'] + '</td>')
    f_html.write('<td>' + row['Sted'] + '</td>')
    
    if row['Mer Info'] != (''):
        f_html.write('<td><a href="' + row['Mer Info'] + '">Link</a></td>')
    else:
        f_html.write('<td>' + '</td>')

    f_html.write('</tr>')



'''
# Create the HTML file
f_html = open('Output.html',"w")




for row in csv_reader: # Read a single row from the CSV file
    print(row)
    f_html.write('<tr>');# Create a new row in the table
    if row == 0 or 1 or 2 or 3 or 4:

        for column in row: # For each column..
            print("Working first")
            f_html.write('<td>' + column + '</td>')

    if row == 5:

        for column in row:
            print("Working second")
            f_html.write('<td><a href="' + column + '">Link</a></td>')

    f_html.write('</tr>')

f_html.write('</table>') '''