# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v2-1 in comparison to the previous tag O2PDPSuite/MC-prod-2026-v1-1.

The release is based on the daily tag O2PDPSuite/daily-20260201-0000-1.


## Repository Updates
- **O2sim**: `async-20260109.1` → `v20260201`
- **gpu-system**: `error` → `cuda_12.9.86_arch@80_real#86_real#89_real#120_real#75_virtual@_home_F52XG4RPNRXWGYLMF5RXKZDBBI000000-rocm_6.3.42134_arch@gfx906#gfx908@_home_F5XXA5BPOJXWG3IK-opencl-miopen-migraphx-cudnn-tensorrt`
- **Ppconsul**: `v0.2.3-alice2` → `v0.2.3-alice3`
- **Control-OCCPlugin**: `v1.46.1` → `v1.48.0`
- **xsimd**: `8.1.0` → `14.0.0`
- **EPOS4HQ**: `v1.0hq-alice3` → `v1.0hq-alice4`
- **GEANT3**: `v4-4` → `v4-5`
- **AEGIS**: `v1.5.8` → `v1.5.9`
- **ROOT**: `v6-36-04-alice7` → `v6-36-04-alice9`
- **ms_gsl**: `4.0.0` → `4.2.1`
- **O2**: `daily-20260106-0000` → `daily-20260201-0000`
- **EPOS4**: `v4.0.3-alice3` → `v4.0.3-alice4`
- **QualityControl**: `v1.185.0` → `daily-20260201-0000`
- **KFParticle**: `v1.1-7` → `v1.1-alice9`
- **O2DPG**: `daily-20260106-0000` → `daily-20260201-0000`
- **O2Physics**: `daily-20260106-0000` → `daily-20260201-0000`
- **AliGenO2**: `v20260109` → `v20260201`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`, `.*`

- 02a0aebb57 DPL: improve type_to_task_name function (#15006)
- dd70bca748 ALICE 3: add fully cylindrical IRIS, correct Si thickness, add v3 building (#14979)
- 515ba3a699 Revert "DPL Analysis: cleanup AnalysisTask.h and ASoA.h (#14996)" (#15005)
- fd54f4a120 DPL: fix device signpost segfaults for o2-dpl-raw-proxy (#15003)
- a979c459f8 dpl-workflow.sh: enable ALPIDE_ERR_DUMPS by default in online physics runs
- 63e5c6136f DPL Analysis: cleanup AnalysisTask.h and ASoA.h (#14996)
- 0bb564d94f ITS: GPU: fix wrong argument parsing for outward refit
- aa3ef3751f ITS: GPU: more memory clearing in processNeighbours
- e4a4f1a002 ITS: GPU: add skipping of parts where nothing was found
- 5f4f95a479 GPU: add constexpr version of qStr2Tag
- b62d3d6084 ITS: GPU: create compile time stack tags
- c3f85c1d7c ITS: fix correctForMaterial arg for actual layer
- 8eebfb5e61 ITS: GPU: reduce TrackITS allocation
- 2d37a89a85 ITS: enlarge StartLayerMask for TRK
- f86363afb6 ITS: instaniate TRK classes
- 3669ad3516 GPU: Parallelize TPC pad filter over pad rows instead of cachelines.
- 52b0e23ac5 DPL: disable early forwarding for output proxies
- 0df45c4292 Implementation of TPC loopers in O2
- cb66b5edfc Add extra info with charge and timing and occupancy to unbinned residuals (#14969)
- 0cf7ec2217 GPU CMake: Improve architecture auto-detection
- efad2290e1 ITSMFT: fix number of rofs per TF
- a09a567d02 DPL Analysis: Use dangling edges context in more places (#14988)
- c6b7d8bf9c ALICE3-TRK: added possibility to use a local response file during digitization
- 7cc3f1c550 DPL: move snapshot code to use concepts
- 1fba29618f DPL Analysis: modernize and cleanup some code (#14975)
- b33261326d Implement AO2D file checks for full_system_test
- b18b96ab60 Ctpdev: task for populating BK with ctp config/scalers (#14993)
- 5b572ed12a ITSMFT: staggered digitization
- 5376bb861a PVertexer::refitVertexFull for refitting with different geom.
- 538f355832 DPL: do not do the new early forwarding for some of the data
- 078eb5d8b2 Revert "DPL Analysis: Use dangling edges context in more places (#14953)"
- 397e0194d0 [O2-6625] Fix the missing filename in the CCDb
- 587eb9487a TRD: add missing OutputSpec in trd-pulseheight device
- be1d553177 Store missing GlobalTrackID in the CheckResid output
- 8562189e36 DPL: make new early forward optional
- a498938416 DPL: avoid needless copy of messages when cleaning up early forwarding
- 96a6a753d2 GPU QA: Improvements for some plots
- 9634a2ee3f GPU: Don't override --recoSteps flags in standalone.
- ed8276cbdd DPL: earlier forwarding
- a6471db324 DPL: more preparation for earlier forwarding
- c990996954 DPL Analysis: Use dangling edges context in more places (#14953)
- dd66913843 dpl-workflow.sh: increase pvertexer.timeMarginVertexTime to 5 for sync raw pp
- fbe64c88c1 Optionally refit ITS outward seeding with inward refit result
- 9ca7f3a721 GPU: Fix crash with --noEvents option, and improve some debug messages
- 36b13b4dde GPU: Fix direct memory allocation debug message
- 705c73cda6 GPU CUDA: Do not link against nvrtc library, which is not used
- c5f00f245e A3: Fix geometry building of FT3 (#14968)
- db7170bd9c ALICE3-TRK: fix the length of the layers for the kCylinder layout for ML and OT (#14967)
- 7cd4b7f29f DPL: keep code checker happy (#14966)
- 8ead4583ab TPC_MC_anchoring_simple: Added per region relative gas gain to simulate the change in the voltage settings of GEMs
- c5c328283c ALICE3-TRK: partial fix to issue #14959 (#14965)
- 0a8627db85 Switch option from external to hybrid (#14951)
- b5dfe5011a start_tmux.sh: create ED directory to avoid filesystem errors during o2-eve-export-workflow (#14961)
- 7aa1bbc3f9 DPL Analysis: Rework table input record extraction (#14944)
- 7245d49faf AFIT-1 FV0 digitzer dead channel map (#14908)
- 34d96168b9 DPL Analysis: fix for slice index builder resetting its caches in a wrong order
- 8c0bd3ce63 Switch off default embedding
- 5cce90740c Fix embedding test
- eb3d49c31d DPL Analysis: do not override error-handler reader for MC injected workflows
- 056504e47c Fix ITS/MFT clusterization for some complex shapes, O2-6424.
- 1afdd6c490 DPL: fix how many forwarded parts are needed
- 7b11923549 DPL: add callback when inserting in the slot
- 36176ca5c7 DPL: add test for routing messages
- 494f76c08b Fix code checker report
- b20c426d6a use better criterion to add arrow support service
- 1dc98c8718 TPC space-charge: Improve GEM frame charging-up distortions
- ddcdd1f32c reduce verbosity of ITS/MFT digitizer
- c21d7d7a7e add TOF channel in TPC timeseries (#14945)
- 67c2a31833 TPC: move PadFlags and related classes to TPCBaseRecSim
- 696cf650cc DPL: fix a few warnings
- bf75199a53 [EMCAL] implementation of number of local maxima variable
- 96e2f45f8c DPL: avoid MessageSet abstractions when forwarding
- 4c3ba3d451 DPL: fix warnings
- f088a35661 ITS: remove old ClustererTask
- c426fe5cb1 ITS: remove CookedTracker
- 0e958cabd2 DPL: fix routing issues in forwarding
- 9bbf6ecca2 DPL: more refactoring of the forwarding code
- 91a991f6ba DPL: allow to disable oldest possible timeframe propagation with a label
- 027cad2dea Propagate dangling edges context to init context and delay algo loading
- a5f88b7946 AnalysisContext -> DanglingEdgesContext
- aab079f2ba DataModel: improve DataHeader formatter

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 9927be49 Configs for Lc resonance prod. (#2246)
- eb80febb Add Strangeness (cascades) generator pythia ropes + jet gap 4 (#2251)
- dac9ee92 Example script to run workflow with ML clusterizer
- f8a96ded Refactor of TPC clusterization configuration
- 44e1c0dd add EPOS4 with URQMD switched off (#2249)
- 8b31af4f Add TPC Loopers collision system confKey
- 4120f2d4 anchorMC: Fix bug in restoring custom env variable
- dcfc5aba Add missing default Activity fields for HMP simulation QC (#2242)
- 8b165c56 MC/PWGEM: add cfg and init for vm2ll in pp/PbPb (#2244)
- 3cd6b381 Less demanding version of GeneratorPythia8POWHEG_jetjet_13600.ini (#2241)
- e6b7007d Add replacement config to generator_pythia8 to replace D*/Sigmac+ by Xic0/Omegac0 (#2186)
- db9759bf Change requireIsGoodZvtxFT0VsPV value to false for K0s QC
- 57aa0467 rawTF2raw: fix typo in rawTF2raw converter script
- fd047509 Change useIsGoodZvtxFT0vsPV to false (#2230)
- 7f111934 Adding generators for non-prompt charmonia in light ions (#2235)
- ccc4ad69 Add generator for LambdaB to deuteron (#2237)
- 5dbd96c2 [PWGLF] Add generator for strangeness in jets (#2234)
- b664d2db Update to use the gap triggered production as default (#2233)
- d1db8ef8 Included Hybrid generators testing + example (#2223)

## Contributors
- Andrea Sofia Triolo
- Anton Alkin
- Antonio Palasciano
- Barthelemy
- Bong-Hwi Lim
- Daiki Sekihata
- David Rohr
- Ernst Hellbar
- Felix Schlepper
- Felix Weiglhofer
- Florian Jonas
- Francesca Ercolessi
- Francesco Noferini
- Giulio Eulisse
- Marco Giacalone
- Matthias Kleiner
- Nicolò Jacazio
- Pavel Larionov
- Piotr Konopka
- Ravindra Singh
- Roman Lietava
- RuiqiYin
- Sandro Wenzel
- Wiktor Pierożak
- alcaliva
- atriolo
- ehellbar
- mcoquet642
- shahoian
- shahor02
- tubagundem