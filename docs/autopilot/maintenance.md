# Maintenance

`autopilot/maintenance` in the repository

Scripts to maintain, updaate, etc. autopilot behavior rigs in wehr lab.


## `update_autopilot.sh`

The main script to update autopilot, run from the terminal computer, to keep the system up to date.

Each of the pilots has autopilot installed in `~/git/autopilot` and the plugin directory is `~/autopilot/plugins` (with the `wehrlab` plugin beneath that)

This script updates our local copy, and then calls `update_pis.sh` on each of the pis

```{literalinclude} ../../autopilot/maintenance/update_autopilot.sh
:language: bash
```

## `update_pis.sh`

Similar to `update_autopilot.sh`, but ensures that the time zone is correct for the pis.

Stdout and stderr output to `~/autopilot_update_stdout` and `~/autopilot_update_errors` on the terminal, respectively.


```{literalinclude} ../../autopilot/maintenance/update_pis.sh
:language: bash
```


## `pi_ips.txt`

Used by `update_pis.sh` to send commands to multiple pilots at once with [parallel-ssh](https://parallel-ssh.org/) (Also see [configuring SSH access with RSA keys](https://wiki.auto-pi-lot.com/index.php/SSH)).

```{literalinclude} ../../autopilot/maintenance/pi_ips.txt

```