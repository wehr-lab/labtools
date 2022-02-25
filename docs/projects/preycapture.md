# Prey Capture

Documenting the analysis pipeline for prey capture

## Acquisition Configuration

todo -- link to 

## Starting point

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

* `Laser_mouse-{mouse_id}_{timestamp}.csv` - laser on/off (`bool`) for each frame
* `Sky_mouse-{mouse_id}_{timestamp}.csv` - samples since camera on (unused)
* `TTL_mouse-{mouse_id}_{timestamp}.csv` - TTL pulse on/off (`bool`) for each frame

**Video**

* `Sky_mouse-{mouse_id}_{timestamp}.mp4` - Top-down view of arena

**Open Ephys**

Within a folder with name `{timestamp}_mouse-{mouse_id}`

```{todo}
Document which continuous files are which value
```

* `.continuous` files - raw timeseries of accelerometers and laser pulses
* `notebook.mat` - Experimental conditions for each trial