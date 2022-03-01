# Analysis Overview

```{graphviz}
digraph {
  bgcolor="#131416"
  fontcolor="#ffffffcc"
  color="#368ce2"
  node [color="#d0d0d0", fontcolor="#d0d0d0"]
  edge [color="#ed9d13"]

  subgraph cluster_videoinput {
      label = "Video Input"
      raw_video
  }

  subgraph cluster_ephys {
      label = "Ephys Input"
      oe_data
  }

  subgraph cluster_preprocessing {
      label = "Preprocessing"
      dlc_python[label="DeepLabCut"]
      ProcessCams
      AssimilateSignals
      Segmentation
      AssimilateSegmentation
  }

  subgraph cluster_python {
      label="Python"
      extract_points
      geometries
      preycap_metrics
      hmm
  }

  subgraph cluster_matlab {
      label="MATLAB"
      filter_smooth
      geometry_calculations
  }

      subgraph cluster_kilosort {
        label = "Kilosort"
        master8TT
        phy
        ProcessSpikes
    }

  raw_video -> dlc_python
  raw_video -> ProcessCams
  dlc_python -> ProcessCams
  ProcessCams -> AssimilateSignals
  Segmentation -> AssimilateSegmentation
  AssimilateSignals -> AssimilateSegmentation

  dlc_python -> extract_points
  extract_points -> geometries
  geometries -> preycap_metrics
  geometries -> hmm

  ProcessCams -> filter_smooth
  filter_smooth -> geometry_calculations

  oe_data -> master8TT
  master8TT -> phy
  phy ->ProcessSpikes

  ProcessSpikes -> AssimilateSignals
}
```


```{toctree}
analysis_matlab
analysis_python
```
