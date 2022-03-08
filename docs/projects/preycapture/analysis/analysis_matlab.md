# MATLAB

```{todo}
- how does this relate to the processing pipeline described in the index?
- Get an example of `s1` and document it
```
Code from the [wehr-lab/Behavior](https://github.com/wehr-lab/Behavior) repository.

Starting with [CalculateMetricsSky.m](https://github.com/wehr-lab/Behavior/blob/master/CalculateMetricsSky.m) for reference

## Inputs

- `conversion` - cm/px conversion factor from pixels to centimters
- `VideoFS` - frame rate of camera
- `s1` - from Nick's specific loading function

## Processing Stages

### Individual Animal

For the mouse and cricket...

- `GetMidpoints`
- `GetDistance`
- `GetAngVelAcl`
- `GetSpdVelAcl`
- `GetPolarSpdVelAcl`

### Combined Mouse & Cricket

- `GetDistance`
- `GetAngVelAcl`

### Clip Values

- `ClipMetricNaN` for each of the intermediate values

## Output

One matlab struct with fields

- `MusThigmo`
- `CrickThigmo`
- `Crange`
- `MusTheta`
- `CrickTheta`
- `vMusBearing`
- `Azimuth`
- `MCangle`
- `MusSpeed`
- `CrickSpeed`
- `MusV`
- `CrickV`
- `MusVp`
- `CrickVp`

