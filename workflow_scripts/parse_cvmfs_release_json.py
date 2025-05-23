import json, sys

def extract_repos(release_json_path):
    with open(release_json_path) as f:
        data = json.load(f)

    def flatten_deps(deps):
        for key in ["build", "runtime"]:
            for dep in deps.get(key, []):
                name = dep["name"]
                tag = dep.get("tag", "UNKNOWN")
                source = dep.get("source")
                if not source:
                    source = f"https://github.com/AliceO2Group/{name}"
                yield name, tag, source

    repos = dict(flatten_deps(data["dependencies"]["direct"]))
    return repos

if __name__ == "__main__":
    # expects a JSON file with base and new tag
    release_file = sys.argv[1]
    release_tags = {}
    with open(release_file) as fp:
      release_tags = json.load(fp)
    
    print (release_tags)
    current = extract_repos(release_tags["base_tag"] + '.meta.json')
    previous = extract_repos(release_tags["new_tag"] + '.meta.json')
    print(json.dumps({"previous": previous, "current": current}))
