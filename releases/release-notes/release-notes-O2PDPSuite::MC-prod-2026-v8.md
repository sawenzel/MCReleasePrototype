# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v8-1 in comparison to the previous tag O2PDPSuite/MC-prod-2026-v7-1.

The release is based on the daily tag O2PDPSuite/daily-20260522-0000-1.


## Repository Updates
- **QualityControl**: `v1.191.0` → `daily-20260522-0000`
- **AliGenO2**: `v20260508` → `v20260522`
- **O2**: `daily-20260506-0000` → `daily-20260522-0000`
- **ROOT**: `v6-36-04-alice9` → `v6-36-10-alice1`
- **O2Physics**: `daily-20260506-0000` → `daily-20260522-0000`
- **O2DPG**: `daily-20260506-0000` → `daily-20260522-0000`
- **O2sim**: `async-20260508.1` → `v20260522`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- c7d5958f58 ITS: add selections on tracks sharing clusters (#15406)
- aa96c1a9fd IOTOF: align geometry to specs (#15414)
- f8f5d1eb6c Add token for the test CCDB instance
- aafbebfdbc [ALICE 3] TRK: Fix sensitive volumes definition for FT3  (#15397)
- b3e2e7ab0e [ALICE3] TRK: adjustments for z and r of services, split OT barrel into two halves (#15395)
- 3ddeb15d80 [ALICE3] TRK: update of TRK and FT3 services, to better match with Corrado's scheme (#15392)
- a204d4181b TPC_CMV: Improving the CMV workflows (#15360)
- 9ad6dd4b29 Raw TF dump workflow (#15374)
- 560821941e [ALICE 3] TRK: Changed chip size and module number for TRK barrel + updated TRK documentation + included low services around beam pipe (#15382)
- a4e6201f85 ITSMFT: remove redirect header
- 285dbb7fbe move OT barrel service disks closer to stave 'edges' (to 135 cm), change rMax from 68 to 80 cm (#15384)
- 0a6ade3635 Add new particles to O2DatabasePDG
- a0f94b4784 [ALICE3] IOTOF: Digitization for the TOF3  (#15372)
- 4ba3efa7d2 ITS: add hash function over clidx
- 70bfe0eca3 AODProducer option to store all mft covariances (#15338)

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- e87efa6d AODBcRewriter: possibility to treat AliEn files directly
- b11cd3de AODBcRewriter: fix paste-join children after row reorder/dedup
- e82b065a [PWGLF] add new config files for Deuteron production in pythia at pp 5.36 TeV (#2357)
- 0ae184a3 Expand o2-analysis-qa-event-track.json configuration (#2321)
- 8867bb9c PWGHF:  beauty production with natural decay at forward rapidity (#2353)
- c33b9e8d MC/PWGEM: fix typo in #2351 (#2352)
- 851f56f0 MC/PWGEM: update configs in pp at 5.36 TeV (#2351)

## Contributors
- Daiki Sekihata
- Fabrizio Chinu
- Felix Schlepper
- Francesca Ercolessi
- Giorgio Alberto Lucia
- Martin Eide
- Nicole Bastid
- Nicolò Jacazio
- SCHOTTER Romain
- Sandro Wenzel
- Stefano Cannito
- Tuba Gündem
- altsybee
- mcoquet642
- shahor02