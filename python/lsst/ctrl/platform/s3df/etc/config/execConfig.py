# flake8: noqa
config.platform.nodeSetRequired = False
config.platform.localScratch = "$USER_SCRATCH/condor_scratch"
config.platform.fileSystemDomain = "slac.stanford.edu"
config.platform.scheduler = "slurm"
config.platform.peakcpus = 120
# This is the value for nodes of the milano partition.
# Configuration per partition will be implemented in a
# followup ticket.
config.platform.peakmemory = 491520
config.platform.collector = "sdfiana012.sdf.slac.stanford.edu"
