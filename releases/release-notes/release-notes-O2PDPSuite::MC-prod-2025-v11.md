# Release Notes


These are release notes for O2PDPSuite::MC-prod-2025-v11 in comparison to the previous tag O2PDPSuite::MC-prod-2025-v10.

The release is based on the daily tag O2PDPSuite::daily-20251001-0000-1.


## Repository Updates
- **O2Physics**: `daily-20250902-0000` → `daily-20251001-0000`
- **O2**: `daily-20250902-0000` → `daily-20251001-0000`
- **Control-OCCPlugin**: `v1.42.0` → `v1.44.0`
- **O2DPG**: `daily-20250902-0000` → `daily-20251001-0000`
- **ROOT**: `v6-32-06-alice9` → `v6-32-06-alice10`
- **FairMQ**: `v1.9.2` → `v1.10.0`
- **QualityControl**: `v1.181.0` → `daily-20251001-0000`
- **O2sim**: `async-20250902.1` → `v20251001`
- **AliGenO2**: `v20250902` → `v20251001`
- **gpu-system**: `error` → `cuda_arch@86#89@_12.9.86-rocm_arch@gfx906#gfx908@_6.3.42134-opencl-miopen-migraphx-cudnn-tensorrt`

## MC Relevant Changes

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 0b91842e52 Add possibility to apply signal filtering for MC with embedding (#14698)
- 774014b283 Temporarily keep reduntant HelixHelper in DCAFitter and DetectorsVertexing for O2Physics
- 99548c4276 Robust propagation to certain R
- 429846dcc7 Common: Minor cleanup of flag helper class
- 1c52969c50 Custom streamer for std::vector<o2::tpc::PadFlags>
- 8ce25b7607 Methods for layer-dependend mat.LUT rescaling
- 4dfc128054 First version of ECal sim, digitizer and clusterizer (#14697)
- cec632fcc2 Common: allow literal suffix and add tests for confkey
- c864689194 Add ITS fake clusters information to the mcMask (#14666)
- f72e1a2714 Avoid recompiling fpu.cxx a gazillion of times (#14686)
- 6a82fffbbc Add new raw data type for common mode values
- e04d84f1b6 remove new line from Track::asString, set alpha to +-pi
- 91a7d8b0ae MaterialManager: Allow density modification on the individual material level
- cc7210c48b NN clusterizer: Fixing memory access faults (#14657)
- db05c58f0f Fix inconsistencies in the HelixHelper
- 7d68370fb8 Fix EnumFlags compilation for large enums The EnumFlags fails to compile when the underlying enum has 30 or more elements.

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 1c4641e2 also disable TOF QC tasks when TOF not present
- 0ed0a86f anchoredMC: treat case of disabled TOF detector
- 40a28660 make more QC tasks dependent on detector presence
- fb7c3cd0 Target refactor in anchoredMC; Improvements for early file removal
- 14fd2607 PWGHF: Smoothen injection function vs impact parameter (#2134)
- cf337d14 PWGHF: fix the tests for .ini of `corr. bkg` and `ptHardBins` (#2136)
- 93ff9d0d O2DPG workflow_runner: New early-file removal feature
- f83b8708 MCProdInfo-CCDB: Possibility to force overwrite
- f8f369a9 Add dependence to centrality task
- 2872bb43 Add missing dependency
- 05d33f6b Add missing configuration
- 1df60891 Fix typo
- 3742aa68 Add Dzero meson in QC
- bcb042c2 fix compile error in PWGDQ/GeneratorPromptCharmonia.C
- 248c287e Update Generator_InjectedPromptCharmoniaFwdy_TriggerGap_PbPb5TeV.ini (#2130)
- 6e011468 add param for dielectron OO cocktail based on pythia (#2124)
- f535c06a UTILS: add helper script to create raw files from rawtf files for REPLAY datasets
- 17810b67 exec under bash
- 420dc041 improvements for runGRIDContainerized
- 8eb8228a O2DPG workflow: Integration of fileaccess reporting
- 9d0149b1 change configuration (#2127)
- ec128f33 change eta gap (#2125)
- 5a52d241 filemonitor improvements
- 3a567c0a adjustments to runGRIDContainerized
- 07ed1d34 improvements and alternative version for fileaccess monitoring
- 3a0c8129 Restrict search space in MCProd harvester tool
- b2a9dccf pronmpt onia at 9.6 TeV extrapolated (#2123)
- 80c2339a Charmonium generator for pO (#2120)
- 58146a16 Fix light ion generator (#2118)
- 0b2c1146 MC/PWGEM: add DY->ll config (#2117)
- 865fc3a9 Remove default workflow detector list from anchorMC
- c2f0bca2 Take out CPV, PHS, ZDC from workflow when they are not in the run
- 04b9d6b0 New config for analysis task - reduce verbosity
- 02227c5d modify decay chains (#2112)
- a81c61fa For light ions at mid rapidity (#2111)
- ddbd7a1c removing useless process from pythia config (#2110)

## Contributors
- Christian Sonnabend
- Chuntai
- Daiki Sekihata
- Ernst Hellbar
- Evgeny Kryshen
- Fabrizio
- Fabrizio Chinu
- Fabrizio Grosa
- Felix Schlepper
- Francesco Mazzaschi
- Giulio Eulisse
- Jonghan Park
- Sandro Wenzel
- Sebastian Scheid
- aferrero2707
- lucamicheletti93
- mcoquet642
- sgaretti
- shahoian
- shreyasiacharya
- swenzel
- wiechula