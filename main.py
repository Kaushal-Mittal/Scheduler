from stanfordcorenlp import StanfordCoreNLP
import outlook
from getpass import getpass

mail = outlook.Outlook()
email_id = raw_input('Email : ')
password = getpass()
mail.login(email_id, password)
mail.inbox()
mail.getEmail(len(mail.allIds()))
nlp = StanfordCoreNLP(r'/home/kaushal/stanford-corenlp-full-2018-02-27')

sentence1 = mail.mailbody()
# print sentence1

list1 = nlp.ner(sentence1)

d = ''
t = ''
for (x, y) in list1:
    if(y == 'DATE'):
        d += (x+' ')
    elif (y=='TIME'):
        t += (x+' ')
print "Date" + " : " + d + "\n" + "Time" + " : " + t

nlp.close()
