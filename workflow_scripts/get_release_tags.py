#
#
import sys, json

def read_tags(file):
    with open(file) as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines[-2:]  # last two tags

tags = read_tags(sys.argv[1])

# You can define the repo set here per tag
release_def = {
    "base_tag" : tags[0],
    "new_tag" : tags[1]
}

print(json.dumps(release_def))
