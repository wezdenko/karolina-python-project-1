import json
from datetime import datetime, date

with open('message_1.json', 'r') as data:
    file = json.load(data)

#1

date1_entry = input('Enter start date in YYYY-MM-DD format:')
date2_entry = input('Enter end date in YYYY-MM-DD format:')

year1, month1, day1 = map(int, date1_entry.split('-'))
year2, month2, day2 = map(int, date2_entry.split('-'))

date1 = date(year1, month1, day1)
date2 = date(year2, month2, day2)

counter = 0

for message in file['messages']:
    message_date = datetime.fromtimestamp(message['timestamp_ms']/1000).date()
    if message_date > date1 and message_date < date2:
        counter = counter + 1
print(f'Number of messages in the given period is {counter}.')

#2

user1 = file['participants'][0]['name']
user2 = file['participants'][1]['name']

print(user1)
print(user2)