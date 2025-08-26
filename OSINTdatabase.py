import shelve 
from datetime import datetime
import pyinputplus as Pyip
import time

def save(title, fn, un, dob, loc, gen, sf, su, bio, cp, ce, jt, co, rls, age, act, geo, src, shn):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    template = {'Fullname': fn,
                 'Username': un,
                 'Date of birth': dob,
                 'Location': loc,
                 'Gender': gen,
                 'Social followers': sf,
                 'Social username': su,
                 'Description': bio,
                 'Contact phone': cp,
                 'Contact email': ce,
                 'Job title': jt,
                 'Company/Employer': co,
                 'Relationship': rls,
                 'Recent activity': act,
                 'Age': age,
                 'Geolocation': geo,
                 'Sources(Links)': src,
                 'Short note': shn,
                 'Timestamp of collection': now
                 }
    with shelve.open('OSINTbase.db') as db:
        if title in db:
            db[title].append(template)
        else:
            db[title] = [template]

def search(title):
    with shelve.open('OSINTbase.db') as db:
        if title in db:
            for i, titles in enumerate(db[title], start=1):
                print(f'Listing the details given under "{title}"')
                print('-' * 40)
                print(f'Entry                       : {i}')
                print(f"Fullname                    : {titles.get('Fullname', 'Escaped')}")
                print(f"Username(s)                 : {titles.get('Username', 'Escaped')}")
                print(f"Date of Birth               : {titles.get('Date of birth', 'Escaped')}")
                print(f"Location                    : {titles.get('Location', 'Escaped')}")
                print(f"Gender                      : {titles.get('Gender', 'Escaped')}")
                print(f"Social Followers in Total   : {titles.get('Social followers', 'Escaped')}")
                print(f"All Social Media Username(s): {titles.get('Social username', 'Escaped')}")
                print(f"Description                 : {titles.get('Description', 'Escaped')}")
                print(f"Contact Phone(s)            : {titles.get('Contact phone', 'Escaped')}")
                print(f"Contact Email(s)            : {titles.get('Contact email', 'Escaped')}")
                print(f"Job Title(s)                : {titles.get('Job title', 'Escaped')}")
                print(f"Company/Employer            : {titles.get('Company/Employer', 'Escaped')}")
                print(f"Relationship                : {titles.get('Relationship', 'Escaped')}")
                print(f"Recent Activity             : {titles.get('Recent activity', 'Escaped')}")
                print(f"Age                         : {titles.get('Age', 'Escaped')}")
                print(f"Geolocation                 : {titles.get('Geolocation', 'Escaped')}")
                print(f"Sources                     : {titles.get('Sources(Links)', 'Escaped')}")
                print(f"Short Note                  : {titles.get('Short note', 'Escaped')}")
                print(f"Timestamp of collection     : {titles.get('Timestamp of collection', 'Escaped')}")
                print('-' * 40)
        else:
            print(f'Error: {title} doesn\'t exist in database')

def findall():
    with shelve.open('OSINTbase.db') as db:
        for key in db:
            print(f'\n- {key}')
            print('-' * 40)
        if not db:
            print('No OSINT Report Templates saved yet.')
        

def no(value):
    return value if value else 'N/A'


while True:
    try:
        print('\nWelcome to The Ghost Analyst OSINT Report Template Database')
        start = Pyip.inputInt("""Which of these operations would you like to perform:
1. Save a new OSINT Report Template
2. Search for save OSINT Reports
3. Show Titles of all saved OSINT Reports 
4. Exit                  
============ """, min=1, max=4)
        if start == 1:
            print("""Please take your time to read this well as for creating an OSINT report template in this database,
any question you don't have an answer too here just skip it, no problem with that, thank you.""")
            time.sleep(5)
            title = input('Enter a title to save this OSINT Report to database: ').strip().lower()
            fn = no(Pyip.inputStr('Enter the name of the person: ', blank=True))
            un = no(Pyip.inputStr('Enter the username of the person: ', blank=True))
            dob = no(Pyip.inputStr('Enter date of birth of the person(YYYY-MM-DD): ', blank=True))
            loc = no(Pyip.inputStr('Enter the location of the person: ', blank=True))
            gen = no(input('Enter the gender of the person: '))
            sf = no(Pyip.inputStr('Enter the number of social media followers the person has accross all profiles(eg., Instagram: 3000, Facebook: 4000): ', blank=True))
            su = no(Pyip.inputStr('Enter the social usernames the person has by separating them with a comma(eg., Instagram: Lewis32, Facebook:Lewwy345): ', blank=True))
            bio = no(input('Enter the description of the person or bio of one of their social accounts: '))
            cp = no(Pyip.inputStr('Enter contact phone number of the person it can be more than one number separate with a comma: ', blank=True))
            ce = no(Pyip.inputStr('Enter the email of the person: ', blank=True))
            jt = no(input('Enter Job title of the person: '))
            co = no(Pyip.inputStr('Enter the name of the person\'s company or employer: ', blank=True))
            rls = no(input('Enter the relationship of the person: '))
            act = no(input('Enter the recent activity of the person: '))
            age_input = Pyip.inputInt('Enter the age of the person: ', blank=True)
            age = int(age_input) if age_input.isdigit() else 'N/A'
            geo = no(Pyip.inputStr('Enter the geolocation of the person based on metadata: ', blank=True))
            src = no(Pyip.inputStr('Enter the sources where you used to get the persons information, seperate them with a comma: ', blank=True))
            shn = no(Pyip.inputStr('Enter a short note you\'ll like to add on the information gotten, kindly press enter to skip: ', blank=True))
            print('Saving to database.......\n')
            save(title, fn, un, dob, loc, gen, sf, su, bio, cp, ce, jt, co, rls, age, act, geo, src, shn)
            time.sleep(1)
            print('Information has been stored in a database')
        
        elif start == 2:
            name = input('Enter the title of the OSINT Report Template you want to open: ').strip().lower()
            print(f'Getting {name} from database.......')
            time.sleep(1)
            search(name)
        
        elif start == 3:
            findall()

        elif start == 4:
            print('Bye we hope to see you soon\nExiting CLI.......')
            break
    
    except KeyboardInterrupt:
        print('Exit successful.......')
        break
