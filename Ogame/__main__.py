import requests
import time

from Ogame.py_bot import OgameBOT

domain = ''
server_url = ''
username = ''
password = ''
session = requests.session()
myMail = ''
myMailPass = ''
toMail = ''
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
