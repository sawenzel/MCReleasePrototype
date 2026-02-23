# Release Notes


These are release notes for O2PDPSuite/MC-prod-2026-v4-1 in comparison to the previous tag O2PDPSuite/MC-prod-2026-v3-1.

The release is based on the daily tag O2PDPSuite/daily-20260223-0000-1.


## Repository Updates
- **FairMQ**: `v1.10.0` → `v1.10.1`
- **libInfoLogger**: `v2.8.3` → `v2.10.0`
- **O2Physics**: `daily-20260205-0000` → `daily-20260223-0000`
- **JAliEn-ROOT**: `0.7.15` → `0.7.16`
- **Monitoring**: `v3.19.8` → `v3.19.10`
- **Common-O2**: `v1.6.3` → `v1.6.4`
- **alibuild-recipe-tools**: `0.2.6` → `v0.3.0`
- **O2DPG**: `daily-20260205-0000` → `daily-20260223-0000`
- **O2**: `daily-20260205-0000` → `daily-20260223-0000`
- **libjalienO2**: `0.2.0` → `0.2.3`
- **O2sim**: `async-20260205.1` → `v20260223`
- **Control-OCCPlugin**: `v1.48.0` → `v1.48.2`
- **TBB**: `v2021.5.0` → `v2022.3.0`
- **gpu-system**: `cuda_12.9.86_arch@80_real#86_real#89_real#120_real#75_virtual@_home_F52XG4RPNRXWGYLMF5RXKZDBBI000000-rocm_6.3.42134_arch@gfx906#gfx908@_home_F5XXA5BPOJXWG3IK-opencl-miopen-migraphx-cudnn-tensorrt` → `cuda_13.1.115_arch@75_virtual@_home_F52XG4RPNRXWGYLMF5RXKZDBBI000000-rocm_6.3.42134_arch@gfx906@_home_F5XXA5BPOJXWG3IK-opencl-miopen-migraphx-cudnn-tensorrt`
- **AliGenO2**: `v20260205` → `v20260223`
- **QualityControl**: `v1.186.0` → `daily-20260223-0000`

## MC Relevant Changes

### O2DPG
This is the list of commits in dirs matching: `^MC/.*`, `^GRID/.*`, `UTILS/.*`

- 2ea99ec6 No generator with forced beauty and charm hadron semileptonic decays (#2277)
- 6cd7584e use of GeneratorPYTHIA8 to generate background events instead of duplicate PYTHIA8 for injection mode (#2273)
- 0d6ff3c5 Add Non-HFE–enhanced dataset configuration (#2189)
- c6a2269d Add new generator to trigger on events with at least two lambdas (#2271)
- 0f6d1378 Remap TPC time gain objects for MC anchored to 2023, where --tpc-mc-time-gain option does not exist
- 1608b583 Central PbPb generator with added strangeness (#2269)
- ba914591 Creat a dedicated config for the ppref (#2260)
- bc617506 Files required for an O2DPG production of prompt-photon MC, with a ga… (#2255)
- c0386a16 Update 13.6 TeV config to use MB gap 2 (#2266)
- ff554106 New Tau decays (#2267)
- aa2877a3 [PWGEM] Add configs for Dalitz-decay MC (#2263)
- 81286d28 [PWGDQ] Shifting CM frame of generated charmonia in pO (#2262)
- 99945274 Set TPCLoopers as debug generator (#2265)
- 2d833476 PbPb cocktail (#2264)

### O2
This is the list of commits in dirs matching: `^CCDB/.*`, `^Common/SimConfig/.*`, `^Common/MathUtils/.*`, `^Common/Utils/.*`, `^DataFormats/.*`, `^Detectors/AOD/.*`, `^Detectors/Base/.*`, `^Detectors/.*/simulation/.*`, `^Detectors/.*/base/.*`, `^Detectors/.*sim.*`, `^Generators/.*`, `^Common/.*`, `^run/.*`

- 16ee3b839f [ALICE3] Add proto segmentation of TF3 (#15081)
- 4728518ad3 [ALICE] Fix TRK services crossing (#15085)
- cb599998aa FIT: Delete unused files (#15031)
- 813e416361 CCDB: report stats about CCDB fetches / misses to DPL
- 98820e9b68 EMCAL: Delete unused files (#15026)
- db8db2f046 Ctpdev: getting list of unmasked inputs (#15082)
- 0b483951ab [ALICE3] Change to upper-case 'S' in "FT3sensor_*" strings  (#15078)
- d384645a99 ALICE3-TRK: fix detector ID assignment to hits (#15074)
- d95be4db7b o2-sim: Possibility to switch between TGeo and Geant4 navigation
- 06150434b8 A3: Add geometries for IOTOF (#15073)
- e5768cde63 ALICE3-TRK: adapt ordering key for digits to the large number of columns in the VD (#15070)
- e57a6edf96 Configurable VD design, set def to IRIS 4, remove IRIS disks (#15055)
- 0355d19f2a [ALICE3] Fix geometry overlaps in tracker (ML/OT) (#15072)
- 8361c429fd Add option to compress out non-dEdx info in TrackQA table (#15045)
- 17d865e646 Fix Header info forwarding
- 48c0b5433f Support to plug-and-play external (CAD) geometry
- 7c50309030 [A3 TRK] Fix kCylinder option + services crossing (#15067)
- ab29595c91 Update examples on AO2D creation from MCTracks (#15056)
- f926fb83e7 MUON: Delete unused files (#15027)
- 93cae7b660 ITS3: split longerons, improving stepping speed (#15052)
- 7c79e17a0c TPC: time gain calibration optimizations
- 970ed8ea73 EventsPerBC calibration task for FT0 (O2-6563) (#14986)
- 331f2cc815 fix topology adjust corner case (#15053)
- bf8a4027b3 Fix codechecker violation
- a63c9c1172 TRD: Delete unused files
- d43ba29f8b SimulationDataFormat: Delete unused files
- 1fd232899d ALICE3 Sensor orientation fix + first try to close in-stave gaps (#15043)
- 7830e9c54d DataFormats: Delete unused files (#15029)
- 1dedc84cef Store TPC track A/C side info in the AO2D TrackExtra.fFlags unused bits (#15014)
- c2cae5e773 Add ability to retain TrackQA for all global tracks (#15010)
- c8834dee0b Promote --ctf-dict from process to workflow level option

## Contributors
- Andrea Sofia Triolo
- Anton Alkin
- Chiara De Martin
- David Rohr
- Felix Schlepper
- Giulio Eulisse
- Hirak Koley
- Jesper Karlsson Gumprecht
- Marco Giacalone
- Marco van Leeuwen
- Matthias Kleiner
- Nicolò Jacazio
- Pavel Larionov
- Rashi gupta
- Raymond Ehlers
- Roman Lietava
- Sandro Wenzel
- Stefano Cannito
- Vít Kučera
- Wiktor Pierożak
- altsybee
- ddobrigk
- lgansbartl
- mbroz84
- mcoquet642
- rbailhac
- sejeong8
- shahoian
- shahor02
- smaff92
- tubagundem