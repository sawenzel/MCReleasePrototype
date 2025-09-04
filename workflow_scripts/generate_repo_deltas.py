import json
import sys
import re
import subprocess
with open(sys.argv[1]) as file:
    data = json.load(file)
data = json.load(open(sys.argv[1]))
previous = data["previous"]
current = data["current"]

deltas = {}
for reponame in current:
    tag = current[reponame]["tag"]
    if old_tag != tag and "source" in current[reponame]:
       deltas[reponame] = {"from": old_tag, "to": tag, "source": current[reponame]["source"]}
       deltas[reponame] = {"from": old_tag, "to": tag, "source" : current[reponame]["source"]}

with open("repo_changes.md", "w") as f:
    for repo, tags in deltas.items():
        f.write(f"- `{repo}`: `{tags['from']}` → `{tags['to']}`\n")

# now we can directly fetch the relevant commits for packages whitelistes
whitelist = {}
with open("detailed_release_notes_filter.txt", "r") as file:
    for line in file:
        if not re.match("^#", line):
           whitelist[line.strip()] = 1

print ("Whitelisted repos", whitelist)

def fetch_commits(repo, source, tag1, tag2):
    subprocess.run(["git", "clone", "--quiet", "--depth=100", source, repo])
    log = subprocess.check_output([
        "git", "-C", repo, "log", f"{tag1}..{tag2}"
    ], text=True)
    commits = log.strip().split("\n")
    return commits

commits = {}
for reponame in deltas:
    if reponame in whitelist:
       commits[reponame] = fetch_commits(reponame, deltas[reponame]["source"], deltas[reponame]["from"], deltas[reponame]["to"])
    else:
       print (f"{reponame} not in whitelist")

print(json.dumps(commits, indent=2))