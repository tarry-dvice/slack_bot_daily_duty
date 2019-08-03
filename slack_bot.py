from access import aut_slack


def send_message(client, message):
    """
        Send message to user from Slack bot
    """

    slack_client = aut_slack()

    if client.rtm_connect(with_team_state=False):
        print("Daily Duty Bot connected and running!")

        slack_client.api_call(
            "chat.postMessage",
            channel="DKNF6MR8A",
            text=message
        )

    else:
        print("Connection failed. Exception traceback printed above.")
