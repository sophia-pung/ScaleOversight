import csv

text = "line 1\nline 2\nline 3"

# Replace newline characters with escape sequence
text = text.replace('\n', '\r\n')

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([text])
