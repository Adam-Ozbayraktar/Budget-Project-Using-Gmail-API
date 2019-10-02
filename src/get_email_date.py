from src.credentials import get_credentials
from src.get_id import ListMessagesMatchingQuery
from datetime import datetime

def Get_email_date(service, message_id):
    """Returns the date when the email was sent"""
    valid_date = False
    email_thing = service.users().messages().get(userId='me',id=message_id)\
                    .execute()

    for i in range(len(email_thing['payload']['headers'])):
        if email_thing['payload']['headers'][i]['name'] == 'Date':
            date = email_thing['payload']['headers'][i]['value']
            date = date[5:]
            date = date[:-15]
            date = datetime.strptime(date, '%d %b %Y')
            date_after = "16 Aug 2019"
            date_after = datetime.strptime(date_after, '%d %b %Y')
            date_string = date.strftime("%Y-%m-%d")
            if date > date_after:
                valid_date = True

            return date_string, valid_date

def main():
    print(Get_email_date())

if __name__ == '__main__':
    main()
