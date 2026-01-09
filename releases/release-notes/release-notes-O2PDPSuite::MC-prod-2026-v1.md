# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v1-1 in comparison to the previous tag O2PDPSuite/MC-prod-2025-v16-1.

The release is based on the daily tag O2PDPSuite/daily-20260106-0000-1.


## Repository Updates
- **gpu-system**: `error` → `cuda_arch@80-real#86-real#89-real#120-real#75-virtual@_12.9.86-rocm_arch@gfx906#gfx908@_6.3.42134-opencl-miopen-migraphx-cudnn-tensorrt`
- **O2DPG**: `daily-20251217-0000` → `daily-20260106-0000`
- **ROOT**: `v6-36-04-alice3` → `v6-36-04-alice7`
- **QualityControl**: `v1.185.0` → `daily-20260106-0000`
- **pythia6**: `428-alice2` → `428-alice4`
- **O2Physics**: `daily-20251217-0000` → `daily-20260106-0000`
- **AliGenO2**: `v20251217` → `v20260106`
- **VMC**: `v2-0` → `v2-1`
- **O2**: `daily-20251217-0000` → `daily-20260106-0000`
- **O2sim**: `async-20251217.1` → `v20260106`
- **lhapdf-pdfsets**: `v2025` → `v2026`
- **HepMC3**: `3.3.0` → `3.3.1`

## MC Relevant Changes

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 6d85da19 Disable TPC timeseries when required detectors are missing
- 3bef31fe Implemented ITS ramp-up shift in start-of-run
- d71859aa Update GeneratorLFDeuteronOOGap.ini
- 9c5a142c Add deuteron injected ini files for OO
- 7161e7ec Reduce number of events for tests (#2216)
- 28f05998 Fix Pythia8 CI testing
- 2e31d1b2 add 2tag-test case (recently failing)
- 62702470 [PWGHG] Adjusted centrality range in HF config file to keep dummy values (#2220)
- d25f9339 reduce number of events for tests
- d48f01f5 [PWGHF] add configuration for D2H ccbar and bbbar gap2 for pO collisions
- 31cbf2f3 Add DPL-eventgen testing
- 0acdaf14 Treat "all" in detector list cleaning
- 35d151b2 Allow to run central barrel only

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- ea23c378e4 MathUtils: move BetheBlochAleph to a common header
- 51f8cefb58 Moved configFile check + expand env vars
- 73c5a52720 DCA Fitter GPU: Disable failing test, which was not active before and seems broken
- 4804b1c165 Common: EnumFlags add set

## Contributors
- ALICE Action Bot
- Arvind Khuntia
- David Rohr
- Fabrizio
- Felix Schlepper
- Florian Jonas
- Giulio Eulisse
- Marco Giacalone
- Ravindra Singh
- Sandro Wenzel
- arvindkhuntia