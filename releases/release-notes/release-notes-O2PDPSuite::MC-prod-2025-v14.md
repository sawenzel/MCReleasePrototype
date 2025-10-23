# Release Notes


These are release notes for O2PDPSuite::MC-prod-2025-v14 in comparison to the previous tag O2PDPSuite::MC-prod-2025-v13.

The release is based on the daily tag O2PDPSuite::daily-20251023-0000-1.


## Repository Updates
- **KFParticle**: `v1.1-6` → `v1.1-7`
- **O2**: `daily-20251010-0000` → `daily-20251023-0000`
- **ODC**: `0.86.0` → `0.87.0`
- **AliGenO2**: `v20251010` → `v20251023`
- **O2DPG**: `daily-20251010-0000` → `daily-20251023-0000`
- **gpu-system**: `error` → `cuda_arch@86#89@_12.9.86-rocm_arch@gfx906#gfx908@_6.3.42134-opencl-miopen-migraphx-cudnn-tensorrt`
- **O2sim**: `async-20251010.1` → `v20251023`
- **O2Physics**: `daily-20251010-0000` → `daily-20251023-0000`
- **Control-OCCPlugin**: `v1.44.0` → `v1.45.0`
- **QualityControl**: `v1.183.0` → `daily-20251023-0000`
- **DDS**: `3.13` → `3.16`
- **ROOT**: `v6-32-06-alice10` → `v6-36-04-alice2`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 39824aefb8 ALICE3-TRK: adding macro to check digitization output (#14736)
- fc241f407e Adding cuts for air (#14755)
- 10dd81bb69 Generators: Embedd into correct event when using collision-context
- cba3d9131e FD detector (#13476)
- 009371b997 ability to take inject external vertices in collision context
- 516303f147 Example to run HERWIG7 with o2-sim
- eaeee05067 corrected positions of volumes in RB24 after recent Cave updates
- 3fbf25307e TOF: param utilities are separated in a dedicated library for O2Physics usage (#14730)
- 21d965eaeb Fix unwanted behaviour in signal filtering with embedding pattern different from (#14735)
- 14c234e582 fix methods is/setInNominalSector of TOF cluster
- a35cf1e514 Fix precalculated sector cos/sin values in TOF Geo
- a657810d92 ALICE3-TRK: several fixes in the digitization code (#14733)
- 24d15d0410 Set default DCA in case of propagate call fail (#14729)
- 84d8383406 ITS3: fix longeron length to not clip into Hring
- 03eba8ea89 ITS3: remove unnecessary recalculation of trackingframe
- ac31e61182 ITS3: add some services material and update MatLUT macro
- a662980a87 [Common] Add eta, omega and eta' to PhysicsConstants.h

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 8ccc9996 Fix a quoting problem related to CCDB remapping
- aef777fc 2tag: Correctly restore user-overwritten O2DPG env vars
- f7eb97c1 [PWGDQ] New ini file with Trigger Ratio = 2 (#2162)
- 355a5325 Added OO-Gun for nuclei and hypernuclei (#2158)
- 58270d6f add `ini`, `cfg` config files and  test macro for OO collision (#2157)

## Contributors
- Andrea Sofia Triolo
- Chuntai
- Fabrizio
- Felix Schlepper
- Hadi Hassan
- Marco Giacalone
- Marvin Hemmer
- Nicolò Jacazio
- Podist Kurashvili
- Sandro Wenzel
- amorsch
- arvindkhuntia
- ddobrigk
- sgaretti
- shahoian
- swenzel