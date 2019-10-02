from credentials import get_credentials
from get_id import ListMessagesMatchingQuery

service = get_credentials()
query = 'ibsupport@standardbank.co.za'
messages = ListMessagesMatchingQuery(service, 'me', query)
message_id = messages[0]['id']


email_thing = service.users().messages().get(userId='me',id=message_id).execute()

for i in range(len(email_thing['payload']['headers'])):
    if email_thing['payload']['headers'][i]['name'] == 'From':
        print(email_thing['payload']['headers'][i]['value'])

    if email_thing['payload']['headers'][i]['name'] == 'Date':
        print(email_thing['payload']['headers'][i]['value'])

    #print(email_thing['payload']['headers'][i])

#print(len(email_thing['payload']['headers']))
