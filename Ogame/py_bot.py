import smtplib

from bs4 import BeautifulSoup


class OgameBOT:
    def check_event(self):
        urll = self.session.get(self.get_url('eventList'))
        soup = BeautifulSoup(urll.content)
        event = soup.findAll(id='eventContent')
        try:
            soup = BeautifulSoup(str(event))
            eventr = soup.findAll('figure')
            check = True
            if len(eventr) != 0:
                for eventparser in eventr:
                    if check:
                        if eventparser.parent.get_text() != None:
                            if 'Angelus' in eventparser.parent.get_text() or 'Daemon' in eventparser.parent.get_text() or 'Caelum' in eventparser.parent.get_text() or 'Keşif' in eventparser.parent.get_text() or 'Nakliye' in eventparser.parent.get_text():
                                check = False
                                pass
                            else:
                                return True
                        else:
                            check = False
                            continue
            return False
        except:
            self.start()
            return False

    def get_url(self, page):
        if page == 'login':
            return 'http://%s/main/login' % self.domain
        else:
            url = 'http://%s/game/index.php?page=%s' % (self.server_url, page)
            return url

    def login(self):
        payload = {'kid': '',
                   'uni': self.server_url,
                   'login': self.username,
                   'pass': self.password}
        self.session.post(self.get_url('login'), data=payload).content

    def start(self):
        print('Connecting . . .')
        self.login()
        print('Connected . . .')
        print('server_url:', self.server_url)
        print('username:', self.username)
        print('password:', self.password)
        print('domain:', self.domain)

    def send_mail(self):
        content = 'EVENT DETECTED .. EVENT DETECTED .. EVENT DETECTED .. EVENT DETECTED .. EVENT DETECTED  ..!'
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(self.myMail, self.myMailPass)
        mail.sendmail('', self.toMail, content)
        mail.close()

    def __init__(self, session, domain, server_url, username, password, myMail, myMailPass, toMail):
        self.session = session
        self.domain = domain
        self.server_url = server_url
        self.username = username
        self.password = password
        self.myMail = myMail
        self.toMail = toMail
        self.myMailPass = myMailPass
