# check_mk-mounts_layout
A Check_MK plugin for checking for the presence of defined mountpoints 

The check basically parses the mounts, nfsmounts and cifsmounts section of the standard check_mk_agent.
It  compares the found mountpoints against defined mountpoints (thresholds), if a defined threshold is missing 
in a the agent output an alert is thrown  
