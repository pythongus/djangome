# coding: utf-8
from finapp.models import Entry
import csv

with open('../data/Financial Planning 2019.csv') as csv_file:
    reader = csv.reader(csv_file)
    header = [column.lower() for column in next(reader)]
    records = [dict(zip(header, row)) for row in reader]
    
for rc in records:
    amount = float(rc['amount'])
    rc['entry_type'] = 'E' if amount < 0 else 'I' 
    rc['amount'] = abs(amount)
    new_entry = Entry(**rc)
    new_entry.save()
