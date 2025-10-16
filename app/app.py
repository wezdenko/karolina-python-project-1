import json
from datetime import datetime, date


path = input('Input path for json file:')

with open(path, 'r') as data:
    file = json.load(data)

#1

date1_entry = input('Input start date in YYYY-MM-DD format:')
date2_entry = input('Input end date in YYYY-MM-DD format:')

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

counter_user1 = 0
counter_user2 = 0

for message in file['messages']:
    message_date = datetime.fromtimestamp(message['timestamp_ms']/1000).date()
    if message_date > date1 and message_date < date2 and message['sender_name'] == user1:
        counter_user1 = counter_user1 + 1

for message in file['messages']:
    message_date = datetime.fromtimestamp(message['timestamp_ms']/1000).date()
    if message_date > date1 and message_date < date2 and message['sender_name'] == user2:
        counter_user2 = counter_user2 + 1

print(f'Number of messages for {user1} in the given period is {counter_user1}.')
print(f'Number of messages for {user2} in the given period is {counter_user2}.')