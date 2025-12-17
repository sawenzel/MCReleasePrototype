# Release Notes


These are release notes for O2PDPSuite/MC-prod-2025-v16-1 in comparison to the previous tag O2PDPSuite/MC-prod-2025-v15-1.

The release is based on the daily tag O2PDPSuite/daily-20251217-0000-1.


## Repository Updates
- **libjalienO2**: `0.1.5` → `0.2.0`
- **gpu-system**: `error` → `cuda_arch@86#89@_12.9.86-rocm_arch@gfx906#gfx908@_6.3.42134-opencl-miopen-migraphx-cudnn-tensorrt`
- **Control-OCCPlugin**: `v1.45.3` → `v1.46.1`
- **ROOT**: `v6-36-04-alice2` → `v6-36-04-alice3`
- **Python**: `v3.9.16` → `v3.10.19`
- **QualityControl**: `v1.184.5` → `daily-20251217-0000`
- **O2**: `daily-20251203-0000` → `daily-20251217-0000`
- **O2DPG**: `daily-20251203-0000` → `daily-20251217-0000`
- **AliGenO2**: `v20251203` → `v20251217`
- **O2sim**: `async-20251203.1` → `v20251217`
- **O2Physics**: `daily-20251203-0000` → `daily-20251217-0000`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 528a5a5913 Refine parameter getter methods with error handling (#14794)
- 0244a9838f ITSMFT&ITS3&TRK: load response functions from ccdb (#14902)
- 7394855057 Reco: Add cov setters for ind. elements
- 33a68caa22 Common: new linkdef for TimeStamp
- 2eba0da019 Common: add host symbols to RangeRef
- d6d20b4ec4 GPU DataTypes / QA: Clean up some data types / enums
- c628d29798 Integrate non-uniform InteractionSampler into CollisionContextTool
- 7ffc897643 Use new User Agent in CCDB
- 93ff0dcf60 ALICE3-TRK: adjusted VD segmentation taking into account gaps between adjacent layers (#14903)
- 6db969d4c5 Introducing non-uniform mu InteractionSampler
- 3cbed2e40e Add GRPLHCIF to AggregatedRunInfo
- 53130312ee TRD add digit phases to CTF encoding, collapse phases on reading.
- 7b3397d53e Fix for headers-only CCDB uploads
- b6c63a0b2c [FT3] Modular structure for OT disks - first version of modules structure with dynamic disks paving for ALICE 3 sensors and initial material estimations (#14816)
- 99a77145c0 Add possibility for head only object
- 754936f607 Use stable lin.ref. point for alignment track initial fit

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- b925a337 Fix mother index and decay chain issue (#2197)
- 8ca8e843 Make precollcontext task outside-configurable
- 4c4bdca5 Script to extract/upload BcTVX from EvtSelQA
- c81c6484 scripts to delete CCDB objects from the test instance
- dd5dca12 Scripts for MC-DATA embedding
- a435c840 Use uniformly DOTPCRESIDUALEXTRACTION env.var
- 8b60d31d Fix test macro for Ds-reso MC, checking also 425 pdg code. (#2210)
- e5707720 Fix test macro for Sc bkg, checking for D*+. (#2209)
- 55ce5b1a MC production for glueball study (#2211)
- fd508bfa Fix HF tests (#2208)
- 22da9869 Add LF generator for MC with coalescence production for De Tr He3 (#2207)
- c359dc30 O2DPG MC: Support for missing MID
- 56699f6c TPC digitizer should not use internal multi-threading
- 7f7a3412 Correct deuteron pdg code
- 868db817 Add pythia CLR-BLC Modes 0,2,3  (#2201)
- 9dc9ea3d Add files via upload (#2199)

## Contributors
- Andrea Sofia Triolo
- David Rohr
- Fabrizio
- Felix Schlepper
- Francesca Ercolessi
- Jseo
- Martin Eide
- Mattia Faggin
- Nicolò Jacazio
- Rita Sadek
- Sandro Wenzel
- Sean Murray
- klsmith15k
- sawan
- shahoian
- wiechula