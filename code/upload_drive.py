from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    folder_id = []
    for item in items:
        if item['name'] in 'Supreme Talk':
            folder_id.append(item['id'])
            print("folder Found:" + str(folder_id[0]))
            break
    
    if len(folder_id) == 0:
        file_metadata = {
            'name': 'Supreme Talk',
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = service.files().create(body=file_metadata,
                                            fields='id').execute()
        folder_id.append(file['id'])
        print("folder Created: " + str(folder_id[0]))

    media = MediaFileUpload('supremeText.txt', mimetype="text/plain")
    service.files().create(
        body = {
            "name" : "supremeText.txt",
            "parents" : folder_id
        },
        media_body = media,
        fields = 'id'
    ).execute()

    print("File Uploaded!")

def authoriseDrive():
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

def upload():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        authoriseDrive()
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)


    service = build('drive', 'v3', credentials=creds)

    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    folder_id = []
    for item in items:
        if item['name'] in 'Supreme Talk':
            folder_id.append(item['id'])
            print("folder Found:" + str(folder_id[0]))
            break
    
    if len(folder_id) == 0:
        file_metadata = {
            'name': 'Supreme Talk',
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = service.files().create(body=file_metadata,
                                            fields='id').execute()
        folder_id.append(file['id'])
        print("folder Created: " + str(folder_id[0]))

    media = MediaFileUpload('supremeText.txt', mimetype="text/plain")
    service.files().create(
        body = {
            "name" : "supremeText.txt",
            "parents" : folder_id
        },
        media_body = media,
        fields = 'id'
    ).execute()

    print("File Uploaded!")

if __name__ == '__main__':
    main()