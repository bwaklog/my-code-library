import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "adimhegde@gmail.com"
    msg['from'] = user
    password = "uljenleshcrjqzaa"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    entry = '''
HOUSE        : D-004
VISITOR NAME : Visitor - 1
VISIT REASON : General Visit
'''

    email_alert("Hey", entry, "adityamhegde@icloud.com")
