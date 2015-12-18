import requests
import time

from Ogame.py_bot import OgameBOT

domain = 'tr.ogame.gameforge.com'
server_url = 's135-tr.ogame.gameforge.com'
username = 'AngelusMortis'
password = '58525654afi'
session = requests.session()
myMail = 'halacayberk@gmail.com'
myMailPass = '58525654afi'
toMail = 'ayberk35halac@gmail.com'
bot = OgameBOT(session, domain, server_url, username, password, myMail, myMailPass, toMail)
bot.start()
while True:
    session = requests.session()
    ret = bot.check_event()
    if ret:
        bot.send_mail()
        time.sleep(600)
        bot.start()
    else:
        time.sleep(60)
        bot.start()
