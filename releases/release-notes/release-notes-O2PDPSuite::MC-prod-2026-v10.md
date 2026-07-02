# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v10-1 in comparison to the previous tag O2PDPSuite/MC-prod-2026-v9-1.

The release is based on the daily tag O2PDPSuite/daily-20260629-0000-1.


## Repository Updates
- **FairMQ**: `v1.10.1` → `v1.11.0`
- **O2DPG**: `daily-20260612-0000` → `daily-20260629-0000`
- **QualityControl**: `v1.192.0` → `daily-20260629-0000`
- **KFParticle**: `v1.1-alice9` → `v1.1-alice10`
- **JAliEn-ROOT**: `0.7.17` → `0.7.21`
- **O2Physics**: `daily-20260612-0000` → `daily-20260629-0000`
- **ROOT**: `v6-36-10-alice1` → `v6-36-10-alice2`
- **O2sim**: `async-20260615.1` → `v20260629`
- **O2**: `daily-20260612-0000` → `daily-20260629-0000`
- **AliGenO2**: `v20260615` → `v20260629`

## MC Relevant Changes

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 249fae8d MC/PWGEM: update DY simulation (#2391)
- f26986ec DPG: update FIT parameters for 2023 and 2024 data
- 0a6a1bfb DPG: update FIT parameters for 2023 and 2024 data
- 9d7321b4 Fix seed initialisation of c-deuteron gun and status codes (#2389)
- b4a073bd Allow arbitrary prodsplits in grid_submit
- c36702ac Add missing B_s -> JPsi decays (#2385)
- 732c81fe Adding chiC (#2384)
- 07a16ff0 [PWGHF] Add possibility to use EVTGEN in HF generator + config for B2Jpsi (#2378)

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 77c2fc33ea TPC: avoid having a direct dependency on RDataFrame (#15551)
- 522d17f1b5 TF3: fix digit time (#15556)
- dfe0aaa94d [Algorithm] Remove unused parser and TableView utilities
- ad6a130cb0 FT0 crosstalk in digitizer (#15466)
- 4d3c046386 Extend configurable params for std-container types (#15525)
- 5d0a12e208 [ALICE3] TF3: add first version of QA macro to check digitization (#15543)
- 54d639b1ed TPC: Add sector edge fluctuation correction infrastructure (#15532)
- 9429beb4a9 Possibility to globally bias MeanVertex objects via env.var
- 644949a529 ALICE3: prepare IOTOF geometry for including TOF in tracking (#15521)
- 79fec1994a [ALICE3] TF3: fix labels filling in digitization (#15537)
- d687bf5250 Enable Alien hybrid config file fetching
- e8acf47326 fix warning final-dtor-non-final-class (#15490)
- cf8c9dccd4 Add missing parameter instantiation
- b6cbe1406f Fix missing L* resonances
- 4d229fbeae Add c-deuteron PDG code in physics constants

## Contributors
- Daiki Sekihata
- Fabrizio
- Fabrizio Grosa
- Felix Schlepper
- Giulio Eulisse
- Marco Giacalone
- Mario Ciacco
- Matthias Kleiner
- Maximiliano Puccio
- Sandro Wenzel
- Szymon Puławski
- shahoian
- shreyasiacharya
- spulawsk