import json, subprocess, os
import argparse
import yaml
import re
import shutil
import os

parser = argparse.ArgumentParser(description="Extracts git commits for various repos between 2 cvmfs tags")
parser.add_argument("--repos", default="repo_deltas.json", help="File describing the repo diffs")
parser.add_argument("--whitelist", default="release_note_filter.yml", help="File specifying repos to include")
parser.add_argument("--base-tag", default="", help="The base tag (for the report to compare to)")
parser.add_argument("--new-tag", default="", help="The tag for the release (for the report)")
parser.add_argument("--daily-candidate-tag", default="", help="The daily tag on which this release is based")
parser.add_argument("--generate-report", help="")
args = parser.parse_args()

deltas = json.load(open(args.repos))

# Load whitelist
with open(args.whitelist) as f:
    whitelist_data = yaml.safe_load(f)

# # Convert into a dict for easier lookup
whitelist = {
    entry["name"]: entry.get("dirs", [])
    for entry in whitelist_data["repositories"]
}

commits = {}

def generate_release_notes(deltas_transformed, commits, whitelist, base_tag="", release_tag="", daily_tag="", filename="release-notes.md"):
    lines = ["# Release Notes\n"]

    lines.append(f"\nThese are release notes for {release_tag} in comparison to the previous tag {base_tag}.\n")    
    if len(daily_tag) > 0:
       lines.append(f"The release is based on the daily tag {daily_tag}.\n\n")

    # (a) Repository rundown
    lines.append("## Repository Updates")
    any_changes = False
    for repo, data in deltas_transformed.items():
        prev_tag, new_tag = data.get("previous-tag"), data.get("new-tag")
        if prev_tag != new_tag:
            lines.append(f"- **{repo}**: `{prev_tag}` → `{new_tag}`")
            any_changes = True
    if not any_changes:
        lines.append("_No repositories updated._")

    # (b) Whitelisted commits
    lines.append("\n## MC Relevant Changes")
    any_commits = False
    for repo, repo_commits in commits.items():
        if repo_commits:
            any_commits = True
            dirs = whitelist.get(repo, [])
            dir_list = ", ".join(f"`{d}`" for d in dirs) if dirs else "_(no dir filters)_"
            lines.append(f"\n### {repo}")
            lines.append(f"This is the list of commits in dirs matching: {dir_list}\n")
            for commit in repo_commits:
                lines.append(f"- {commit}")
    if not any_commits:
        lines.append("_No relevant commits found._")

    # Write file
    with open(filename, "w") as f:
        f.write("\n".join(lines))

    print(f"Release notes written to {os.path.abspath(filename)}")

# transforms the code into dict of repos containing url and old and new tag
def transform(data):
    out = {}
    pkgs = set(data["previous"]) | set(data.get("current", {}))
    for p in pkgs:
        prev, curr = data["previous"].get(p, {}), data.get("current", {}).get(p, {})
        out[p] = {
            "source": curr.get("source") or prev.get("source"),
            "previous-tag": prev.get("tag"),
            "new-tag": curr.get("tag")
        }
    return out

deltas_transformed = transform(deltas)
print (deltas_transformed)

for repo, repo_data in deltas_transformed.items():
    print(f"Looking into {repo}")
    if repo not in whitelist:
        print(f"repo {repo} not in whitelist")
        continue

    url = repo_data['source']
    # If repo dir exists, delete it
    if os.path.exists(repo):
        shutil.rmtree(repo)

    subprocess.run(
        ["git", "clone", "--quiet", "--no-single-branch", "--tags", url, repo],
        check=True
    )

    # Get log with full diff names (to match regex later)
    log_cmd = [
        "git", "-C", repo, "log",
        f"{repo_data['previous-tag']}..{repo_data['new-tag']}",
        "--oneline", "--name-only"
    ]
    raw_log = subprocess.check_output(log_cmd, text=True)

    # Split into commits and filter by dirs regex
    repo_commits = []
    current_commit = None
    for line in raw_log.splitlines():
        if re.match(r"^[0-9a-f]+\s", line):  # new commit line
            current_commit = line
        elif line.strip():  # file path
            if any(re.match(pattern, line.strip()) for pattern in whitelist[repo]):
                if current_commit != None:
                   repo_commits.append(current_commit)
                current_commit = None  # prevent duplicates
    commits[repo] = repo_commits

with open("commits.json", "w") as f:
    json.dump(commits, f, indent=2)


#if args.release_notes:
generate_release_notes(deltas_transformed, commits, whitelist, base_tag=args.base_tag, 
                       release_tag=args.new_tag, daily_tag=args.daily_candidate_tag, filename="release-notes.md")