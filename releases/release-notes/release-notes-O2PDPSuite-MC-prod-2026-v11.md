# Release Notes


These are release notes for O2PDPSuite::MC-prod-2026-v11 in comparison to the previous tag O2PDPSuite::MC-prod-2026-v10.

The release is based on the daily tag O2PDPSuite::daily-20260729-0000-1.


## Repository Updates
- **O2Physics**: `daily-20260629-0000` → `daily-20260729-0000`
- **O2**: `daily-20260629-0000` → `daily-20260729-0000`
- **Monitoring**: `v3.19.14` → `v3.19.16`
- **QualityControl**: `v1.193.0` → `daily-20260729-0000`
- **O2DPG**: `daily-20260629-0000` → `daily-20260729-0000`
- **AliGenO2**: `v20260629` → `v20260729`
- **O2sim**: `async-20260629.1` → `v20260729`
- **STARlight**: `20251025` → `20260511`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 792c0d0942 Multi-threaded material budget LUT creation
- c226ccb014 Use fastAtan2 with protection against radial tracks (#15642)
- b6647b4fb9 Fix in Propagator::initFieldFromGRP (#15637)
- 4e94192628 [ALICE3] TF3: approaching TF3 ASIC: use 8-chip modules + update chip segmentation (#15639)
- 980546b33b move OT barrel service 'disk' z from 132 to 142 cm to have space for readout cards (#15635)
- 9a3938a24d remove overlaps in OTOF staves (#15633)
- 51d8507439 Add geometrical TPC protection against misfired loopers (#15621)
- 1709369443 Fix includes for ROOT 6.40 (missing in cxx, and can no longer forward-declare)
- e6152d702a Created group labels for randomisation + added protection on non-integer fractions
- 9caae96a37 Fix wrong parameters injected in SimFieldUtils
- 91307a4b46 Latest v3b.1 RICH geometry with quadrants, modules and shielding (#15608)
- fce05cf673 [ALICE3] added segmentation to the particle propagation in TOF3 (#15591)
- 656fd89603 Properly discard Alice3 TRK hits preceding RO start (#15606)
- 775528b421 Fix x-axis related error treatments (#15610)
- 9e7582fc04 Improve TrackParCov covmat conversion to&from Lab Covariance (#15612)
- 79391f410b Propagate PV MCLabel to extended PV in the trackingStudy
- 6ac7a7a863 Properly discard ITS hits preceding readout start (#15601)
- 7d9a516f25 Fix for Loopers identified as primaries
- 56f11931cb TPC addHits: remove short type limitation
- 19d24d5b06 Make maximum number of electrons per step a configurable
- 6645741120 Align: add option to print local delta of params
- 433890f02b TPC VDrift: hold refVdrift constant
- 28d11a8dcc Possibility to bias magnetic field origin via env.var.
- be551457fb Expand path of evtpools
- bd1861201c [NN CF]: Updates and bug-fixes (#15571)
- 95fb936b93 GPU: Process dEdx with full qTot range (#15523)
- 86bbd108ec TPCLoopers: single threaded by default
- 4a1ce5cb14 [TF3] Clusterizer interface for ALICE3 TOF (#15570)
- a18e051b59 Fix usage of the MeanVertex in PVertexer

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 367e25b5 AODBcRewriter: re-sort tables stored sorted by a reordered reference
- ba8a6b20 AODBcRewriter: remap every index column an output table carries (O2-7098)
- 9d7983ac PWGDQ: add PbPb 5.36 TeV Bottomonia gap trigger generator config (#2395)
- de4c4abe PWGDQ: add PbPb 5.36 TeV Bottomonia generator parameters (#2397)
- 1e7bf822 [SigmaProton generator] Add minPt for protons and sigmas separately (#2417)
- f3990a82 Add pp 13.6 cfg with tuned diffractive events (#2415)
- a92d70bc [MC/PWGEM] add HF and DY->dimuon MC in pp at 13.6 TeV (#2414)
- 9d2776d2 Add specific EPOS4HQ parameters
- 7e41835d Add --no-qed to reliably disable QED background
- 6e8202b9 anchorMC: resolve modulecmd via readlink -f + /usr/share/Modules fallback
- c7ca6a5b anchorMC: Fail hard if modulecmd not found for 2-tag operations
- c929fac0 Disable CTP lumi if not active
- 8879050e Adding OO input shape (#2411)
- 015dba5e [PWGLF] Add finite-width resonance injection and particle definitions (#2405)
- a6836eb2 Bugfix for phi angle in PWGGAJE hooks (#2408)
- 18f55b02 Make the non-prompt injection ratio configurable also for p-O (#2402)
- c6adb1b6 ExtToHybrid parallel example (#2403)
- e4a7c3d3 [PWGGAJE] jet parametrised model: add bkg choice in ini (#2399)
- c53f5cd0 Make the non-prompt injection ratio configurable and fix EvtGen decay definitions (#2400)
- 5f8f8184 External to Hybrid example (#2401)
- f0f978d8 PWGDQ: Add Ne–Ne prompt charmonia generator configuration for anchored MC (#2394)
- d70a8d12 Add triggerLc function call to makeStarlightConfig.py (#2398)
- e03096e3 Add diffraction-tuned pythia8 inel generator (#2393)

## Contributors
- Amit Kumar Pradhan
- Christian Sonnabend
- Daiki Sekihata
- David Rohr
- Felix Schlepper
- Francesco Mazzaschi
- Giorgio Alberto Lucia
- Giulio Eulisse
- Igor Altsybeev
- Koushik Barai
- Marcello Di Costanzo
- Marco Giacalone
- Mario Ciacco
- Matthias Kleiner
- NNicassio99
- Nicolò Jacazio
- Paul Veen (paveen)
- Rrantu
- Sandro Wenzel
- Tristan Wenzel
- aimeric-landou
- ddobrigk
- donglovo
- mj525
- rebeccacerri
- shahoian
- shahor02
- smaff92
- swenzel
- wiechula