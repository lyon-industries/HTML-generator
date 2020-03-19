import csv
import sys

if len(sys.argv) < 2:
  print "Usage: ./csv-html.py <your CSV file> <your HTML File.html>"
  print
  print
  exit(0)

# Open the CSV file for reading
reader = csv.reader(open(sys.argv[1]))

# Create the HTML file
f_html = open(sys.argv[2],"w");
f_html.write('<title><YOUR TITLE HERE></title>')

for row in reader: # Read a single row from the CSV file
  f_html.write('<tr>');# Create a new row in the table
  for column in row: # For each column..
    f_html.write('<td>' + column + '</td>');
  f_html.write('</tr>')


f_html.write('</table>')