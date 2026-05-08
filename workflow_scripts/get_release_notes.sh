BASE_PATH=/cvmfs/alice.cern.ch/el9-x86_64/Packages/
CURR_TAG=O2PDPSuite/MC-prod-2026-v6-1
FINAL_TAG=O2PDPSuite/MC-prod-2026-v7-1
CAND_TAG=O2PDPSuite/daily-20260506-0000-1

echo "${BASE_PATH}/${CURR_TAG}" > compare-tags.txt
echo "${BASE_PATH}/${CAND_TAG}" >> compare-tags.txt
echo "Stage 1"
python3 get_release_tags.py compare-tags.txt > tags.json
echo "Stage 2"
python3 parse_cvmfs_release_json.py tags.json > repo_deltas.json
echo "Stage 3"
python3 extract_commits.py --base-tag ${CURR_TAG} --new-tag ${FINAL_TAG} --daily-candidate-tag ${CAND_TAG} --whitelist ../release_note_filter.yml
