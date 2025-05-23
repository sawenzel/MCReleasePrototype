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
    # ok, so here we extract the meta.json files for
    # 2 given releases to then read the precise release specification

    current = extract_repos(sys.argv[1])
    previous = extract_repos(sys.argv[2])
    print(json.dumps({"previous": previous, "current": current}))
