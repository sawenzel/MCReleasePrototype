# Release Notes


These are release notes for O2PDPSuite::MC-prod-2026-v14 in comparison to the previous tag O2PDPSuite::MC-prod-2026-v13.

The release is based on the daily tag O2PDPSuite::daily-20261102-0000-1.


## Repository Updates
- **gl2ps**: `None` → `v1.4.2`
- **GEANT4**: `v11.2.0-alice2` → `v11.2.0-alice3`
- **QualityControl**: `v1.196.0` → `daily-20261102-0000`
- **O2sim**: `async-20260929.1` → `v20261102`
- **libgif**: `None` → `6.1.3`
- **GBL**: `V03-01-04` → `V04-00-06`
- **VecGeom**: `v2.1.1` → `v2.1.1-210-g66d734137`
- **O2Physics**: `daily-20260929-0000` → `daily-20261102-0000`
- **OpenBLAS**: `None` → `v0.3.27`
- **Control-OCCPlugin**: `v1.50.0` → `v1.51.0`
- **XRootD**: `v5.8.4` → `v5.9.8`
- **DittoMC**: `v1.0.1` → `v1.0.2`
- **Mille**: `None` → `V01-01-02`
- **GEANT4_VMC**: `v6-6-update2-p3` → `v6-6-update4-p4`
- **AliGenO2**: `v20260929` → `v20261102`
- **O2**: `daily-20260929-0000` → `daily-20261102-0000`
- **O2DPG**: `daily-20260929-0000` → `daily-20261102-0000`
- **lzma**: `v5.2.3` → `v5.8.4`
- **Millepede-II**: `None` → `V05-01-06`
- **AMPT**: `None` → `v1.26t9b-v2.26t9b-alice1`
- **vgm**: `v5-3` → `v5-5`
- **zstd**: `None` → `v1.5.7`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 1f4567dbcf Flip order of collision owner to prefer the signal + implemented review
- c756dc946b Fix loopers double counting when using embedding
- 9864f4126e Drop CCDBDownloader.h from the CCDB dictionary
- c4dda5aa07 ITS/MFT digi: account BC reassignment in time wrt BC (#16016)
- 63eca507c7 TrackCosmicExtended reader, attach to InputHelper and RecoContainer (#16017)
- 58f90b8691 Join the hybrid generator's TBB pool on shutdown (#16008)
- 6994ca6774 [ALICE3] TRKFT3: first implementation to store Time of Arrival into digits (#16012)
- f65ed96965 ITS/MFT digi: fix for late hits seen by the next ROF (#16011)
- 3b1de2716e [ALICE3] TF3: geometry update steered by the final definition of the chip size and module architecture (#15998)
- ab6e1c2326 [ALICE3] TRK update: New radii for the simplified-realistic OT paving (#16009)
- f98960a6e8 [ALICE3] TF3: double number of TDC pairs + add RO column masking (#15981)
- adf79c941e Integration of monopoles in O2 framework (#15602)
- 25a9d447fc TrackTools: shared TrackGeometry utilities for track acceptance and PID studies" (#15999)
- 06081e00c6 [ALICE3] TF3: fetch pixel maps inside digitizer workflow (#16002)
- feecef25b9 Extending track references to other detectors (#15997)
- 612f9ef00c Add contributesToAHit flag to MCTrack (#15996)
- 561ba48772 Make the partonic-decay test independent of the Pythia8 version
- 9bfef590fa Update charm and beauty lifetimes in the Pythia8 decay base config
- 390bc618bb Decay generator particles before transport in Generator::ReadEvent
- c993a260fb Add an event decayer that decays generator particles before transport
- 50ebfc10d3 Add a tool that writes the Geant4 particle table
- ff93406f5a [ALICE3] TRK: rInnRow column for staggered ML layers in the config file (#15992)
- cf6d37327b  AFIT-80 - Implementation of configurable parameters for FV0 reconstruction  (#15881)
- e02a56e6e4 TrackParametrization: use double math functions for TrackParD (#15990)
- ae9efba3c4 Geant base fluence studies for ALICE 3 (#15892)
- 8f4271a2c0 GPUCommonMath: double functions, 64-bit bit counts, atomic load/store
- fc413fc395 Cosmics cluster collector: store TPC occupancy per cosmic and per TF (#15987)
- 121fbacc52 BaseCluster: initialise errors to 0 by default (#15988)
- f1d73dfc80 Make O2DatabasePDG::Instance() thread-safe and remove duplicate PDG warnings
- c0b730cb25 Silence importing task line on hyperloop
- 22fed333c3 TRK: IRIS service aluminium from the MaterialManager (#15912)
- b7c157b863 GPU: let the constant-address-space constants be built on Metal
- 1c4118cb3b MathUtils: declare fastATan2's Pi where its lambdas can use it (#15949)
- afb8f0ff08 GRPGeomHelper optionally provides aligned geom + alignments (#15953)
- f642553202 MathUtils: make getMean()'s ternary unambiguous for an emulated double (#15947)
- b45ab114d8 MathUtils: let bringTo* deduce the type of the call they forward to (#15946)
- 63eafe3081 add adjustments for orbit shifts for some other MCs created with MC-prod-v12 (#15919)
- f2f04a298f Modernize Descriptor runtimeInit()
- a43ab3e1c1 Fix missing include
- d24f2c1e4b MatchCosmics: cosmics in collision data + raw-cluster writer with TOF (#15915)
- c584edc7a8 MathUtils: extend the OpenCL sincos workaround to Metal
- d3b4ba2598 [TF3] Add efficiency, time resolution and ToA maps from ccdb (#15883)
- eeaf095080 Implemented suggestions from code review
- 4cbcbed130 Implemented automatic parallelisation for external generator on HY
- 21d4ce4799 AFIT-81: Implementation of configurable parameters in FDD reco (#15882)
- 0a06b5d839 [ALICE3] TF3: group pixel columns into readout columns in digitizer (#15907)
- 024f05624a [ALICE3] TF3: fix conversion factor in absolute time computation (#15906)
- d4bd7efb95 simple EoS cards for disks (#15905)
- 44e82ed6cb [ALICE3] TRK: simple end-of-stave cards for ML barrel (#15902)
- 26127056d2 Let VecGeom turn large Boolean solids into MultiUnions
- 2fa3f3ebc9 Prevent broken tests related statements when BUILD_TESTING is OFF
- 37ae7ee590 SOR adjustment for some MC productions with ITS ramp-up offset (#15897)
- 59e68b2662 FT3 New Optimised OT Tiling & Clean up material writing (#15858)
- 42e4fdf2ef [ALICE3] IOTOF: Make timing response independent for different pixels (#15884)
- abc9b48b81 Support (staggered) per-layer cluster input in all ITS-dependent workflows (#15878)
- 150990b991 GPU: give Metal an IEEE-754 binary64 in software (#15866)
- 205248dc45 Cosmetic fix for FT3 GeometryTGeo to pass codechecker (#15885)
- 60e8cae85d o2-sim: VecGeom navigation mode for Geant4 (#15865)
- 48ac6437c9 Fix the vertical position of IB FPC resistors (#15876)
- 5f6b5b7342 Use std::threads instead of TBB tasks in the o2-sim hit merger
- 140d0e9c41 Resolve the TRD chamber by name when chamber assemblies have no volume id
- c69d567427 Fix CI test script
- ad7b5f715c Carry the ZDC box shapes in double
- 98825f70f8 Carry the PHOS geometry in double
- 77cd1ee779 Carry the TRD geometry in double
- bf20e96f3f Carry the CPV geometry in double
- e4337fb5dd Build the FT0 MCP stack and radiator wrap from running planes
- dd638210a5 Carry the TOF geometry in double and build the strip stack from running planes
- 509dfe404b Carry the rotation angles of Detector::Matrix in double
- 26d429cab8 Fix the MFT half-disk 3 support pockets to match the drawing
- f16249afb4 ORT CI tests (#15792)
- 4acbd0ae96 Extend RecoContainer to support ITS and MFT cluster access per layer (#15861)
- de2a8c4b3d Align Omega(2012) PDG code between database and transport

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 73f585d4 PYTHIA8 Box Generator: Minimum-Bias Events with Injected π⁰/η Decays (#2504)
- 46900edf Strangeness gap-triggered MC for OO collisions (#2516)
- 2034a92e getCCDBTimeMachineTimestamp.py: publish the NotAfter estimate to CCDB (#2509)
- 43060e0e grid_submit: wait until no subjob is active
- 0567fe5d Add --inputfile to pre-stage extra files via JDL InputFile
- 4aebb445 MC: store the MC truth in the TPC residuals whenever MC labels are on (#2503)
- ae342a14 Add Pb--Pb collisions at 5.02 TeV (#2513)
- da52329b Add ini files for gap-trigger scan (#2505)
- a60401c0 Support ITS(MFT) staggerd MC with ALIEN_JDL_ITS(MFT)_STAGGERED=1 (#2487)
- ca014390 First implementation of HGPythia (#2485)
- c91c9596 [PWGGAJE] Param Model: better multiplicity model (#2496)
- a769ab66 made the mass and pt cut configurable (#2500)
- 272c31d4 Fix indices in case of no mother in HF embedding generator (#2498)
- 392eb4de Add dittoMC oo, add injection (#2483)
- f98e628f [PWGLF] Add single-channel K1(1270) and Omega(2012) injection configs for ML signal samples (pp 13.6 and 5.36 TeV) (#2497)
- 8e2fcba1 Fix the ITS ramp-up shift rounding and the Pylint errors on master
- b5438367 Add Lstar gun generator, ini and config (#2495)
- 1fd2fb76 Various Upsilon states (#2494)
- 99f73585 Inclusive Jpsi decays and trigger (#2493)
- a12b1f7c Added phi-phi trigger code with additional selections to reduce total number of events (#2492)
- 1d96c11f [PWGLF] Added twoPhi trigger MC and renamed codes based on convention (#2490)
- d1a26b63 Ensure the ITS ramp-up offset to SOR orbit is multiple of orbitsPerTF
- cba47e1f [PWGDQ] adding generator to trigger all inclusive quarkonia in pp (#2466)
- 3415bc60 Add NeNe HF generator configurations (D2H ccbar+bbbar gap2 QCDCR) (#2476)
- b5ea46e9 Add a CCDB TimeMachine timestamp harvester for anchored MC
- 752c3e7d [MC/PWGEM] remove unnecessary files (#2484)
- aeebc784 Add pp at 5.36 TeV AMPT (#2482)
- 6b38f862 remove EvtGen ini file breaking the DQ update

## Contributors
- Andrea Sofia Triolo
- Anton Alkin
- Berkin Ulukutlu
- Bong-Hwi Lim
- Christian Sonnabend
- Daiki Sekihata
- David Rohr
- Fabrizio
- Farsh86
- Felix Schlepper
- Giorgio Alberto Lucia
- Giulio Eulisse
- Igor Altsybeev
- Justus Rudolph
- Lorenzo Bernardinis
- Marco Giacalone
- Marian Ivanov
- Mario Ciacco
- Matthias Kleiner
- NNicassio99
- Nicolò Jacazio
- Raphaelle Bailhache
- Rashi gupta
- Sandro Wenzel
- Tuba Gündem
- Wiktor Pierożak
- aimeric-landou
- ehellbar
- glegras
- hyungjun
- ldellost
- mario6829
- mbroz84
- rbailhac
- sawan
- shahoian
- shahor02
- spucillo