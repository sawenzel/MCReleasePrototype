# Release Notes


These are release notes for O2PDPSuite::MC-prod-2026-v15 in comparison to the previous tag O2PDPSuite::MC-prod-2026-v14.

The release is based on the daily tag O2PDPSuite::daily-20261122-0000-1.

O2PDPSuite::MC-prod-2026-v16 was published by mistake from the same daily tag. It contains the same software as MC-prod-2026-v15 and should not be used.

## Important fixes

This release fixes the collision sampling of anchored MC. Since MC-prod-2026-v9 the sampler that follows the per-BC interaction rate from CCDB (`--nontrivial-mu-distribution`) could pick the same BC twice, so BCs with two or more collisions were about 2.6 times more frequent than Poisson. Such collisions bias the FT0 vertex, which caused a deficit of up to ~15 % of events passing `kIsGoodZvtxFT0vsPV` in OO. With the fix the pile-up agrees with Poisson and the event selection agrees with MC-prod-2026-v1 again (https://its.cern.ch/jira/browse/O2-7330, https://github.com/AliceO2Group/AliceO2/pull/16158).

It also fixes anchored jobs that ran the reconstruction without the anchored settings, because the printout of the reco workflow could be lost (0.1-0.4 % of jobs, visible for instance as twice as many ITS clusters). The printout is now kept, and anchorMC stops a job when it is still missing (https://its.cern.ch/jira/browse/O2-7359, https://github.com/AliceO2Group/AliceO2/pull/16169).

MC timeframes are now aligned with the data using the `FirstOrbitMC` value that each production records in MCProdInfo, replacing a hardcoded list of productions (https://its.cern.ch/jira/browse/O2-7335).

Expected differences with respect to MC-prod-2026-v14: TPC digits come from the multithreaded digitizer with per-sector seeding, the TRD digitizer takes its calibration from CCDB with an updated t0, and FT0 hits no longer reuse photon track ids from a previous sub-event. These change the output statistically, not systematically.


## Repository Updates
- **O2sim**: `async-20261102.1` → `v20261122`
- **GEANT4_VMC**: `v6-6-update4-p4` → `v6-6-update4-p5`
- **MCStepLogger**: `v0.6.2` → `v0.6.3`
- **O2Physics**: `daily-20261102-0000` → `daily-20261122-0000`
- **O2DPG**: `daily-20261102-0000` → `daily-20261122-0000`
- **O2**: `daily-20261102-0000` → `daily-20261122-0000`
- **GBL**: `V04-00-06` → `V04-00-07`
- **AliGenO2**: `v20261102` → `v20261122`
- **QualityControl**: `v1.196.0` → `daily-20261122-0000`
- **GEANT4**: `v11.2.0-alice3` → `v11.2.0-alice5`
- **FairRoot**: `v18.4.9-alice3` → `None`

## MC Relevant Changes

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 57000ab9 Also stop anchorMC on a truncated workflow printout
- fe43e560 Stop anchorMC when the reco workflow printout is missing
- 72907314 Add Gap 5 in deuteron coalescence generator for pp at 13.6 TeV (#2560)
- 2be40bef Record FirstOrbitMC and the software version in MCProdInfo
- 5f698fd9 Round the ITS ramp-up shift with the final orbitsPerTF
- 654a8ced rename ini file
- c55d56ce replace QC digit reader with O2 digit reader for MFT digit QC task in o2dpg_sim_workflow.py
- b5de34cd Run a planned set of DF folders per MC-DATA embedding job
- 8192cf1d Add tools to plan, submit and check MC-DATA embedding productions
- 7ead7b9f Select DF folders and time-order collisions in the embedding utils
- f027c107 Switch off TPC loopers and QED for MC-DATA embedding
- 6427d080 Anchor explicit timeframe IDs to their place in the data
- dbf6d9b6 Allow anchored MC to run the AnalysisQC
- cf554aa6 Add the TPC PID service to AnalysisQC chains that miss it
- 1bd8d5ee grid_submit.sh: allow setting the JDL Price
- 1370c5f0 Fix pylint used-before-assignment errors
- 712da774 Lstar ini files for gap trigger 3 and 4 (#2548)
- dc516512 Make the multithreaded TPC digitizer the default
- c97ed0ee Add opt-in switches for the multithreaded TPC digitizer
- 0427deec Set the static TLS reserve for Geant4 in the simulation tasks
- 8263fe70 update parameters (#2542)
- e5708b88 move unused dependencies in PV finder to AOD producer in o2dpg_sim_workflow.py
- 42c26820 fix dependencies of PV finder and AOD producer in o2dpg_sim_workflow.py
- 9132c207 Photoproduction injection in PbPb hadronic event
- 63939230 tests for prompt gamma config
- 47f4874c add increased MB gaps for prompt photon config
- 5561d030 Count backfill memory in the memory gate of the new runner
- eff59ef4 Add AMPT Generator for OO collisions at 5.36 TeV (#2534)
- f8c0a6da PWGDQ: adding chi_c1(3872) and updating quarkonia proportions (#2536)
- 904a359a Add hybrid genberator for antideuterons in jets (#2537)
- 6ab618e3 Inject UPC events as an independent stream in the UPC example
- 19691bbb Add an example for UPC events in hadronic Pb-Pb pile-up
- 5eb59f19 Add a decay config that lets the EventDecayer decay charm baryons (#2518)
- 5b58ea9f higher MB gaps for testing (#2515)
- c56a1345 Make the TPC time-series task follow the active detectors
- 65e9025a Add MC filtering tools for AO2D files
- cf926bc1 Add coalescence-based deuteron production generator (#2535)
- f5b30593 Add ini file for combined c->D->mu and b->B->D->mu (#2523)
- e9d5f2db Improve Lambda(1520) generator (#2533)

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 39b3f2ec5f Fix return value and size check of setBCIntensityScales
- 8b00be5b1a Add Poisson unit tests for NonUniformMuInteractionSampler
- 840a084224 fix BC jump offset for NonUniformMuInteractionSampler
- 59e9376b83 Align MC timeframes using FirstOrbitMC from MCProdInfo
- 08d05b465d GPU: Unify usage of half precision float into half_t typedef in GPUCommonMath.h
- cc26941379 [ALICE3] TF3: update default sensor parameters (#16150)
- 5c6d39be77 [ALICE3] TRK/FT3 digitizer:  introduced discretization of the timestamp into digits with the ALMIRA ToA timestamp format (#16137)
- 6de374239b Mutex-free TGeo material budget for multithreaded users
- 210a2a7a85 Close the nanometre gaps between EMCAL modules
- cf1343c726 fix sor calculation issue for some MC tags, also consider special cases (#16141)
- a84b2fafad Fix invalid iterator dereference in MaterialManager debug log
- ca01776887 dummy commit to trigger CI PR formatting checks
- 4a6d29b1b8 fixes for TF shifts for MC-prod-2026-v13
- c419989671 Apply PAI in the TRD gas only with the energy-deposit charge
- ad31f647dc Add a TRD ionisation model independent of the Geant4 energy loss
- 4b998878df Remove TRD from the Run 4 detector list
- 5cc7845534 TPC: read rule for the old ClusterNative::qTot
- 7449ca50b8 TPC: fix pair swap when reading CalArray<PadFlags> written by the cus… (#16124)
- 42f413e7c3 MUON: Fix missing include for libfmt12 and GCC 16
- 0b18d57080 Stronger protection for NaN (e<m) in e-loss correction + optimization (#16129)
- d05c98cfcf Do not keep physical nodes when aligning the o2-sim geometry
- 4dfedcb92b ALICE3 Forward Detector update - #15791 (#15967)
- 28ab00cede [ALICE3]: Add FD3 hit (#16118)
- bf2e0354e6 Avoid InheritsFrom in CCDB object extraction
- 4c92364c5b Add a multithreaded TPC digitizer device (#16090)
- de7f6501fb Do not run the multithreaded Geant4 tests on macOS
- 48715bd44d Add a test of o2-sim in multithreaded Geant4 mode
- 30e878543a Add a test that multithreaded o2-sim gives the same output for 1 and N threads
- 50179fc078 Look up the PDG record once per thread and PDG code in the Stack
- 8170834712 Reset the FT0 photon track ids at the end of each event
- b124c373ed Add a multithreaded Geant4 mode to o2-sim
- e314cf9f8b TRD: update of T0 value and possibility to disable shift in the tracklet transformer (#16104)
- f9c9589fb4 Set the static TLS reserve for Geant4 inside the sim executables
- 94e30e8fcd DPL: when updatig params provenance, check if the iterator is not at the end
- 1320d761e2 Add optional per-sector seeding to the TPC digitizer (#16085)
- dbc9f178ed Fix deprecated use of localtime
- 6dad2fe9cb Fix missing header
- 5b3c766666 Fix the inverted and the external primary transport selection in the Stack
- b8dd0a31bc Do not take ownership of CCDB distortion maps in the TPC digitizer
- 5f95228f07 Make the TPC DigitContainer non-copyable
- 7368424055 Fix MC labels carried over between sectors in the TPC digitizer
- bc5ed44b2c Resolve TPC digitizer calibration objects once per sector
- dac10c0c37 Refactor/shared lookuptable (#15667)
- ce1684d6cb FileFetcher acknowledges suppression of processed files (#16078)
- d273816458 CCDB: read std::array objects written by libstdc++ on libc++ builds (#16072)
- 10205ca5f0 Seed Geant4 through a function installed by the Geant4 configuration
- a781a584c4 Draw transport random numbers from a per-thread generator
- a8388782be Remove a trailing space in the FDD base CMake file
- f972016879 Complete the FairRoot provenance notes and guard unused geometry import
- 805a3d7c3a Move FairRoot simulation infrastructure into O2
- 383674dbaf Make the magnetic field evaluation reentrant
- ca6568dafc Keep stepping state in detector members instead of statics
- 9dfa79bd12 [ALICE3] VD: fixed digitization for the kIRIS4a and kIRISFullCyl geometries (#16063)
- ec214c87fe Spawn the o2-sim hit merger before the sim workers
- f296b3ca85 Flush queued hits before an o2-sim worker exits
- 155565ee2b Factor the primary request out of the sim worker kernel
- 09403ed1c2 [ALICE3] TRK/FT3 digitizer: noise rate set in hits/px/s instead of hits/px/ROF + uniform ToA for noise digits within ROF  (#16050)
- aeb75a70e1 ALICE3: TRK/FT3 digitizer response matrix on the heap, not the stack (#16033)
- d1cef57c82 [ALICE3] TRKFT3 digitizer: compensate for the shift of the reference BC when mCollisionTimeWrtROF < 0 (#16041)
- 451f837673 TRD: improve anchoring using CCDB objects (#15890)
- 59a8763b94 TrackCosmicsExt.Reader pushes TF ID info only if explicitly requested (#16035)

## Contributors
- Alberto Caliva
- Andrea Sofia Triolo
- Anton Alkin
- Cristian-Moscatelli
- David Rohr
- Ernst Hellbar
- Fabrizio
- Felix Schlepper
- Giulio Eulisse
- Igor Altsybeev
- Mario Ciacco
- Matthias Kleiner
- Nicolò Jacazio
- Podist Kurashvili
- Sandro Wenzel
- Yiping Wang
- abmodak
- alcaliva
- glegras
- jaimenorman
- ldellost
- shahoian
- shahor02
- spulawsk
- swenzel