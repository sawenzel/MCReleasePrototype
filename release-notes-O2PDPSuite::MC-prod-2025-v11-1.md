# Release Notes

## Repository Updates
- **JAliEn-ROOT**: `0.7.14` → `0.7.15`
- **O2sim**: `async-20250806.1` → `v20250904`
- **Control-OCCPlugin**: `v1.40.0` → `v1.42.0`
- **O2DPG**: `daily-20250806-0000` → `daily-20250904-0000`
- **libjalienO2**: `0.1.4` → `0.1.5`
- **O2**: `daily-20250806-0000` → `daily-20250904-0000`
- **FairMQ**: `v1.10.0` → `v1.9.2`
- **AliGenO2**: `v20250806` → `v20250904`
- **O2Physics**: `daily-20250806-0000` → `daily-20250904-0000`
- **QualityControl**: `v1.178.0` → `daily-20250904-0000`
- **gpu-system**: `error` → `cuda_arch@86#89@_12.9.86-rocm_arch@gfx906#gfx908@_6.3.42134-opencl-miopen-migraphx-cudnn-tensorrt`
- **Clang**: `v18.1.8` → `v20.1.7`

## MC Relevant Changes

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 532a4d86 MC picks up the FIT-related options used in o2-tof-matcher
- 1ee4f301 [PWGHF] new files for production of electrons from heavy-flavour hadron decays (#2106)
- 78d79332 [PWGDQ] Adding configuration for light nuclei (#2107)
- 6983ae6f Improvements for MCProdInfo; MCProdInfo harvester tool
- a7b8de25 Iteration on AODBcRewriter
- fef755cf Fix decreasing time trend of loopers in last event (#2102)
- ba0105c2 2stage testing logfile keeping
- cee54bde Adding utility to remove duplicate BCs from a MC-AO2D
- a53c0bd7 Separate the cgf files for each baryon (#2097)
- 56d1ff5f Add pythia pp 5.02 TeV to generators (#2098)
- 01f1eb02 Update test_looper.sh
- 58478fda Add config for pools of undecayed Xic+ in pp collisions at 13 TeV (#2085)
- 5622cefd Flat Gas external generator (#2094)
- 6bbcd05f Add generator energies for MC sims (#2096)
- f68d1aea Fix shellcheck issues
- 6821a4cc improvements to grid_submit
- a7433af8 more improvements for 2tag testing
- a767cbc9 allow for custom O2DPG repo in anchored testing
- 617b5e82 make TPC residual merging conditional
- 7844f382 improve 2tag testing output
- 6e3720e2 Store CTP lumi in CTP digits in anchored sim.
- 889a7251 Add TPC residuals merging stage for tfs of a job
- db61c442 Extra process in the script
- e03a5138 Allow TPC residual extraction in MC and data corr maps in the reco
- 1a30c42b typo fix
- 1b06695b commit missing file
- e0cf0526 Setup to test anchorMC in the 2tag approach
- 5367c37f Improvements for grid_submit
- d3ec5a36 Extra Jpsi decay and Neon setup
- e0a508a9 [PWGLF] Add OO cascade-enriched ini file (#2071)

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- cfa791d765 add best knowldge of collision time in tof matching info (#14615)
- 8735573dd1 ALICE3-TRK: first version of working digitizer (#14619)
- dec2fe8515 A3: Add customization of detector MID/Magnet/Absorber radius (#14621)
- ff42ca25aa Data Model: provide size when deallocating a Stack
- a4dd82a477 Fix alignment so that jemalloc / address sanitizer do no complain
- 7278b4e3e4 TPC: sort buffer of pressure in case it is not sorted
- 88321c2a56 Minor fixes of debug printouts
- 3e1afe2b25 Method to translate TOF cluster to nominal sector frame
- 06c1b84595 Enable ROOT file output in TPC chunked-digit merger (#14608)
- 9b8fb2326d TPC: Add scaling of VDrift with T/P (#14602)
- 556556aeec ZDC: Add getter for hit secondary flag
- fa7d8f9274 Revert "Fix in TRD sector getter"
- 7262c36703 Fix in TRD sector getter
- 3912592e85 Align: Fix using local delta matrix
- 44cd710321 Align: print delta frame and level
- c35a2cdf7c Geo: optional print out alignment matrices
- 3cafea04f8 Revert "Fix alignment so that jemalloc / address sanitizer do no complain"
- fe9e22661f Revert "DPL: move to std::pmr where possible" This reverts commit 83467b3c67f9b51545b730c3fff5904419ea2806.
- 947b41ba5a Revert "Data Model: provide size when deallocating a Stack"
- 999ac719cf Make sure extra tracks are randomized to avoid PHOS hole losses
- bbef7a7e93 Data Model: provide size when deallocating a Stack
- e96552ab9d Update README so example code has std::
- 28345fbd29 Get rid of C++ extension warning
- 83467b3c67 DPL: move to std::pmr where possible