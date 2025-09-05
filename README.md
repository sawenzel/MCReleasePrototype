![Badge1](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/sawenzel/MCReleasePrototype/refs/heads/O2sim-nightly-status/o2sim_nightlies_status/badge_30350.json?token=GHSAT0AAAAAADITBGZGEG2ZK5ONZNA6DD7C2F3DVSQ)
![Badge2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/sawenzel/MCReleasePrototype/refs/heads/O2sim-nightly-status/o2sim_nightlies_status/badge_27506.json)
![Badge3](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/sawenzel/MCReleasePrototype/O2sim/badge_27506.json)

# MCReleasePrototype
Playground to get ALICE MC release-QC pipeline

Goal is to have automatic pipeline to

(a)
- make a new MC release (propsosal)
- build the software stack
- publish the software stack
- run test jobs against the proposed software stack
- produce plots, do release validation

(b)
- pilot-run provided job scripts on the GRID
- actually job-script pipelines !
- report back feedback about jobs / QC
- show links to production things

(c) 
- run analysis QC jobs on existing productions
- input: LHC production, sampling rate
- show

(d)
- collect list of open MC productions
- collect list of MC tags in use
- produce dynamic documentation (lists)
