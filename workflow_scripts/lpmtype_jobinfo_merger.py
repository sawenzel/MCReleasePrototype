import json
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Merge job JSONs by SoftwarePackage")
    parser.add_argument("inputs", nargs="+", help="Input job JSON files")
    parser.add_argument("--existing", default="data/merged.json",
                        help="Path to existing merged JSON file (if any)")
    parser.add_argument("--output", default="data/merged.json",
                        help="Output merged JSON file")
    args = parser.parse_args()

    merged = {}

    # Load existing file if present
    if os.path.exists(args.existing):
        with open(args.existing, "r", encoding="utf-8") as f:
            try:
                existing_jobs = json.load(f)
                for job in existing_jobs:
                    spkg = job.get("SoftwarePackage")
                    if spkg:
                        merged[spkg] = job
            except json.JSONDecodeError:
                print(f"Warning: {args.existing} is not valid JSON, ignoring it.")

    # Merge new inputs (overwrite fields if SoftwarePackage already exists)
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
                    merged[spkg].update(job)

    # Save result
    merged_list = list(merged.values())
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(merged_list, f, indent=2, ensure_ascii=False)

    print(f"Merged into {args.output} with {len(merged_list)} SoftwarePackages")

if __name__ == "__main__":
    main()
