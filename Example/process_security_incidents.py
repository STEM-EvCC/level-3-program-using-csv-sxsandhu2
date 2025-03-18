import csv

with open('security_incidents.csv', 'r') as infile:
    reader = csv.reader(infile)
    security = list(reader)

security[0].append("Status")

for i in range(1, len(security)):
    security[i].append("Pending")

with open('security_incidents_modified.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(security)