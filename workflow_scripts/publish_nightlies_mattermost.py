# A script to publish MC nightly testing status to a dedicated mattermost channel.
#

from mattermostdriver import Driver
import json
import os
import requests
import argparse

parser = argparse.ArgumentParser(description="Create O2sim nightlies summary badge")
parser.add_argument("--api-token")
parser.add_argument("--text", default="Foo")
args = parser.parse_args()

# Configuration
driver = Driver({
  'url': 'mattermost.web.cern.ch',
  'token': args.api_token, # 'API_TOKEN_OF_THE_BOTUSER'
  'scheme': 'https',
  'port': 443,
  'verify': True,
  'websocket': True,
  'debug': False
})

# Login
driver.login()
bot_user_id = driver.users.get_user('me')['id']
print(f"Logged in as bot user: {bot_user_id}")

# Edit original post with real content
# driver.posts.update_post(thinking_post['id'], {
#                    'id': thinking_post['id'],
#                    'channel_id': channel_id,
#                    'message': llm_reply,
#                    'root_id': thread_root_id })

# Get channel ID
TEAM_NAME="alice"
# CHANNEL_NAME="o2dpg-mc-nightly-tests-foo"
CHANNEL_NAME="testchannel"

team_id = driver.teams.get_team_by_name(TEAM_NAME)["id"]
channel_id = driver.channels.get_channel_by_name(team_id, CHANNEL_NAME)["id"]

post = driver.posts.create_post({
         "channel_id": channel_id,
         "message": args.text
     })

print (post)

# Load existing threads mapping (version → post_id)
# if os.path.exists("threads.json"): # ---> threads
#    with open("threads.json") as f:
#        threads = json.load(f)
#else:
#    threads = {}

# Build message
# if status == "pass":
#     text = f"✅ Tests passed for **{version}**\n![badge]({badge_url})"
# else:
#     text = f"🚨 @channel Tests failed for **{version}**\n![badge]({badge_url})"

# Post or update thread
# if version in threads:
#     # Reply in existing thread
#     root_id = threads[version]
#     post = mm.posts.create_post({
#         "channel_id": channel_id,
#         "message": text,
#         "root_id": root_id,
#     })
# else:
#     # Create new thread
#     post = mm.posts.create_post({
#         "channel_id": channel_id,
#         "message": text,
#     })
#     threads[version] = post["id"]

# # Save updated mapping
# with open("threads.json", "w") as f:
#     json.dump(threads, f)