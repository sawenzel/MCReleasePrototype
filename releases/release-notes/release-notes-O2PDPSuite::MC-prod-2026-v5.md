# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v5-1 in comparison to the previous tag O2PDPSuite/MC-prod-2026-v4-1.

The release is based on the daily tag O2PDPSuite/daily-20260325-0000-1.


## Repository Updates
- **Control-OCCPlugin**: `v1.48.2` → `v1.49.0`
- **libInfoLogger**: `v2.10.0` → `v2.10.1`
- **EPOS4HQ**: `v1.0hq-alice4` → `v1.0hq-alice5`
- **Monitoring**: `v3.19.10` → `v3.19.11`
- **ODC**: `0.87.0` → `v0.87.2`
- **EPOS4**: `v4.0.3-alice4` → `v4.0.3-alice5`
- **O2**: `daily-20260223-0000` → `daily-20260324-0551`
- **GBL**: `None` → `V03-01-04`
- **O2DPG**: `daily-20260223-0000` → `daily-20260325-0000`
- **QualityControl**: `v1.187.0` → `daily-20260325-0000`
- **O2sim**: `async-20260224.1` → `v20260325`
- **AliGenO2**: `v20260224` → `v20260325`
- **O2Physics**: `daily-20260223-0000` → `daily-20260325-0000`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 35fc90d933 [ALICE3] TRK: changed ML/OT pitch to 20 um (#15203)
- cfb2c3a655 [ALICE3] Adding error msg for TGeo features and QA macro for reco (#15183)
- 45753477d8 [ALICE 3] Properly set FT3 sensitive volumes; improve tiling (#15201)
- 43a3732a0f AODProducer: Option to specify and forward parent AOD file
- 70ca1a2fe8 [ALICE3] Updated ALICE 3 IRIS coldplate in O2 geometry (#15198)
- ae084c77dc Revert "DPL: Better detection for injected workflows (#15130)" (#15197)
- 20be6e73f6 DPL: Better detection for injected workflows (#15130)
- 5b0ada5f31 Add treatment of channel saturation to all scenarios
- 74f713a0c2 TRD: small fix for gain and VdExB calib
- bd173fab42 Use finer Z bins for mat LUT in 56.5 < R< 76 cm
- ce92d025a5 [ALICE3] TOF: Update stave tilt angles for iTOF and oTOF layers (#15172)
- 8e4cfe1c0a [ALICE3] Refactor TRK Hit class to rely on ITSMFT (#15173)
- 38ccad5c51 [ALICE3] TRK: add noise to the digitization process (#15167)
- f03975009c Fix overlap IRIS vacuum (#15185)
- decf5734f5 Workaround for non-null vertexes in event pools (#15169)
- a346105448 [ALICE 3] Fix cylindrical MLOT layout (#15168)
- b7a497ba51 fix field/material usage in the propagateToR... methods
- f9f6b09235 [ALICE3] oTOF: fix missing tilt shift for overlaps (#15159)
- 2f3b972596 Improve Vertex handling in MCEventHeader
- c1af82da4d [ALICE3] adding trapezoidal disk option for FT3; fixing overlaps in FT3 and TOF (#15158)
- fd78301558 [ALICE3] Update oTOF radius (#15140)
- e17ce87255 Methods for Barrel <-> Forward tracks conversion
- 2e80e74b87 [ALICE 3] TRKLayer refactoring (#15145)
- d886b772de Add getR method to TrackPar
- 202d71be3c [ALICE 3] Implementation of peacock layour for services (#15122)
- 90fbe62a83 [ALICE3] TRK: fix orientation of response function both for APTS and ALICE3 response + set reasonable threshold (#15135)
- 79f51afc16 ALICE3-TRK: fix y-axis orientation in the sensor local coordinate system, keeping the geometry unchanged (#15134)
- 49b0cb7c06 [ALICE3] Remove petal Z caps from vacuum vol (#15119)
- dbdc1df7db [ALICE3] Update FT3 geometry (#15126)
- f4c528d045 Fix missing header
- d890d412ba add treatment of TOF DRM Errors
- 1913a00141 [ALICE3] Add possibility to set the chip thickness (#15120)
- b2575f95b5 [ALICE 3] Fix VD full cyl building for ACTS (#15116)
- afcf287eb3 [ALICE3] Cluster finding of TRK (#15110)
- 3626eeac1a [ALICE3] TRK/Geometry: small bug fix (#15112)
- a1d999e775 [ALICE 3] Add IRIS option with inclined walls material   (#15098)
- 1ffca72c09 Fix type mismatch
- 8c4238634e Extra support for dumping ConfigurableParam to ini/json files
- 075c01aa42 Fix in the 3D field propagation final step
- 497abe0382 Integrate TRD extra data support in AOD production workflow (#15108)
- e59f5cb62c [ALICE3] TRK: fix extrusions and overlaps b/n staves (#15105)
- d19919cf22 [ALICE3] Change 'layoutOL' to 'layoutOT', update ALICE3/README with a config table (#15101)
- c590fd7f2f Change default ctf-dict of encoders to "none" (per-tf dictionary)
- 657d53aefc [ALICE3] update TOF geometry (#15096)
- 60cea723ef TRD: updates in vdrift and ExB calibration + possibility to use slope in chi2 matching (#14989)
- 96fafb9e89 Update MC header when using event pool generator
- 47fced53c0 Workaround for HepMC3 bug
- 03279d0607 Fix missing accumulate of covmatrix in fall-back case
- 9a75a460b6 o2sim: fix time aggregation in dpl-eventgen (#15091)

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 8d9bcc21 Honor detector inclusion list for FT0,FV0,EMC,CTP
- 4eee7fb6 PWGEM: Use default Pythia settings for OO HFee generator (#2305)
- 418fe243 Generator for HF enhanced PbPb MC for dielectron analysis (#2304)
- ddbdc548 update params (#2302)
- 1c02908b Updated gap parameter to 4 and removed Xi1820 (#2301)
- c32c968c Added configuration for exotic + Lambda1520 resonances with gap 2 (#2300)
- 3fc4a8e4 Remove Xi(1820) resonances from JSON configuration (#2299)
- 248b92e3 MC: Add reco-pass meta-data to AOD
- 47f914f7 Event-pools: Consistency fix for vertexing
- 5e972df2 Add generator for Sigma-Proton correlations (#2296)
- a82a0657 Update cfg and decay chain for exoticAll resonances (#2295)
- eb2b8919 Add Pythia8 trigger gap generator config for pO 9.6 TeV (#2292)
- 690deb19 [PWGLF] Added configuration for baryonic resonances (#2291)
- 12e659bb Force Xic0 and Omegac0 decay via external decayer (#2293)
- 7f272515 Add JJ config for gap 3 test production (#2289)
- 22f8bf42 PWGEM: Add HF2ee script for OO (#2290)
- 3b511ae9 Add impact parameter as centrality variable (#2287)
- da3640b7 Add collision system overwriting option (#2283)
- 1144e4f2 MID: add subSpec to QC inputs
- d8e02264 Add new files for synthetic flow study in OO (#2285)
- 72be7882 Force Lambdas to decay into protons and pions (#2284)
- 8a4a641d [PWGHF] Protect daughter index access in selectEvent to prevent segmentation faults (#2281)
- 92074d34 Added and updated ini for Lambda1520 (#2279)
- 14999396 [PWGEM] forced dalitz decay: fix missing width (#2280)
- f6d2de51 O2-6235 - change pt range  and bug fix (#2270)
- f102e9e7 tmp use special ALIENPY_JCENTRAL
- 8afcabae [PWGLF] reduce gap size (#2278)

## Contributors
- AizatDaribayeva
- Andrea Sofia Triolo
- Anton Alkin
- Chiara De Martin
- David Rohr
- Ernst Hellbar
- Fabio Colamaria
- Francesco Mazzaschi
- Francesco Noferini
- Gauthier Legras
- Giulio Eulisse
- Hirak Koley
- Kangkan Goswami
- Marco Giacalone
- Marco van Leeuwen
- Marian Ivanov
- Marvin Hemmer
- Maximiliano Puccio
- Nicolò Jacazio
- Pavel Larionov
- Raymond Ehlers
- Sandro Wenzel
- Sebastian Scheid
- Stefano Cannito
- abmodak
- alcaliva
- altsybee
- chengtt0406
- glegras
- laguiard
- rbailhac
- shahoian
- wiechula