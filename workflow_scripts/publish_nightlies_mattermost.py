# A script to publish MC nightly testing status to a dedicated mattermost channel.
#

from mattermostdriver import Driver
import json
import os
import requests
import argparse

parser = argparse.ArgumentParser(description="Create O2sim nightlies summary badge")
parser.add_argument("--api-token", help="Mattermost API token")
parser.add_argument("--text", default="Foo")
parser.add_argument("--software-package", help = "The package for which we want to publish (determines mattermost thread)")
parser.add_argument("--badge-files", nargs="+", help = "List of nightly badge files to read status from")
parser.add_argument("--mattermost-threads-cache", help = "A file containing a software package to mattermost messag id mapping")
args = parser.parse_args()

def get_mm_thread_id(cachefile, swversion):
    """Retrieve the thread id for a given swversion from cachefile (JSON)."""
    if not os.path.exists(cachefile):
        return None

    with open(cachefile, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    
    return data.get(swversion)

def write_mm_thread_id(cachefile, swversion, id):
    """Write/update the thread id for a given swversion in cachefile (JSON)."""
    data = {}
    if os.path.exists(cachefile):
        with open(cachefile, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    
    data[swversion] = id
    
    with open(cachefile, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def extract_badge_message(badge_file):
    """Iterate over JSON files and extract 'message' field."""
    message = None
    path = badge_file
    if not os.path.exists(path):
      print(f"⚠️ Skipping missing file: {path}")
    else:
      try:
        with open(path, "r", encoding="utf-8") as f:
          data = json.load(f)
          message = data.get('label','Unknown') + " : " + data.get('message','Unknown')
      except (OSError, json.JSONDecodeError) as e:
        print(f"⚠️ Failed to read {path}: {e}")
    
    return message


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

# retrieve mattermost id
action = "create"
mm_thread_id = get_mm_thread_id(args.mattermost_threads_cache, args.software_package)
if mm_thread_id != None:
    action = "update"

# Get channel ID
TEAM_NAME="alice"
# CHANNEL_NAME="o2dpg-mc-nightly-tests-foo"
CHANNEL_NAME="testchannel"

team_id = driver.teams.get_team_by_name(TEAM_NAME)["id"]
channel_id = driver.channels.get_channel_by_name(team_id, CHANNEL_NAME)["id"]

# read badge files and extract

nightly_text = f"Nightly status for **{args.software_package}** : \n"
for badge in args.badge_files:
   status = extract_badge_message(badge)
   nightly_text += "... " + status + "\n"

if action == "create":
  print ("Creating a post")
  post = driver.posts.create_post({
           "channel_id": channel_id,
           "message": nightly_text
         })
  print (post)
  # save the message id for reuse
  write_mm_thread_id(args.mattermost_threads_cache, args.software_package, post['id'])
elif action == "update":
  print ("Updating a post")
  driver.posts.update_post(
      mm_thread_id,
      {
        'id' : mm_thread_id,
        'channel_id' : channel_id,
        'message' : nightly_text,
        'root_id' : ''
      }
  )
else:
  pass