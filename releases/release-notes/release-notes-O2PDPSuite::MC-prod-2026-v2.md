# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v2-1 in comparison to the previous tag O2PDPSuite/MC-prod-2026-v1-1.

The release is based on the daily tag O2PDPSuite/daily-20260201-0000-1.


## Repository Updates
- **KFParticle**: `v1.1-7` → `v1.1-alice9`
- **O2**: `daily-20260106-0000` → `daily-20260201-0000`
- **EPOS4HQ**: `v1.0hq-alice3` → `v1.0hq-alice4`
- **xsimd**: `8.1.0` → `14.0.0`
- **AEGIS**: `v1.5.8` → `v1.5.9`
- **O2Physics**: `daily-20260106-0000` → `daily-20260201-0000`
- **ms_gsl**: `4.0.0` → `4.2.1`
- **O2DPG**: `daily-20260106-0000` → `daily-20260201-0000`
- **GEANT3**: `v4-4` → `v4-5`
- **gpu-system**: `error` → `cuda_12.9.86_arch@80_real#86_real#89_real#120_real#75_virtual@_home_F52XG4RPNRXWGYLMF5RXKZDBBI000000-rocm_6.3.42134_arch@gfx906#gfx908@_home_F5XXA5BPOJXWG3IK-opencl-miopen-migraphx-cudnn-tensorrt`
- **EPOS4**: `v4.0.3-alice3` → `v4.0.3-alice4`
- **Control-OCCPlugin**: `v1.46.1` → `v1.48.0`
- **ROOT**: `v6-36-04-alice7` → `v6-36-04-alice9`
- **AliGenO2**: `v20260109` → `v20260201`
- **O2sim**: `async-20260109.1` → `v20260201`
- **QualityControl**: `v1.185.0` → `daily-20260201-0000`
- **Ppconsul**: `v0.2.3-alice2` → `v0.2.3-alice3`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- dd70bca748 ALICE 3: add fully cylindrical IRIS, correct Si thickness, add v3 building (#14979)
- 0df45c4292 Implementation of TPC loopers in O2
- c6b7d8bf9c ALICE3-TRK: added possibility to use a local response file during digitization
- 5b572ed12a ITSMFT: staggered digitization
- 397e0194d0 [O2-6625] Fix the missing filename in the CCDb
- c5f00f245e A3: Fix geometry building of FT3 (#14968)
- db7170bd9c ALICE3-TRK: fix the length of the layers for the kCylinder layout for ML and OT (#14967)
- 8ead4583ab TPC_MC_anchoring_simple: Added per region relative gas gain to simulate the change in the voltage settings of GEMs
- c5c328283c ALICE3-TRK: partial fix to issue #14959 (#14965)
- 0a8627db85 Switch option from external to hybrid (#14951)
- 7245d49faf AFIT-1 FV0 digitzer dead channel map (#14908)
- ddcdd1f32c reduce verbosity of ITS/MFT digitizer
- 67c2a31833 TPC: move PadFlags and related classes to TPCBaseRecSim
- bf75199a53 [EMCAL] implementation of number of local maxima variable
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
- Antonio Palasciano
- Barthelemy
- Bong-Hwi Lim
- Daiki Sekihata
- Ernst Hellbar
- Felix Schlepper
- Florian Jonas
- Francesca Ercolessi
- Giulio Eulisse
- Marco Giacalone
- Nicolò Jacazio
- Pavel Larionov
- Piotr Konopka
- Ravindra Singh
- RuiqiYin
- Sandro Wenzel
- Wiktor Pierożak
- alcaliva
- atriolo
- mcoquet642
- shahoian
- tubagundem