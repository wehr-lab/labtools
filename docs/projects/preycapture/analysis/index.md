# Analysis Overview

```{graphviz}
digraph {
  
  subgraph cluster_input {
      label = "Input"
      oe_data
      raw_video
  }
  
  subgraph cluster_python {
      label="Python"
      dlc_python[label="DeepLabCut"]
      extract_points
      geometries
      preycap_metrics
      hmm
  }
  
  subgraph cluster_matlab {
      label="MATLAB"
      idk[label="idk???"]
      
  }

  raw_video -> dlc_python
  dlc_python -> extract_points
  extract_points -> geometries
  geometries -> preycap_metrics
  geometries -> hmm
  
  raw_video -> idk
  
}
```


```{toctree}
analysis_matlab
analysis_python
```







