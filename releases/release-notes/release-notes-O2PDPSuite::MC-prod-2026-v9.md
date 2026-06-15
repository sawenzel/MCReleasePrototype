# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v9-1 in comparison to the previous tag O2PDPSuite/MC-prod-2026-v8-1.

The release is based on the daily tag O2PDPSuite/daily-20260612-0000-1.


## Repository Updates
- **EPOS4HQ**: `v1.0hq-alice5` → `v1.0hq-alice6`
- **EPOS4**: `v4.0.3-alice5` → `v4.0.3-alice6`
- **GEANT4**: `v11.2.0-alice1` → `v11.2.0-alice2`
- **Monitoring**: `v3.19.12` → `v3.19.14`
- **O2**: `daily-20260522-0000` → `daily-20260612-0000`
- **O2DPG**: `daily-20260522-0000` → `daily-20260612-0000`
- **GEANT4_VMC**: `v6-6-update1-p3` → `v6-6-update2-p3`
- **VMC**: `v2-1` → `v2-2`
- **O2Physics**: `daily-20260522-0000` → `daily-20260612-0000`
- **QualityControl**: `v1.192.0` → `daily-20260612-0000`
- **AliGenO2**: `v20260522` → `v20260612`
- **O2sim**: `async-20260522.1` → `v20260612`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- e6a7a9ef0f AOD Writer: correct reserve for cpvClusters
- f50077dd78 RICH: make local Z the radial axis for radiator and photosensor tiles (#15503)
- a684e5aa06 DPL: properly reserve memory when writing (#15510)
- 323df58cec [IOTOF] Update in the TOF digitization (#15493)
- 2fe8a26835 [ALICE3] IOTOF: Configurable radii for cylinder TOF (#15501)
- d9f827c397 Add ITS stuck-pixel CCDB object output (#15468)
- 94d919870d ITS: add back the code for track following (#15456)
- 6bc6de6d05 bugfix: do not overwrite intial z-vertex position
- 2c94782a00 Fix memleak in ConfKeyValues
- cc226e91eb Avoid unneeded lambda
- 280dac70c2 Fix memleaks due to unmanaged ExpandPathName
- 46c24d7abf MathUtils: speed up Chebyshev field eval via FMA-grouped Clenshaw
- 8e372de599 GPU/TPC: Use qTot as marker for HIP clusters instead of qMax (#15481)
- 0853880a41 GPU/TPC: Encode saturated qTot and tailLength in ClusterNative (#15472)
- e731821405 ITS: constexpr computePhi
- 1a18e76952 optional use of Geant4 fluence weighting added (#15417)
- d9fbe030d8 Optionally store refs on ITS parts of all PV contributors
- babe031809 Fix PDG codes for Lc resonances
- 9f1e44a975 Add Lc resonances to physics constants
- b9971bc9b3 Fix TPC-only tracks DCA calculation
- 145d5ea659 Add PV-related rejections to cosmic matcher for interleaved mode
- f3cc9592ec ITS3: opt. staggering and fixes to alignment (#15401)
- 4a5adf1049 TOF: pre-filter hypotheses in getStartTimeInSet to reduce (#15442)
- 1d8606ece1 Update ALICE3 RICH base parameters to v3b (#15398)
- 68a9560f2d Ft3 tiling bugfixing & module feature update (#15409)
- a8b684cf0b ITSMFT: ITS3: fix asserts in TopoDict
- bd619d006c Avoid filling a vector just to count the bits
- ac48d72874 ITS: Remove redundant 'const' from getter methods

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- c4bafe94 Keep track of resonance intermediate state in coalescence (#2379)
- 061b4201 [PWGJE] add parametrised model fast sim (#2375)
- 9a9a5411 DQ InjectedInclusiveJpsiPsi2SMidy generators (#2350)
- 7278c4a7 AOD: Apply aod-parent option only when available
- 5597f516 AODBcRewriter: restore BC sort in Stage 0, keep track regrouping
- c19050ca Add Lc DPMJET trigger support for PWGUD Starlight configs (#2376)
- cdb0b6ec Add NeNe and OO EPOS4HQ configurations (#2374)
- f9529055 Fix typo in CCDB path to FT0 EventsPerBc
- c912611f [PWGHF] Add Pythia8 B- CRmode2 config and BToDeuteron trigger ini (#2366)
- db02ffaf PWGHF: beauty production production at forward y with natural decay and muon trigger (#2367)
- 28b44ef0 AODBcRewriter: regroup tracks by collision so the -1 group stays contiguous (#2370)
- 61a7bb7e Apply correction for energy (non)conservation in coalescence for c-deuteron (#2372)
- 15818907 MC/PWGEM: add ini for DYee in pp at 13.6 TeV (#2369)
- ac1edfe5 Forgotten include (#2371)
- e882201c Add generator and config for charmed nuclei (c-deuteron)  (#2368)
- 216e56d9 MC/PWGEM: update DY generator in OO (#2356)
- c840d7f9  Add configuration for Pb-Pb with hadronic rescattering  (#2364)
- 46876005 Photon energy in header (#2365)

## Contributors
- Andreas Morsch
- Daiki Sekihata
- Fabrizio
- Felix Schlepper
- Felix Weiglhofer
- Giorgio Alberto Lucia
- Giulio Eulisse
- Jaehyeok Ryu
- Justus Rudolph
- MRazza
- Marcello Di Costanzo
- Marco Giacalone
- Maximiliano Puccio
- NNicassio99
- Nicole Bastid
- Rrantu
- SCHOTTER Romain
- Sandro Wenzel
- aimeric-landou
- altsybee
- apalasciano
- mbroz84
- shahoian
- shreyasiacharya
- sigurd
- swenzel