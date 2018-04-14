import outlook
from getpass import getpass

mail = outlook.Outlook()
email_id = raw_input('Email : ')
password = getpass()
mail.login(email_id, password)
mail.inbox()
mail.getEmail(len(mail.allIds()))
print mail.mailbody()
