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
f_html = open(sys.argv[2],"w")

for row in reader: # Read a single row from the CSV file
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

f_html.write('</table>')