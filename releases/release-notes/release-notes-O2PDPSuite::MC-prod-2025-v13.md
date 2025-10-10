# Release Notes


These are release notes for O2PDPSuite::MC-prod-2025-v13 in comparison to the previous tag O2PDPSuite::MC-prod-2025-v12.

The release is based on the daily tag O2PDPSuite::daily-20251010-0000-1.


## Repository Updates
- **O2DPG**: `daily-20251001-0000` → `daily-20251010-0000`
- **O2sim**: `async-20251001.1` → `v20251010`
- **gpu-system**: `error` → `cuda_arch@86#89@_12.9.86-rocm_arch@gfx906#gfx908@_6.3.42134-opencl-miopen-migraphx-cudnn-tensorrt`
- **QualityControl**: `v1.183.0` → `daily-20251010-0000`
- **O2**: `daily-20251001-0000` → `daily-20251010-0000`
- **O2Physics**: `daily-20251001-0000` → `daily-20251010-0000`
- **AliGenO2**: `v20251001` → `v20251010`

## MC Relevant Changes

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 740d94ec Fix of an environment problem affecting 2stage processing
- b26d7189 O2DPG-MC: Adding more utilities for pipeline metric aggregation/processing
- 83b2c5a4 cleanup unused env var
- a9ace747 O2DPG: Fix vertex inconsistency between background and signal MC events
- fa2f6600 Add the `userhook` to the `ini` files used for the event pools production (#2122)
- f1a59353 further modularize o2dpg_sim_metrics
- 7c29d353 o2dpg_workflow_runner.py: Adapt format for --update-resources to that of o2dpg_sim_metrics.py
- 9e82588f MC: pvfinder need reco input only if det active
- 6b44b5d3 anchorMC: Improve checking of essential variables
- fd274b35 Dq pb pb (#2142)
- 2954b82d [PWGDQ]: updating generator Pythia8 (#2148)
- 6d329a97 add additional newline at the end of inner fun
- fc65b537 MC: add special check for IT3 mocked output
- a121b9d9 AnchorMC: Allow more option overwrites
- fc30fba2 meta info in metric json output
- 04c9dae7 o2dpg_sim_metrics: Introduce JSON statistics and merging of statistics
- e0fc2306 small beautification
- 40625bff TRD QC: Do not write tracklets
- 5ebc5798 metrics: report also max,mean disc usage
- fba4c22e Disable reading tf1 Kine files for EventStat
- 5f04d25c Top-N memory consumer feature
- 224078c1 fix detectorList argument for PbPb (#2143)
- d0e19813 MC: allow ITS3 to be simulated by dpg scripts (#2128)
- 41467f35 anchorMC: Integrate aligned geometry download into O2DPG workflow
- c979b670 Custom number of events in  generator tests

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 21092835fe Fix protection of MC signal filtering to work with any embedPatt
- b797b8ef97 Suppress reduntant versions of HelixHelper
- b1904ffa8d Fixes for modules at negative eta (#14716)
- 879a535086 Add voxel map binning
- 9220ba5aef Negative binning omits drawing the 1D distributions

## Contributors
- Chuntai
- Evgeny Kryshen
- Fabrizio Grosa
- Felix Schlepper
- Jseo
- Marco Giacalone
- Sandro Wenzel
- sgaretti
- shahoian
- swenzel
- wiechula