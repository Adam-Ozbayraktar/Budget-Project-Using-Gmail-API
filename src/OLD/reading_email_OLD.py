"""Retrieve an attachment from a Message.
"""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import base64
from apiclient import errors



def service_account_login():
    SCOPES = ['https://mail.google.com/']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def GetAttachments(service, user_id, msg_id, store_dir):
  """Get and store attachment from Message with given id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: ID of Message containing attachment.
    store_dir: The directory used to store attachments.
  """

  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    for part in message['payload']['parts']:
      if part['filename']:
        print(part['filename'])
        attachment = service.users().messages().attachments().get(userId='me', messageId=message['id'], id=part['body']['attachmentId']).execute()
        file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))

        #path = ''.join([store_dir, part['filename']])
        path = os.path.join(store_dir, part['filename'])
        print(path)
        f = open(path, 'wb')
        f.write(file_data)
        f.close()

  except errors.HttpError as error:
    print(f'An error occurred: {error}')

  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    for part in message['payload']['parts']:
      if part['filename']:

        file_data = base64.urlsafe_b64decode(part['body']['data']
                                             .encode('UTF-8'))

        path = ''.join([store_dir, part['filename']])

        f = open(path, 'w')
        f.write(file_data)
        f.close()

  except errors.HttpError as error:
    print ('An error occurred: %s' % error)
"""

service = service_account_login()
FILE_PATH = r'C:\Users\Study\Downloads'
GetAttachments(service, 'me', '16c8ea8d5c1167de', FILE_PATH)
