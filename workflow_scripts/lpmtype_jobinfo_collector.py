import os
import glob
import requests
from bs4 import BeautifulSoup
import json
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Extract job info from ALICE MonALISA into JSON"
    )
    parser.add_argument(
        "--lpmtype",
        required=True,
        help="LPM type identifier (e.g., 27506)"
    )
    parser.add_argument(
        "--output",
        default="jobs.json",
        help="Output JSON file (default: jobs.json)"
    )
    args = parser.parse_args()

    # Construct URL
    url = f"https://alimonitor.cern.ch/prod/jobs.jsp?t={args.lpmtype}"
    print(f"Fetching {url}")

    tmpdir = os.environ.get("TMPDIR", "/tmp")
    cert_pattern = os.path.join(tmpdir, "tokencert_*.pem")
    certfile = glob.glob(cert_pattern)
    key_pattern = os.path.join(tmpdir, "tokenkey_*.pem")
    keyfile = glob.glob(key_pattern)

    if not keyfile:
      raise FileNotFoundError(f"No proxy certificate found in {proxy_pattern}")

    # Fetch HTML with client cert
    response = requests.get(url, cert=(certfile[0], keyfile[0]), verify=False)
    response.raise_for_status()
    html = response.text

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="sortable")

    header_rows = table.find("thead").find_all("tr")
    final_headers = [td.get_text(strip=True) for td in header_rows[-1].find_all("td")]

    keep_headers = {
        "PID",
        "Run no.",
        "Output directory",
        "Total",
        "Done",
        "Active",
        "Wait",
        "Err."
    }

    data = []
    for row in table.find("tbody").find_all("tr", class_="table_row"):
        cells = row.find_all("td")
        row_data = {}
        for header, cell in zip(final_headers, cells):
            text = cell.get_text(strip=True)

            # Keep only selected headers
            if header in keep_headers:
                # Normalize "Err." → "Err"
                key = "Err" if header == "Err." else header
                try:
                    row_data[key] = int(text)
                except ValueError:
                    row_data[key] = text

            # Detect SoftwarePackage
            if "::" in text:
                row_data["SoftwarePackage"] = text

        if "PID" in row_data:
            data.append(row_data)

    # Save JSON
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(data)} rows into {args.output}")


if __name__ == "__main__":
    main()
