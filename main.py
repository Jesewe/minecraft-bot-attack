import time
from javascript import *

mineflayer = require('mineflayer')

BOT_USERNAME = input('Enter bot nickname [Example: Dethroit] : ')
HOST = input('Enter Host [Example: 127.0.0.1 | example.aternos.me] : ')

try:
    PORT = int(input('Enter Port [Example: 25565] : '))
    NUMBER = int(input('Enter number of bots [Example: 10] : '))
except ValueError:
    print('ValueError')
else:
    try:
        for i in range(NUMBER):
            bot = mineflayer.createBot({
              'host': HOST,
              'port': PORT,
              'username': BOT_USERNAME+str(i+1)
            })
            print(f'Joined bot: {i+1}')
    except Exception as e:
        print('Error: ' + e)

while True:
    pass
