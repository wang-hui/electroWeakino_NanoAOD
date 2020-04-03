#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh  ## if a tcsh script, use .csh instead of .sh
#export SCRAM_ARCH=slc6_amd64_gcc630
echo $SCRAM_ARCH
eval `scramv1 project CMSSW CMSSW_10_2_9`
cd CMSSW_10_2_9/src
eval `scramv1 runtime -sh`
cd ${_CONDOR_SCRATCH_DIR}
pwd
ls

cmsRun step1_NANO.py $1 $2 $3

xrdcp nano_test.root root://cmseos.fnal.gov//store/user/huiwang/ElectroWeakino/nanoAOD_test/nano_mn1_${1}_mx1_${2}_${3}.root
