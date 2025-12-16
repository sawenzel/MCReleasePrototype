BASE_PATH=/cvmfs/alice.cern.ch/el9-x86_64/Packages/
CURR_TAG=O2PDPSuite/MC-prod-2025-v14-1
FINAL_TAG=O2PDPSuite/MC-prod-2025-v15-1
CAND_TAG=O2PDPSuite/daily-20251203-0000-1

echo "${BASE_PATH}/${CURR_TAG}" > compare-tags.txt
echo "${BASE_PATH}/${CAND_TAG}" >> compare-tags.txt
python3 get_release_tags.py compare-tags.txt > tags.json
python3 parse_cvmfs_release_json.py tags.json > repo_deltas.json
python3 extract_commits.py --base-tag ${CURR_TAG} --new-tag ${FINAL_TAG} --daily-candidate-tag ${CAND_TAG} --whitelist ../release_note_filter.yml
