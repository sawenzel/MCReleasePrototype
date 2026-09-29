# Release Notes


These are release notes for O2PDPSuite::MC-prod-2026-v13 in comparison to the previous tag O2PDPSuite::MC-prod-2026-v12.

The release is based on the daily tag O2PDPSuite::daily-20260929-0000-1.


## Repository Updates
- **O2sim**: `async-20260917.1` → `v20260929`
- **AliGenO2**: `v20260917` → `v20260929`
- **QualityControl**: `v1.195.6` → `daily-20260929-0000`
- **O2**: `daily-20260917-0000` → `daily-20260929-0000`
- **DittoMC**: `None` → `v1.0.1`
- **O2DPG**: `90c0a3d259b814aeb6f687bcfdea6dec4694e94f` → `daily-20260929-0000`
- **O2Physics**: `daily-20260917-0000` → `daily-20260929-0000`
- **pythia**: `v8315-alice1` → `pythia8318`
- **VecGeom**: `v1.2.6` → `v2.1.1`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- fced5072ac Add missing resonances PDG codes in the contraints files (#15820)
- 8329295aef Count the charge of the buffered TPC hit in the electron counter
- 3baedd0940 Reset the TPC hit grouping at the end of each event
- 3c018e5037 Fix memory deletion for bufferptr in SerializedInfo/RootSerializableKeyValueStore
- eb06ef46ea make sensor thickness configurable in geometry definition (#15848)
- 3528ed2638 Fix Hybrid example including new HepMC parameters
- 4215a64209 Fix couple of invalid debug print arguments
- 900b5e46fd Keep the hit-merger hit buffers as a detector member
- d2923551b3 Create the hit-merger detector instances from a table
- 2912c670d9 Move the o2-sim device implementations into source files
- bbd63ce1b9 Flush the output files of the o2-sim hit merger concurrently
- 8876f2c4b5 Move instead of copy when merging hits in the o2-sim hit merger
- 772a0cfa0c Adopt decoded hit containers in the o2-sim hit merger
- 33345fb577 Send the hit transport mode with the hits in o2-sim
- 8751577617 Remove the o2-sim shared-memory segment when its last user detaches
- c5c3d2229d Make the shared-memory hit-buffer busy flag atomic
- 47c5a640d4 Initialise the output pointers of the o2-sim hit merger
- ba873ef503 Release per-event buffers in the o2-sim hit merger
- 4b704ead38 Fix the event-flush loop of the o2-sim hit merger
- 4957f17508 Skip malformed info requests in the primary server
- adb24c4bb6 Do not cache external-kinematics generators in the primary server
- 4d42b5b830 Fix the merger exit-status check in o2-sim
- 341b3156c0 Terminate the LinkDef rules that rootcling rejected
- b5768c91c8 Use ClassDefOverride in the derived interaction samplers
- dccd0393db GPU: three additional Metal adaptations
- 4f9072579a Give the MFT support volume a name of its own
- 9a93b68645 GPU: route noexcept through GPUnoexcept() for Metal
- d48231502a Write tracked V0s, cascades and 3-bodies in collision order (#15838)
- cd59f17980 BoxGenerator: enable sampling of pT and rapidity instead of p and eta
- 186a4afc19 [ALICE 3] FT3 digitization: Change axis convention in disc sensors (#15827)
- b1e73be1fa Use the LHC orbit duration for CTP scaler rates
- b7270bb55e Fix out-of-range BC slice for ambiguous tracks past the last BC
- af76bd1393 [ALICE 3] FT3 fix magnetic field silently disabled when FT3 is active (#15828)
- f3ebce3bf2 MathUtils: make SMatrixGPU compile as MSL
- 603b7ed818 TRD: using slope to correct y position and reject more fakes (#15799)
- f3be1eab9b [TF3] Implement cluster finder for multiple digits in same chip (#15748)
- 5da2428cca TRD: more program-scope variables fixes
- 0f3fb8b659 Common: put the namespace-scope constants in the constant address space (#15825)
- 86cd1896a8 More VecGeom v2.x compatibility (#15821)
- 1b917c4776 GPUTracking: place global constexpr constants in the "constant" address space (#15818)
- 5b009ee93b fix int/uint comparison (#15819)
- 98dd00ec33 Apply NIEL damage weights to all hadrons and electrons
- 1d0f240d99 Merge Geant4 scoring meshes from parallel o2-sim workers
- cefb94d6f3 Clamp NIEL damage weights to the tabulated energy range
- 5ca7d3f26c [EMCAL-688] Update ClusterFactory and fix bug in `buildCluster` (#15788)
- 28b475407c [TF3] Improve digit efficiency in stepping (#15804)
- 1e21f73cb0 TPC: place shared constants in the Metal constant address space (#15802)
- 0860f6fd3a Give box-gun primaries weight 1 in o2-sim

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- e956baec [PWGLF] Appended the injected event in MB event correctly (#2481)
- 2cc0f9a9 Cleanup test macros (#2480)
- be360c34 Add dittoMC configurations for pbpb at 5.36 TeV (#2478)
- ea6d40d3 Add DittoMC (#2464)
- a7bf47cd Update generator_pythia8_NonPromptSignals_gaptriggered_dq.C (#2475)
- 768e660f Replace simple string search with regular expression
- 4b2ac040 Flat pt for phi meson (#2473)
- 813d35b8 Update decay table for b-hadron to open charm MC (#2472)
- 514cd666 [PWGLF] MC for Uncorrelated+Correlated phi-phi pairs for phi-phi resonance study (#2469)
- 9b87eb1e Change the number of embedded signal in the Pb--Pb collisions (#2467)
- d07c87f8 [PWGLF] Revise injected-particle pT and rapidity ranges and add .ini file for rare-resonance MC in pp at 5.36 TeV (#2471)
- 8d5dc8be Run the O2DPG simulation tests against a CVMFS release
- 8af99c34 Fix typo in Tau decay tables
- 046c4e24 Keep the ZEM geometry instead of skipping the whole ZDC module

## Contributors
- Berkin Ulukutlu
- Bong-Hwi Lim
- David Rohr
- Fabrizio
- Felix Schlepper
- Francesco Mazzaschi
- Giulio Eulisse
- Ida Storehaug
- Marcello Di Costanzo
- Marco Giacalone
- Marco van Leeuwen
- Mario Ciacco
- Marvin Hemmer
- Michal Broz
- Nicolò Jacazio
- Sandro Wenzel
- glegras
- mj525
- rbailhac
- sawan
- shahor02