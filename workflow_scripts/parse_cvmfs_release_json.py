import json, sys

def extrac_info(data):
    info = {}
    for entry in data:
        name = entry["name"]
        tag = entry.get("tag", "UNKNOWN")
        source = entry.get("source")
        info[name] = { "tag" : tag , "source" : source }
    return info

def extract_repos(release_json_path):
    data = {}
    with open(release_json_path) as f:
      data = json.load(f)

    return extrac_info(data["dependencies"]["recursive"]["runtime"])
    
if __name__ == "__main__":
    # expects a JSON file with base and new tag
    release_file = sys.argv[1]
    release_tags = {}
    with open(release_file) as fp:
      release_tags = json.load(fp)
    
    previous = extract_repos(release_tags["base_tag"] + '/.meta.json')
    current = extract_repos(release_tags["new_tag"] + '/.meta.json')

    print(json.dumps({"previous": previous, "current": current}))
