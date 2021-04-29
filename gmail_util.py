from secrets_util import GMAIL_CREDS
import smtplib

def send_email(TO):
    SUBJECT = '[HappyMakiGames] Verify your email address to get started with your game'
    TEXT = 'Welcome to Happy Maki Games! To verify your email address, simply click the link below:\n\n' \
           'https://www.google.com\n\n' \
           'The link expires after 30 minutes. If the link does not work, ' \
           'please copy and paste the URL into a browser. For inquiries, please contact HappyMakiGames@gmail.com' \
           'Thanks!\n Happy Maki Games'

    # Gmail Sign In
    gmail_sender = GMAIL_CREDS["username"]
    gmail_passwd = GMAIL_CREDS["password"]

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: noreply-verification@happymaki.com', #'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print (f'email sent to {TO}')
    except:
        print ('error sending mail')

    server.quit()

if __name__ == "__main__":
    send_email("toonling6@gmail.com")

