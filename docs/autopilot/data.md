# Data

Tips for handling autopilot data!

## Split Subject Data by Session

The {meth}`~autopilot.core.subject.Subject` data interface in autopilot can return trial data as a pandas {class}`~pandas.DataFrame`, which can then use its {meth}`~pandas.DataFrame.groupby` method to write separate .csvs for each session

```{literalinclude} ../../autopilot/data/split_session_data.py
:language: python
```
