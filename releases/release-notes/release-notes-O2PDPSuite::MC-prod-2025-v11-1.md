# Release Notes


These are release notes for O2PDPSuite::MC-prod-2025-v11-1 in comparison to the previous tag O2PDPSuite::MC-prod-2025-v9-1.

The release is based on the daily tag O2PDPSuite::daily-20250904-0000-1.


## Repository Updates
- **Control-OCCPlugin**: `v1.40.0` → `v1.42.0`
- **gpu-system**: `error` → `cuda_arch@86#89@_12.9.86-rocm_arch@gfx906#gfx908@_6.3.42134-opencl-miopen-migraphx-cudnn-tensorrt`
- **libjalienO2**: `0.1.4` → `0.1.5`
- **O2**: `daily-20250806-0000` → `daily-20250904-0000`
- **O2sim**: `async-20250806.1` → `v20250904`
- **O2Physics**: `daily-20250806-0000` → `daily-20250904-0000`
- **O2DPG**: `daily-20250806-0000` → `daily-20250904-0000`
- **FairMQ**: `v1.10.0` → `v1.9.2`
- **Clang**: `v18.1.8` → `v20.1.7`
- **AliGenO2**: `v20250806` → `v20250904`
- **QualityControl**: `v1.178.0` → `daily-20250904-0000`
- **JAliEn-ROOT**: `0.7.14` → `0.7.15`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 5f95c73d8f ITS: extend macros for pull distributions
- c09477ef95 ITS: GPU: added launch bounds for ITS kernels, not fully optimised for MI50 (#14644)
- 6749a807bb dpl-workflow.sh: modifying config/key defaults (ITS, MFT, MCH) for synchronous processing
- 17ae0d0a34 TOF matching should use the same FT0 int. tag as other global workflows
- dbd2625ae5 Add to trackdata in residuals TOF time difference and t0 error
- ef0de0f9e2 DPL: fix for printing O2_SIGNPOST_END without start interval (#14637)
- 057426487b DPL: change exit transition timeout default on FLPs to 40 s (#14638)
- 6fd377b7e1 DPL: initial metric to debug size of the histograms / objects being written
- 3db6ccad19 GPU Workflow: Pop next tf from completion policy queue only when actually running and add sanity checks
- ac05dee924 DPL: print error when exit transition timer expires
- aee6ae7236 Add includes
- a4c0d4fde6 Fix codechecker error
- bd41c6a7a2 Add missing includes
- e962d83a5a DPL Analysis: percolate DataOrigin so that we can use it for multiple files reading.
- 4d6b61e44d Fix DCS object sspec for MFT noise calibration
- c1576ad6ed DPL CDDB: hide private implementation of CCDBFetrcherHelper
- 8de09fccdf TPC: change default max-delay to 1 for o2-tpc-calibrator-dedx
- 577a7f008d ITS: skip processing entirely if no clusters/rofs in TF (#14629)
- cfa791d765 add best knowldge of collision time in tof matching info (#14615)
- 3673ef74be ITS: cell neighbour step use atomicMax (#14595)
- ad2098cbb0 GPU: Rename misleading variable
- 6d863f47f3 ITS: template Vertexer&Traits, IndexTableUtils (#14606)
- 8735573dd1 ALICE3-TRK: first version of working digitizer (#14619)
- dec2fe8515 A3: Add customization of detector MID/Magnet/Absorber radius (#14621)
- e1ff91130b Add HBFUtilsConfig to allow standalone aggregation of TPC residuals
- de1d18e300 start_tmux.sh: use o2-ccdb.internal for ccdb requests
- 7278b4e3e4 TPC: sort buffer of pressure in case it is not sorted
- 504267220e GPU QA: Proper fix for fetching timebins of MC data
- 88321c2a56 Minor fixes of debug printouts
- bd748b7784 Revert "Skip QED events in TPC QA"
- 2d53aee68c another fix
- 408665def3 Add missing includes
- d375e63478 DPL Analysis: centralised CCDB support in analysis (#14567)
- 012946b0d2 GPU CMake: Force using alidist GCC for host compilation of CUDA/HIP code
- c86ea4ed59 TPC Workflow: Don't write triggerwords if they are not created
- 4a450cf93e GPU HIP: Ignore comments in hipification template file check
- 1eb10b8c78 GPU Workflow: Do not do calib requests / updates in gpu-reconstruction-prepare
- 8e291428af GPU Workflow: Don't load ITS geometry when ITS is not used
- 38a4549cd5 Add residuals for external detectors unless --skip-ext-det-residuals is passed
- 3e1afe2b25 Method to translate TOF cluster to nominal sector frame
- d823a46382 Ctpdev: validity of orbitreset (#14612)
- b319a5ff82 ITS: GPU: disallow nROFsPerIterations (#14614)
- 7fccf1d245 [MFT] Fixing wrong call of functions in construction of NoiseMaps (#14609)
- ec334bc281 fix
- da20bb7471 fix
- 95f677e876 Adding sigma=0 cluster handling
- df10dd3ccd DPL Analysis: rework cursor logic keeping the `gsl::span` for VLAs (#14607)
- 06c1b84595 Enable ROOT file output in TPC chunked-digit merger (#14608)
- 9b8fb2326d TPC: Add scaling of VDrift with T/P (#14602)
- d84a22ca45 DPL: make addInputs support anything which provides base_specs (#14575)
- 396c2c4113 Add sapling to the .gitignore (#14605)
- be990f7544 DPL Analysis: fix for retrieving placeholder nodes in filters parsed from strings (#14603)
- 89bef8a2f5 DPL: don't print INVALID runNumber error when running with ALICE_O2_FST=1 (#14591)
- 6b6098b988 ITS: create artefacts labels only on demand  (#14594)
- 556556aeec ZDC: Add getter for hit secondary flag
- fb4df11e4a ITS: template Tracker, Cell and Road (#14597)
- d4e16e117b ITS: GPU: overlap memcpy with compute kernels (#14596)
- 86424f9b3c DPL Analysis: support configurables in string expressions (#14598)
- fa7d8f9274 Revert "Fix in TRD sector getter"
- cd8e5769a7 DPL Analysis: add an example of the string filter (#14570)
- 0364324707 ITS: GPU: prepare to lazy loading of data (#14585)
- 7262c36703 Fix in TRD sector getter
- 3912592e85 Align: Fix using local delta matrix
- 44cd710321 Align: print delta frame and level
- c35a2cdf7c Geo: optional print out alignment matrices
- 6c35d65ceb DPL: add more views on InputSpecs / OutputSpecs / DataProcessors (#14588)
- dce7e0eaca Skip QED events in TPC QA
- 65275d977a DPL Analysis: use offset cache for sorted grouping (#14571)
- fe9e22661f Revert "DPL: move to std::pmr where possible" This reverts commit 83467b3c67f9b51545b730c3fff5904419ea2806.
- 1463e6654c ITS: add common vertex definition and neighbours per road
- 999ac719cf Make sure extra tracks are randomized to avoid PHOS hole losses
- bbef7a7e93 Data Model: provide size when deallocating a Stack
- f9fa54ef16 DPL: add benchmark for stack creation
- a1c484d696 Ctpdev: reducing logs in run manager (#14574)
- e96552ab9d Update README so example code has std::
- a4605d0518 [MCH] improvements to the pedestal calibrator
- 26acde4f6c DPL: add C++20 ranges views to filter vectors of InputSpecs / OutputSpecs
- 3e0d913b6c Optionally store CTP lumi scaler (norm to 1s) in CTP digitizer output
- 5df80a763d Please consider the following formatting changes
- c1e321bfbf Remove probably redundant check. To be checked
- aec2bdb7ba Further simplification and compilable code
- 73793c8083 Fix after rebase
- cfbfb1374c backward compatibility for binning policy
- 919285695e use generic get() in row_helpers
- 24f1796bc7 DPL: improve error message
- a4e3e15879 Fix TimingInfo.timeslice vs DPH.startTime mismatch
- 80c4d143ee ITS: GPU: resolve added TODOs
- 7b7d8ff229 ITS: GPU: simplify stream synchronization
- 0825b22c6e ITS: GPU: use external allocator for temp storage
- 853e48dd38 ITS: GPU: put cell neighbour finding on different streams
- 2498a68ad1 ITS: GPU: put cell finding on different streams
- f2b0957773 ITS: GPU: put trackleting properly on different streams
- db916c26a1 DPL Analysis: add support for BinaryView columns
- 59033a58b4 Allow filters to be set in init(); Add ability to set a filter from string directly
- 81851e7f75 move unnecessary statics to .cxx
- 7129f45656 DPL Analysis: add parsing of expressions from strings
- 6209646b6e DPL Analysis: fix hash calculation for the string_views
- 00279c7108 DPL CCDB: move helper initialisation to a separate function
- 87ef0fc667 DPL: drop more boost_test usage
- 1f0e87470b DPL tests: drop unneeded includes
- 28345fbd29 Get rid of C++ extension warning
- 1f482616e0 DPL: add component for Arrow Acero Streaming Engine
- 83467b3c67 DPL: move to std::pmr where possible

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 18377a4e gen_topo_o2dpg.sh: force update of local tags in case an existing one was updated on the remote
- e7780bd7 workflow-multiplicities.sh: use two mch-data-decoder instances by default in synchronous pp and PbPb processing
- 532a4d86 MC picks up the FIT-related options used in o2-tof-matcher
- 407e642f Simplify multiplicity settings in async reco scripts
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
- 26daf209 [MCH] improvements to the pedestal calibrator
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

## Contributors
- ALICE Action Bot
- Andrea Sofia Triolo
- Anton Alkin
- Christian Sonnabend
- David Rohr
- Ernst Hellbar
- Fabio Catalano
- Felix Schlepper
- Francesco Noferini
- Gabriele Cimador
- Giulio Eulisse
- Jonghan Park
- Marco Giacalone
- Martin Eide
- Matthias Kleiner
- Maurice Coquet
- Michal Broz
- Nicolò Jacazio
- Roman Lietava
- Sandro Wenzel
- Sebastian Scheid
- aferrero2707
- chengtt0406
- ddobrigk
- ehellbar
- gluparel
- lucamicheletti93
- mcoquet642
- mytkom
- saganatt
- shahoian
- swenzel