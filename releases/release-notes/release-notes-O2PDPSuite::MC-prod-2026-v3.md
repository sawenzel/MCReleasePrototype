# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v3-1 in comparison to the previous tag O2PDPSuite/MC-prod-2026-v2-1.

The release is based on the daily tag O2PDPSuite/daily-20260205-0000-1.


## Repository Updates
- **QualityControl**: `v1.186.0` → `daily-20260205-0000`
- **O2sim**: `async-20260203.1` → `v20260205`
- **O2**: `daily-20260201-0000` → `daily-20260205-0000`
- **O2Physics**: `daily-20260201-0000` → `daily-20260205-0000`
- **O2DPG**: `daily-20260201-0000` → `daily-20260205-0000`
- **AliGenO2**: `v20260203` → `v20260205`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- ff39f95db1 Fix and improve TPC Loopers implementation
- 597fc9ee86 Leave single implementation of TRD RecoParam, init from GPUSettingsRecTRD

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 4a395337 [PWGLF] Add Ropes and EPOS config files for pp 5.36 TeV (#2259)
- 9237d4be make anchor testing more configurable
- d2c93118 new ini for gap triggerd strangeness MC for pp ref energy (#2245)

## Contributors
- Francesca Ercolessi
- Lucia Anna Tarasovicova
- Marco Giacalone
- Sandro Wenzel
- shahoian