# Release Notes


These are release notes for O2PDPSuite/MC-prod-2025-v15-1 in comparison to the previous tag O2PDPSuite/MC-prod-2025-v14-1.

The release is based on the daily tag O2PDPSuite/daily-20251203-0000-1.


## Repository Updates
- **AliGenO2**: `v20251101` → `v20251203`
- **O2**: `daily-20251101-0000` → `daily-20251203-0000`
- **O2sim**: `async-20251101.1` → `v20251203`
- **STARlight**: `20241115` → `20251025`
- **O2Physics**: `daily-20251101-0000` → `daily-20251203-0000`
- **xjalienfs**: `1.6.8` → `1.7.0`
- **FairLogger**: `v2.1.0` → `v2.3.1`
- **alibuild-recipe-tools**: `0.2.5` → `0.2.6`
- **QualityControl**: `v1.184.4` → `daily-20251203-0000`
- **O2DPG**: `daily-20251101-0000` → `daily-20251203-0000`
- **Ppconsul**: `v0.2.3` → `v0.2.3-alice2`
- **Control-OCCPlugin**: `v1.45.2` → `v1.45.3`
- **gpu-system**: `error` → `cuda_arch@86#89@_12.9.86-rocm_arch@gfx906#gfx908@_6.3.42134-opencl-miopen-migraphx-cudnn-tensorrt`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 0ec9c27391 Exclude TPC CalDet test in dataflow builds
- 580d11efdf Methods for Kalman filter linearized wrt reference track
- 1d620f24fb [NN Clusterizer] CCDB fetching within reco workflow (#14841)
- 5b0d25dc15 Possibility to combine 2 material LUTs (#14861)
- 297aa69d7e Fix of custom streamer code
- 133c2ecf89 CalDet<TPCPadFlags>: Protect against invalid reads
- 0fb4692e49 Exercise CalArray<PadFlags> loading in a TPC unit test
- 159cf6a392 o2-sim: Avoid duplicate printout of detector list
- 650f5f5e9a Stability improvement for o2-sim startup
- 8599750dfc o2-sim: Better error handling in req-rep communication in status channel
- 55b66aec6c Set proper EOR to anchored MC GRPECS
- 2439bbec03 Custom member streamer for CalArray<o2::tpc::PadFlags>::mData
- 1d4bf4839c ALICE3-TRK: adapting to recent changes in the ML/OT geometry and to the new type definition o2::trk::Hit (#14831)
- 932036f3a5 Forward interaction rate to collision context
- dae698e672 ALICE3-TRK: fix nSimSteps to cover long hits at large Z + prints cleanup (#14819)
- 3e4c7b1ba3 EncodedBlocks should report real output size, not the allocated buffer
- 02b8c0dae5 Improved description of IB FPC capacitors (#14805)
- 17b6c77bd9 Fix of O2-6437
- 57a66d189d Revert "Fix one-off index problem when copying collision contexts"
- c1a675807a DPL: move TableToTree to AnalysisSupport, on its way to be deprecated
- 898c79334d Fix namespace closing for o2 in BunchFilling.h (#14791)
- 80787ec23b additional features added to TRK geometry (#14772)
- 0efc03f8d2 Fix chip composition and orientation (#14786)
- db55f0819a Fix one-off index problem when copying collision contexts

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 5b59f73d Improvement for --skipModules/--skipReadout
- 79898018 Cleaner --skipModules treatment / remove deprecated -mod
- f483261e Remove deprecated workflow option from scripts
- 0b96a90b Add generator for strangeness in jets (#2194)
- 338d1be2 grid_submit.sh: Basic support to split in InputFileCollections
- 2fe012d4 MC/PWGEM: add MC files for HFll in OO (#2188)
- 1e586579 Implemented Performance Generator (#2159)
- 545fc72c Fix LF_rapidity generator by including generator_pythia8_longlived.C (#2190)
- 8ac59922 ability to take external collision context
- 9197b2f8 Reference particle
- a00eaf1e add POWHEG jet configuration and ini file, pp 13.6 TeV (#2178)
- eb866f38 Automatic IR (#2184)
- 63d61be3 Reduction of nEvents (#2183)
- 14a6c054 added f2(1270), a2(1320) resonances (#2182)
- ccb9ff34 Adjustments for new STARlight version (#2173)
- b8289dc4 MC/PWGEM: add cfg and ini for VM2ll (#2172)
- 13773b58 EPOS: add pp 13.6 TeV (#2176)
- 9abc9395 Make TRD optional; Anchoring improvements

## Contributors
- AizatDaribayeva
- Andrea Sofia Triolo
- Christian Sonnabend
- Daiki Sekihata
- Giulio Eulisse
- Marco Giacalone
- Nicolò Jacazio
- Sandro Wenzel
- Stefano Cannito
- alcaliva
- jaimenorman
- mario6829
- mbroz84
- sawan
- shahoian
- shahor02