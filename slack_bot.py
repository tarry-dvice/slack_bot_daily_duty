from slackclient import SlackClient

# load access token
f = open("access.txt", 'r')
acc = f.readline()
f.close()

# instantiate Slack client
slack_client = SlackClient(acc)


def send_message(client, message):
    if client.rtm_connect(with_team_state=False):
        print("Daily Duty Bot connected and running!")

        slack_client.api_call(
            "chat.postMessage",
            channel="DKNF6MR8A",
            text=message
        )

    else:
        print("Connection failed. Exception traceback printed above.")
