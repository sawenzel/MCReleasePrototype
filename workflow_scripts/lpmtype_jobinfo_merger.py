import json
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Merge job JSONs by SoftwarePackage (per lpmtype)")
    parser.add_argument("inputs", nargs="+", help="Input job JSON files (from extract_jobs.py)")
    parser.add_argument("--output", required=True,
                        help="Path to output merged JSON file (e.g. data/merged_27506.json)")
    args = parser.parse_args()

    merged = {}

    # If output already exists, load it first
    if os.path.exists(args.output):
        with open(args.output, "r", encoding="utf-8") as f:
            try:
                existing_jobs = json.load(f)
                for job in existing_jobs:
                    spkg = job.get("SoftwarePackage")
                    if spkg:
                        merged[spkg] = job
            except json.JSONDecodeError:
                print(f"Warning: {args.output} is not valid JSON, ignoring it.")

    # Merge all new inputs
    for infile in args.inputs:
        with open(infile, "r", encoding="utf-8") as f:
            jobs = json.load(f)
            for job in jobs:
                spkg = job.get("SoftwarePackage")
                if not spkg:
                    continue
                if spkg not in merged:
                    merged[spkg] = job
                else:
                    # Overwrite fields with latest data
                    merged[spkg].update(job)

    # Save result
    merged_list = list(merged.values())
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(merged_list, f, indent=2, ensure_ascii=False)

    print(f"Merged into {args.output} with {len(merged_list)} SoftwarePackages")

if __name__ == "__main__":
    main()
