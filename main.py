from __future__ import print_function

import pickle
import os.path
import gsheets
import slack_bot

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from slackclient import SlackClient


def main():
    """
        Shows basic usage of the Sheets API.
        Prints values from a spreadsheet.
    """
    creds = None

    # If modifying these scopes, delete the file token.pickle.
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

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
                'credentials.json', scopes)
            creds = flow.run_local_server()
        # Save the credentials for the next run

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    #
    # load access token
    f = open("access.txt", 'r')
    acc = f.readline()
    f.close()

    # instantiate Slack client
    slack_client = SlackClient(acc)

    # The ID and range of a sample spreadsheet.
    spreadsheet_id = '15GCDx1G46ux8-VhBQzXu5nK8lL2BkeKcF-24bhlQWAA'

    user = input("Enter your lastname: ")

    user_cells = gsheets.get_user_cell(service, spreadsheet_id, user)

    if not user_cells:
        slack_bot.send_message(slack_client, "Ты даже не гражданин! \n https://www.youtube.com/watch?v=UOkpO--XtH0")


if __name__ == '__main__':
    main()
