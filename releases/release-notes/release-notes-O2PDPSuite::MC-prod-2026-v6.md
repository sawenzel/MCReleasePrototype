# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v6-1 in comparison to the previous tag O2PDPSuite/MC-prod-2026-v5-1.

The release is based on the daily tag O2PDPSuite/daily-20260424-0000-1.


## Repository Updates
- **utf8proc**: `v2.6.1` → `v2.11.2`
- **JETSCAPE**: `v3.1.1-alice6` → `v3.1.1-alice7`
- **libwebsockets**: `v4.3.2` → `v4.3.4`
- **DataDistribution**: `v1.6.9` → `v1.6.11`
- **madgraph**: `v3.5.2` → `v3.5.13`
- **JAliEn-ROOT**: `0.7.16` → `0.7.17`
- **Monitoring**: `v3.19.11` → `v3.19.12`
- **DDS**: `3.16` → `3.18`
- **GLFW**: `3.3.2` → `3.4`
- **MCStepLogger**: `v0.6.1` → `v0.6.2`
- **lz4**: `v1.9.3` → `v1.10.0`
- **O2**: `daily-20260325-0300` → `daily-20260424-0000`
- **ninja**: `None` → `fortran-v1.11.1.g9`
- **O2Physics**: `daily-20260325-0000` → `daily-20260424-0000`
- **O2sim**: `async-20260329.1` → `v20260424`
- **CRMC**: `v1.7.0-correctHepMC` → `v1.7.0-alice1-correctHepMC`
- **libuv**: `v1.40.0` → `v1.52.0`
- **O2DPG**: `daily-20260325-0000` → `daily-20260424-0000`
- **cgal**: `4.12.2` → `6.1.1`
- **QualityControl**: `v1.188.1` → `daily-20260424-0000`
- **Upcgen**: `upcgen-o2-25-12-24-1` → `upcgen-o2-26-03-02-1`
- **boost**: `v1.83.0-alice2` → `v1.90.0-alice1`
- **AliGenO2**: `v20260329` → `v20260424`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 3f9b8d7ff2 AOD producer: improve MC collision labels for embedded events
- c060a1e58a CCDB: add extra metrics for amount of data requested / fetched
- 7ca700a7e5 TPCFastTransform: Do not pollute the global namespace
- bc57538b4e GPU TRD: Reduce headers included in interface class
- 8cdbc9af86 Remove unnecessary GPUCA_GPUCODE protection in non-GPU code
- a6000dbdec TPC: Make TPC calibration objects constructible from standalone benchmark
- 4bfb3015d5 GPU Common: Add GPUCommonConfigurableParam to support ConfigurableParam classes in GPU code
- 02c4e153e1 GPU: Renaming and removal of obsolete macros / defines
- 5500dfcc81 Cleanup: Remove old version of jobutils and cpulimit tool
- b61cf4a80b Tentative improvement of 3-body decay cov. matrix creation
- b50e6f2d05 [ALICE3] TRK:  update geometry, fix in extrusions, cleanup (#15262)
- b7bfb2c0c2 [ALICE3] Rough attempt to pave ML disks as done for OT (#15269)
- 14ff7dbba9 TPC: Processing of common mode values in O2 (#15137)
- c9acd57add ITS: staggering (#15188)
- 85fad0700b [ALICE3] TRK: Introduce Almira params and shorten ROF/response for TRK (#15267)
- 9e8f22b292 fix wrong long_to_int converstion in TOF readout window indexing
- 4f060ca921 C++ standard fobids specializations of is_trivially_copyable
- ebf039321e [ALICE3] Copy class of ITSMFT Hit for TRK Hit (#15194)
- ea6b15c374 [ALICE3] TRK: Collect services in a dedicated volume assembly (#15215)
- 74c8049248 [ALICE3] IOTOF: allow reduced sensor thickness wihout reducing chip size (#15247)
- bbb4570480 [ALICE3] IOTOF: Adjust layer radius calculations for stave tilt and chip thickness (#15220)
- aa5d3c6ec3 FT0: update Digitizer signal shape and trigger logic; FV0: update trigger logic in digitizer (#15209)
- 1b673ecbb2 [ALICE3] Fix extrusions in forward tracker (#15242)
- db1ede319f Revert "DPL: Better detection for injected workflows (fixed) (#15202)"
- 5ca454afeb Proter time-slice calibration from stray TFs
- ea49c665ef ITS3: alignment code (#15161)
- 081240b92a Fix BasicCCDBManager::isCacheValid(ts) method (#15223)
- 85d4143e39 [ALICE3] IOTOF: fix non segmented layers (#15195)
- 87b9775293 DPL: Better detection for injected workflows (fixed) (#15202)
- a628b60489 DPL: use constexpr for data description of EOS data header (#15175)

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 7d26cc39 Update of FIT digitizer parameters for 2025 data (#2330)
- 55530df3 Flat π⁰ and η Distribution for High- pT    Statistics (#2318)
- f401783c [PWGHF] removed primary deuteron from PYTHIA (#2328)
- 110e721f Clean up vertexing parameters in o2dpg_sim_config.py
- a1fff032 Enforce merge-by-name AOD merging for MC-DATA embedding
- 95cc50b4 Fix concatenation for McCollisions indexed Trees
- a935d7d4 [PWGLF] Added injected configuration to use flat rapidity and pt (#2327)
- d5418b94 Set proper settings for ITS vertexer
- 556f5602 ITS: propagate settings to wfx (#2323)
- 458ff61b add generator for NeNe based on EPOS4 (#2322)
- afdcafc7 update missing decay channels of resonances (#2320)
- 30358fa5 Config files for the charm baryon in ppref (#2316)
- e633fcf4 Enabled injection scheme with uniform rapidity and pT (#2315)
- a509bd7b [PWGLF] Added configuration for baryonic resonances  efficiency studies for Light ION (#2311)
- 2fc42f71 Update probQQtoQ and BeamRemnants settings in config (#2312)

## Contributors
- Anton Alkin
- Chuntai
- David Rohr
- Felix Schlepper
- Francesco Noferini
- Giulio Eulisse
- Hirak Koley
- MRazza
- Marco Giacalone
- Marco van Leeuwen
- Maximiliano Puccio
- Nasir Mehdi Malik
- Nicolò Jacazio
- Rashi gupta
- Sandro Wenzel
- Stefano Cannito
- Tuba Gündem
- alcaliva
- ehellbar
- sawan
- shahoian
- shahor02
- spulawsk