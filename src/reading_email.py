import base64
import os.path
from glob import glob
from apiclient import errors
from datetime import datetime
from src.get_email_date import Get_email_date
import sys

files_downloaded = 0
files_that_exist = 0
def GetAttachments(service, user_id, messages, cache_path):
    global files_downloaded
    global files_that_exist
    """Get and store attachment from Message with given id.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: ID of Message containing attachment.
    store_dir: The directory used to store attachments.
    """
    for message in messages:
        msg_id = message['id']
        path=""
        try:
            message = service.users().messages().get(userId=user_id, id=msg_id)\
                        .execute()

            email_date, valid_date = Get_email_date(service, msg_id)
            if valid_date and file_check(email_date,cache_path):
                for part in message['payload']['parts']:
                    if part['filename']:

                        attachment = service.users().messages().attachments()\
                                    .get(userId='me', messageId=message['id'],\
                                    id=part['body']['attachmentId']).execute()

                        file_data = base64.urlsafe_b64decode(attachment['data']\
                                    .encode('UTF-8'))

                        time_curr = datetime.now()
                        time_str = time_curr.strftime("%Hh%Mm%Ss")
                        path = os.path.join(cache_path, part['filename'])
                        path = f"{path[:-4]}_{email_date}_{time_str}.pdf"
                        files_downloaded += 1
                        f = open(path, 'wb')
                        f.write(file_data)
                        f.close()

            sys.stdout.write(f"\rFiles downloaded: {files_downloaded} --- "\
                            f"Files that already exist: {files_that_exist}")
            if files_that_exist > 10:
                break
        except errors.HttpError as error:
            print(f'An error occurred: {error}')
    print()

def file_check(email_date, path):
    """Checks if email attachement has already been downloaded"""
    global files_that_exist
    
    file_checked = True
    possible_files = os.path.join(path, "*.pdf")
    file_dict = {}
    for file_name in glob(possible_files):
        curr = file_name[-24:-14]
        if curr in file_dict.keys():
            file_dict[curr] = 2
        else:
            file_dict.update({curr : 1})
    if email_date in file_dict.keys():
        if file_dict[email_date] == 2:
            files_that_exist += 1
            file_checked = False

    return file_checked
