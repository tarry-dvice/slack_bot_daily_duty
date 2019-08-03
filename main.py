from __future__ import print_function
from access import aut_slack, aut_sheets

import gsheets
import slack_bot


def main():
    """
        Prints values from a spreadsheet.
    """

    service, spreadsheet_id = aut_sheets()

    slack_client = aut_slack()

    # Just test of sending message
    user = input("Enter your lastname: ")

    user_cells = gsheets.get_user_cell(service, spreadsheet_id, user)

    if not user_cells:
        slack_bot.send_message(slack_client, "Ты даже не гражданин! \n https://www.youtube.com/watch?v=UOkpO--XtH0")


if __name__ == '__main__':
    main()
