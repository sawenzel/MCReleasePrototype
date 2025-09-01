import json
import argparse
import os
import glob
import sys

"""
Checks a CVMFS daily software tag against
the status-database of nightly GRID runs.
Spits out good or bad for as CI decision.
"""

def check_package(job, threshold):
    try:
        total = int(job.get("Total", 0))
        err = int(job.get("Err", 0))
    except ValueError:
        return "bad"

    if total == 0:
        return "bad"  # no jobs = bad by definition?

    err_pct = (err / total) * 100
    return "bad" if err_pct > threshold else "good"

def main():
    parser = argparse.ArgumentParser(description="Check SoftwarePackage job health")
    parser.add_argument("software", help="SoftwarePackage to check (e.g. O2sim::v20250901-1)")
    parser.add_argument("--threshold", type=float, default=20.0,
                        help="Error percentage threshold (default: 20%)")
    parser.add_argument("--datadir", default="data", help="Directory containing nightly status JSONS")
    args = parser.parse_args()

    merged_files = glob.glob(os.path.join(args.datadir, "merged_*.json"))
    if not merged_files:
        print("No merged datasets found", file=sys.stderr)
        sys.exit(1)

    overall_status = "good"

    for mf in merged_files:
        with open(mf, "r", encoding="utf-8") as f:
            jobs = json.load(f)

        status = None
        for job in jobs:
            if job.get("SoftwarePackage") == args.software:
                status = check_package(job, args.threshold)
                break

        if status is None:
            print(f"{mf}: {args.software} not found")
            continue

        print(f"{mf}: {args.software} → {status}")
        if status == "bad":
            overall_status = "bad"

    print(f"Final status for {args.software}: {overall_status}")
    if overall_status == "bad":
        sys.exit(1)  # nonzero exit so Actions can fail downstream

if __name__ == "__main__":
    main()
