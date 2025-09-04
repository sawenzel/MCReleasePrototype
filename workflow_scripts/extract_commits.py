import json, subprocess, os

deltas = json.load(open("repo_deltas.json"))
whitelist = {line.strip() for line in open("whitelist.txt")}

commits = {}

for repo, tags in deltas.items():
    if repo not in whitelist:
       continue
    url = f"https://github.com/AliceO2Group/{repo}.git"
    subprocess.run(["git", "clone", "--quiet", "--depth=100", url, repo])
    log = subprocess.check_output([
        "git", "-C", repo, "log", f"{tags['from']}..{tags['to']}", "--oneline"
    ], text=True)
    commits[repo] = log.strip().split("\n")

with open("commits.json", "w") as f:
    json.dump(commits, f, indent=2)
