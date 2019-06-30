import time
from slackclient import SlackClient

f = open("access.txt", 'r')
acc = f.readline()
f.close()

# instantiate Slack client
slack_client = SlackClient(acc)
# daily_bot's user ID in Slack: value is assigned after the bot starts up
daily_bot_id = None

# constants
RTM_READ_DELAY = 1  # 1 second delay between reading from RTM


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Daily Duty Bot connected and running!")

        # Read bot's user ID by calling Web API method `auth.test`
        daily_bot_id = slack_client.api_call("auth.test")["user_id"]

        slack_client.api_call(
            "chat.postMessage",
            channel="DKNF6MR8A",
            text="Hello"
        )

    else:
        print("Connection failed. Exception traceback printed above.")
