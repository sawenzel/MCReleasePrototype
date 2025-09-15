import json
import argparse

"""
Use job info to produce a summary JSON used
for a badge.
"""
def create_badge(job, label, threshold = 20):
    def make_int(input):
        return int(input) if input != '' else 0

    total = make_int(job.get("Total", 0))
    done = make_int(job.get("Done", 0))
    waiting = make_int(job.get("Wait", 0))
    active = make_int(job.get("Active", 0))
    err = make_int(job.get("Err", 0))
    
    message = "✅ good"
    color = "green"
    stat = f"[{done}/{err}/{waiting+active}]"
    if total == 0:
       message = "bad"
       color = "red"
    elif waiting > 0:
       message = "⚠️ waiting" # can't take decision yet
       color = "orange"
    elif active > 0:
       message = "🏃 running"
       color = "orange"
    else:
       err_pct = (err / total) * 100
       if err_pct > threshold:
           message = "❌ bad"
           color = "red"

    message = message + " " + stat

    badge = {
     "schemaVersion": 1,
     "label": label,
     "message": message,
     "color": color
    }
    return badge


def main():
    parser = argparse.ArgumentParser(description="Create O2sim nightlies summary badge")
    parser.add_argument("--status-file")
    parser.add_argument("--badge-file")
    parser.add_argument("--label", default="", help = "Label for this badge")
    parser.add_argument("--threshold", default=20, help="Error threshold in percent")
    args = parser.parse_args()
    
    max_pid = 0
    with open(args.status_file, "r", encoding="utf-8") as f:
        jobs = json.load(f)

        status = None
        # one pass to find the latest job
        max_pid = max([j.get("PID") for j in jobs])
        
        # we need to find latest job. By definition will have largest process id
        for job in jobs:
            if job.get("PID") == max_pid:
               print (f"Creating badge for {job}")
               badge = create_badge(job, args.label + " / " + job.get("SoftwarePackage", ""), args.threshold)
               break

        # write out the badge
        with open(args.badge_file, "w") as f:
           json.dump(badge, f, indent=2)

if __name__ == "__main__":
    main()