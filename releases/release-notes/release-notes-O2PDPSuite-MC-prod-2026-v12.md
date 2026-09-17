# Release Notes


These are release notes for O2PDPSuite::MC-prod-2026-v12 in comparison to the previous tag O2PDPSuite::MC-prod-2026-v11.

The release is based on the daily tag O2PDPSuite::daily-20260917-0000-1, with O2DPG taken from commit
90c0a3d259b814aeb6f687bcfdea6dec4694e94f (one commit after that daily's O2DPG tag).

## Highlights for MC productions

- **MC truth and labels.** Fixed a stale track-ID mapping between events in the MC stack, an offset applied to invalid track indices when merging sub-events, and a label encoded for signals without an MC particle. `isFromRadDecay` ancestry walk fixed.
- **Embedding.** Mother indices are now reassigned correctly after pruning HF events, and a segfault after coalescence from HF decays is fixed. The ccbar/bbbar ratio is tunable.
- **Timeframes without collisions.** Each timeframe gets its own collision-context slot; TPC digitization and the looper generator handle an empty timeframe.
- **Anchored MC.** `anchorMC` no longer anchors to parts of a run without collisions, uses learned resource estimates, and sizes the QED interaction spec to the QED event pool. `o2dpg_sim_workflow.py` is adapted to the new TPC correction maps. The 2-tag (alternative-reco) setup of `anchorMC.sh` and `anchorMC_DataEmbedding.sh` no longer loses the MC software environment when a module version contains `@` (O2DPG#2463). The anchoring point is shifted past the ITS ramp-up in both of its coordinates, so a job at production offset 0 no longer sits in the ramp where the ITS time-dead map masks every chip (O2DPG 90c0a3d259).
- **Simulation.** Per-track random seeding now works with Geant4. New TPC 83mKr calibration generator with Geant4 ionisation-fluctuation support. EMCal digitizer fix (EMCAL-1156). ZNC cross-section ratio applied after the pile-up correction.
- **Geometry.** Field-free media for the L3 magnet and compensator. MFT cooling pipe bends get their material back; TPC inner field cage prepreg strip and sector-17 gas pipe placement fixed; several TOF MANY overlaps removed. TRD and MFT volumes deduplicated; TPC half-space cuts replaced by boxes; ZEM placed in the barrel volume.
- **CCDB.** The CCDB URL is no longer hardcoded, to support the new CCDB setup (#15779).
- **Reconstruction.** DCAFitter X-error regularization applied only where needed; faster material LUT.
- **Generators.** New EPOS4 configurations and several new PWGLF, PWGHF, PWGDQ and jet configurations (see O2DPG list).
- **Externals.** ROOT `v6-36-10-alice4`, arrow `v25.0.0`, ONNXRuntime `v1.29.0`, protobuf/grpc/abseil updates, VecGeom v2 support; TGeo2VecGeom, OCCT and pythonOCC added.

## Validation

- 2-tag compatibility test: Jenkins O2DPG-2TAG-TESTING #68 — SUCCESS.
- AO2D RelVal on the pp nightly `LHC22k5_nightly`, done with the preceding daily `daily-20260916-0500-1` (303457, O2sim v20260819-1 vs 303485, O2sim v20260916-1; the 94 common subjobs, AnalysisQC with `daily-20260916-0500-1`, RelVal default thresholds): 832 objects; 145 GOOD, 119 BAD, 568 empty on both sides. The generated collision count is identical (689934). The MC vertex RMS is about 1.7% larger in x, y and z: the generated vertices are identical, but the older software stored MC collisions with a vertex of exactly (0,0,0) in the AO2D (255 of 7287 in subjob 001), which the new software no longer writes. Reconstructed collisions per generated collision rise from 0.502 to 0.519 and propagated tracks by 3.6%, in line with the geometry, material and TPC reconstruction changes of this release.

## Repository Updates
- **alibuild-recipe-tools**: `v0.3.0` → `v0.4.0`
- **c-ares**: `1.18.1` → `1.34.6`
- **Monitoring**: `v3.19.16` → `v3.19.17`
- **pythonOCC**: `None` → `v7.9.3`
- **grpc**: `v1.71.0` → `v1.74.0`
- **OCCT**: `None` → `v7.9.3`
- **AliGenO2**: `v20260729` → `v20260917`
- **O2sim**: `async-20260729.1` → `v20260917`
- **ONNXRuntime**: `v1.22.0` → `v1.29.0`
- **onnx**: `v1.17.0-alice2` → `v1.22.0`
- **JAliEn-ROOT**: `0.7.21` → `0.7.22`
- **O2**: `daily-20260729-0000` → `daily-20260917-0000`
- **QualityControl**: `v1.194.0` → `daily-20260917-0000`
- **xsimd**: `14.0.0` → `14.2.0`
- **O2DPG**: `daily-20260729-0000` → `90c0a3d259` (master, one commit after `daily-20260917-0000`)
- **arrow**: `v20.0.0-alice1` → `v25.0.0-alice`
- **TGeo2VecGeom**: `None` → `v0.1.2`
- **FreeType**: `v2.10.1` → `v2.13.3`
- **protobuf**: `v29.3` → `v31.1`
- **cudnn_frontend**: `None` → `v1.24.0`
- **ROOT**: `v6-36-10-alice2` → `v6-36-10-alice4`
- **cutlass**: `None` → `v4.4.2`
- **abseil**: `20240722.0` → `20250814.0-alice1`
- **libxml2**: `v2.9.3` → `v2.15.3`
- **gpu-system**: `cuda_13.1.115_arch@75_virtual@_home_F52XG4RPNRXWGYLMF5RXKZDBBI000000-rocm_6.3.42134_arch@gfx906@_home_F5XXA5BPOJXWG3IK-opencl-miopen-migraphx-cudnn-tensorrt` → `cuda_13.1.115_arch_75_virtual-rocm_6.3.42134_arch_gfx906-opencl-miopen-cudnn-tensorrt`
- **O2Physics**: `daily-20260729-0000` → `daily-20260917-0000`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 7f21a971f8 TPC: add 83mKr calibration generator with Geant4 ionisation-fluctuation support
- 9fbf91563f Fix codechecker violations
- 23fb5bd519 [ALICE3] Fix some overlaps between services and supports (#15793)
- 26c5d61084 Handle new CCDB setup by avoiding hardcoding the CCDB url (#15779)
- b122c5f1f1 IOTOF: add in-pixel efficiency (#15786)
- a2ad1348cb Upgrade the CAD to TGeo converter
- 67a360831e Add the CADSupport module with the exact BVH surface solid
- 2aa6d6112f [MUON] Fix assignment of GlobalFwdTrack from base class (#15785)
- b7d563b8ef Switch for the pre-PR-15610 compatibility mode (set as default)
- 54198c006b DCAFitter: apply X-error regularization only where it is needed, drop duplications
- 626c2ad00b Add support for VecGeom v2 (#15737)
- 5d96df35d8 Give the two HMPID absorber plates distinct names
- 5cf6a10b6a Give the FT0 cable container a hole for the beam pipe
- f7f295b896 Fix material bug in FT3 (#15780)
- 868e414baa Implement HepMC reading randomisation
- 8a63905457 [ALICE3] TF3: store BC and TDC in digits
- 10233472d4 [ALICE3] IOTOF: Fix back-propagation of hit in stepping (#15773)
- 40bc7fc519 Remove hardcoded CCDB path
- 7cc729d4de Let the ZEM calorimeters be built without the far beam line (#15752)
- a2f658bcd7 Please consider the following formatting changes
- c26829387e Keep the libcurl header out of CcdbApi.h
- d48b3a3ffa Cross-check the geometry doctor's reachability audit against VecGeom
- 7f7b4f7166 Multi-thread the geometry doctor's reachability audit
- b6258fbf65 Make the geometry doctor's reachability audit trustworthy
- ebfb379184 Fix UB when constructing string
- b5a06a92f8 Fix final so that new clang does not complain
- c575d910d5 Add protection against skipped loopers
- a5a63189d0 [ALICE3] FT3: fix kapton fractional Z (#15753)
- ad9314e2db Deduplicate the MFT flex and the shared ALPIDE metal stack (#15736)
- 21c7380c60 Place the steel tube, not its gas core, on the -x side of the sector-17 gas pipe
- 8f9e1a5e03 Give the front-of-supermodule TRD gas pipes their own names
- 9934f7500d Build twelve TRD chamber shapes instead of thirty
- 75487ac372 Resolve the TRD hit volume lookup to integers at initialisation
- 9325616a6c Write out the TRD chamber dimensions instead of resolving them at run time
- 5f10631bd1 Build the TRD cooling pipes and power lines once per layer
- ee38904013 Share one volume for the MCM cooling pipe stubs in the TRD
- e3b3d79f69 Please consider the following formatting changes
- e56c3286c6 Add a reachability audit to the geometry doctor
- 8beacd09f2 Place the ZEM calorimeters in the barrel volume
- d80c5cbb0b Fix out-of-range hit access in the TOF hit merging
- 10dad2d2ac Place the TOF cooling bars between the FEA containers instead of through them
- d4fb43a040 Seat the TOF Nino mask in a groove instead of a MANY overlap
- cf5861b8ee Position the TOF cooling cross members without MANY
- e25003ab0e Give the MFT cooling pipe bends their material back
- de03530530 [ALICE3] TRK: add the simplified-realistic OT barrel layout (#15646)
- b439f58fdd Simple event pool merger (#15741)
- a4b60c9ccb Fix a misplaced prepreg strip in the TPC inner field cage
- 940909ca47 Replace the TPC half-space cuts by bounded boxes (#15716)
- 2f11433da7 Write one empty TPC digit entry when a timeframe has no collision
- 4da7ffb5ca Let the TPC looper generator accept a timeframe without collisions
- 5351f8ba56 Give every timeframe its own slot in the collision context
- 425d9eea49 Deduplicate MFT capacitor/welding and X7R0402 geometry
- 32d495ad88 Apply the ZNC cross-section ratio after the pile-up correction (#15721)
- 007e9af738 [ALICE3] TF3: switch substaves according to close gaps between staves (#15725)
- c8fdddba6f Reduce Pythia8 verbosity on Hyperloop (#15731)
- a63c2a2555 CCDB: handle access to CCDB via security proxy (#15724)
- 0d2ee8b425 [EMCAL-1156] Modernize EMCal code and fix Digitizer (#15706)
- 7fb26402c5 Follow redirects when truncating/deleting (#15722)
- a3e51177ce faster mat LUT
- ae7df2bd37 CCDB: improved support for CI Security Proxy (#15713)
- bff2b3709f Use field-free media for the L3 magnet and the compensator (#15694)
- 6cc3be0360 Initial setup for G4 FastSim hooks with a toy example for Absorber (#15699)
- 9cda446a96 [ALICE 3] TF3: update OTOF geometry with split staves (#15666)
- 407208ac0a CCDB: add support for bearer token (#15711)
- bf2bdf63de ITSGPU: further optimisations (#15704)
- 9e0fda64e7 [ALICE3] MI3: Add superconducting magnet/cryostat geometry to ALICE3 MID simulation (#15585)
- e0fefa53fd TRK: add nELossSteps (#15703)
- 0d7617dbf7 Do not encode a label for a signal without an MC particle
- 6b2fd4d43b Do not offset an invalid track index when merging sub-events
- 726cbee7b3 Fix stale trackID mapping between events in the MC stack
- 68bd709a36 GPU: propagate architecture name and LTO for ITS
- c2dd585f67 Change division to use float for massInv
- aecea1d229 TRK: add fast getPredictedChi2
- f84a4b582b Rotation2D:  use sincos
- 414e1a275b Change return type to value_T in getCurvature
- 0f02172cfa Refactor TrackUtils.h for value_T consistency
- 3224e1595a Use floating-point literals in TrackUtils.h
- 7c7b0ae6a3 Add o2-sim-geometry-doctor, a geometry against field audit
- 353ed40fc2 Fix CPU accounting for external generator subprocesses
- 61350cd1cb Integrate geometry step killing (#15684)
- ff94004b30 Fixing Clang format
- 7025dd1a5c mplementation of OB FPC Capacitors
- 23411c1f6e Handle list of files in alien paths
- 885e4ea65a Field: keep polarity on MagneticField re-initialisation
- 6339a5a7d2 Fix isFromRadDecay ancestry walk and add a unit test
- f16c6e431f Protect RecoContainer TRDtracklets access in absence of the TRD (#15670)
- 2be94fdf3d Fix cached safety calculation in O2Tessellated
- 303c22f598 Improve safety calculations in Tessellated solid
- 3669c9cbe4 Add method isFromRadDecay(const int id). Checks whether particle resu… (#15470)
- 115d870a2b Pressure: Fix last smoothed pressure value
- b248548a37 Split ALICE3 TRK and FT3 layout (#15657)
- e4d1882bf5 [ALICE3] TF3: add passive edge around each pixel (#15654)
- 43f7fd181a Fix mass value and width
- cd50486284 Add double-omega decay information
- 02a19a3da8 Please consider the following formatting changes
- 905c309bc8 Make per-track random seeding work for Geant4
- aff1d86fae CAD->TGeo: support multiple external modules and sensitive detectors
- 319d397a31 Support to use VecGeom geometry navigation in the material scan
- 9faecc62d8 GeometryManager::getSensID supports up to 2^17 sensors for DetID>FOCAL (#15656)
- 684cad7756 Add barrel reco configParams to AOD metadata. (#15645)
- 5cc27a8850 [ALICE3] TF3: Move hard-coded digitizer parameters to dpldigitizerparams (#15623)
- 3f13a59a65 [ALICE3] Add digitization for the forward tracker (#15620)

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 39ee30b8 Harden module setup and async environment handling in anchorMC
- 6d163ef5 Run the alternative-reco step of anchorMC in a subshell
- fd75cee2 Add a few EPOS4 configurations (#2455)
- a75fe0d2 [PWGGAJE] jet param model: add bkg-only, fix eta (#2452)
- 82d1ca0a add different gap configs for 13 TeV (#2450)
- 860289e5 [PWGLF] Add generator for antideuterons in jets (#2460)
- 0bb96707 Fix reassignment of mother indices after pruning HF events in embedding (#2457)
- b448e9d4 Add generator for V0s in jets with injection (#2459)
- 2a8aa17e Update ini file for cascades in jets (#2458)
- 5afa9432 Fix independent LF resonance gun RNG seeding (#2456)
- 3418de0e Fix missing comment character (#2453)
- f6d13d08 Adapt o2dpg_sim_workflow.py to new TPC corr.maps (#2451)
- 04450fa2 Tunable cb patch (#2448)
- 4fc4713b o2dpg_sim_workflow.py: use the helper function to add workflows
- 89ef5408 [PWG-DQ] Add new ini file to generate single muons at fwd y (#2444)
- 51ea14db Example Pythia8 for HY (#2446)
- 4e2c5243 o2dpg_sim_workflow.py: only add reco tasks of smaller detectors if they are active
- 467683a3 o2dpg_sim_workflow.py: always require MFTRECOtask for MFTMCHMATCHtask
- 08431cd4 o2dpg_sim_workflow.py: clean up trailing white space
- 66bad3a1 Do not anchor an MC to a part of the run that had no collisions
- c2a97f31 Give the QED interaction spec the size of the QED event pool
- dfaedea0 Let learned resource estimates replace dynamic sampling in anchorMC
- a7854c26 tunable ratio of ccbar and bbbar for embedding (#2435)
- a8c42f81 [PWGLF] Revise injection list and add QA codes for injected particles (#2430)
- 5e0a865e Learn the file-IO graph without root, using strace
- d4f14f0d Add a modular workflow runner next to the existing one
- 0cc4061e Prepare o2dpg_sim_metrics.py for the new workflow runner
- 5da6f991 o2_dpg_workflow_runner.py: fix dry-run crash
- e175a5a6 [PWGLF] Added code for flat phase-space MC generator for PWA study (#2433)
- faac260b Fix Xic- name in geant4_externaldecayer_Xic_trigger.in (#2432)
- 411377cc Fix Xic- name used in geant4 configuration (#2431)
- ec32708e Add generator for Double-Omega searches (#2429)
- a0289312 Add configs to force decays of Xic for MC productions for triggered data (#2424)
- a1f47da1 Fix LF resonance gap injection and add phi channel (#2419)
- 9e88429f Fix seg fault caused by stale particle indices after coalescence from HF decays (#2416)
- b4f03d47 Pin reproducer CCDB queries to the original job's run time
- 3e9018ac Fix lambda1405 generator

## Contributors
- ALICE Action Bot
- Andreas Morsch
- Ankur Yadav
- Berkin Ulukutlu
- Chuntai
- David Rohr
- Ernst Hellbar
- Fabrizio
- Fabrizio Chinu
- Felix Schlepper
- Francesco Mazzaschi
- Giorgio Alberto Lucia
- Giulio Eulisse
- Justus Rudolph
- Marcello Di Costanzo
- Marco Giacalone
- Marco van Leeuwen
- Mario Ciacco
- Mario Sitta
- Martin
- Marvin Hemmer
- Matthias Kleiner
- Rocco Liotino
- Sandro Wenzel
- Tristan Wenzel
- aferrero2707
- aimeric-landou
- alcaliva
- jaimenorman
- joseesquivel-hub
- mj525
- sawan
- sgaretti
- shahoian
- shahor02
- swenzel