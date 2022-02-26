# Prey Capture

Documenting the analysis pipeline for prey capture

## Acquisition Configuration

todo -- link to the configs

## Raw Data Structure

What does the raw data look like just after acquisition?

```
./
└── 2022-02-24_9-57-53_mouse-0898
    ├── 2022-02-24_09-57-55_mouse-0898
    │   ├── 103_ADC1.continuous
    │   ├── 103_ADC2.continuous
    │   ├── 103_ADC3.continuous
    │   ├── 103_ADC4.continuous
    │   ├── 103_ADC5.continuous
    │   ├── 103_ADC6.continuous
    │   ├── 103_ADC7.continuous
    │   ├── 103_ADC8.continuous
    │   ├── 103_AUX1.continuous
    │   ├── 103_AUX2.continuous
    │   ├── 103_AUX3.continuous
    │   ├── Continuous_Data.openephys
    │   ├── all_channels.events
    │   ├── messages.events
    │   ├── notebook.mat
    │   ├── settings.xml
    │   └── stimlog.txt
    ├── Laser_mouse-0898_2022-02-24T09_57_53.csv
    ├── Sky_mouse-0898_2022-02-24T09_57_53.csv
    ├── Sky_mouse-0898_2022-02-24T09_57_53.mp4
    └── TTL_mouse-0898_2022-02-24T09_57_53.csv
```

**Timestamps**

All have two columns, one row for each frame.
The first is some data, the second an isoformatted timestamp

- `Laser_mouse-{mouse_id}_{timestamp}.csv` - laser on/off (`bool`) for each frame
- `Sky_mouse-{mouse_id}_{timestamp}.csv` - samples since camera on (unused)
- `TTL_mouse-{mouse_id}_{timestamp}.csv` - TTL pulse on/off (`bool`) for each frame

**Video**

- `Sky_mouse-{mouse_id}_{timestamp}.mp4` - Top-down view of arena

**Open Ephys**

Within a folder with name `{timestamp}_mouse-{mouse_id}`

```{todo}
Document which continuous files are which value
```

- `.continuous` files - raw timeseries of accelerometers and laser pulses
- `stimlog.txt` - .txt (actually .json) version of stimlog within `notebook.mat`
- `notebook.mat` - Experimental conditions for each trial
    - Example notebook file containing nb and stimlog
    ```
    nb =

    struct with fields:

               user: 'Molly'
            mouseID: '0894'
              Depth: 'unknown'
           datapath: 'Z:\lab\djmaus\Data\Molly'
          activedir: '\\wehrrig4\d\lab\djmaus\Data\Molly\2022-02-24_11-24-42_mouse-0894\2022-02-24_11-24-44_mouse-0894'
         LaserPower: 'unknown'
           mouseDOB: 'unknown'
           mouseSex: 'm'
      mouseGenotype: 'vgat-chr2'
              Drugs: 'none'
              notes: [5×10 char]
      Reinforcement: 'none'
    ```
    ```
    >> stimlog(1)

    ans =

    struct with fields:

                      type: 'silentsound'
                     param: [1×1 struct]
             protocol_name: 'SingleLaserFlag'
      stimulus_description: 'silentsound loop_flg:0 duration:100 ramp:0 next:1000'
      protocol_description: 'single laser ON flag for front-panel controlled laser stim'
          PlottingFunction: 'none'
                   version: 'djmaus'
                 timestamp: 'February-24-2022 11:24:45.157'
                LaserOnOff: 1
                LaserStart: 0
                LaserWidth: 10
            LaserNumPulses: 4800
                  LaserISI: 10
    ```
  
## Analysis 

Analysis Diverges from here! 

* [MATLAB Analysis](analysis/analysis_matlab.md)
  * Manually segment trials (cricket drop and capture)
  * 
* [Python Analysis](analysis/analysis_python.md) - 