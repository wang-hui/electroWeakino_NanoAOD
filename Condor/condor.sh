#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh  ## if a tcsh script, use .csh instead of .sh
#export SCRAM_ARCH=slc6_amd64_gcc630
echo $SCRAM_ARCH
eval `scramv1 project CMSSW CMSSW_10_2_18`
cd CMSSW_10_2_18/src
eval `scramv1 runtime -sh`
git cms-init --upstream-only
git cms-addpkg PhysicsTools/NanoAOD
echo "ls SimpleFlatTableProducer.h"
ls ${_CONDOR_SCRATCH_DIR}/SimpleFlatTableProducer.h
mv ${_CONDOR_SCRATCH_DIR}/SimpleFlatTableProducer.h PhysicsTools/NanoAOD/interface/
git clone https://github.com/cms-jet/NanoAODJMAR.git -b 102x PhysicsTools/NanoAODJMAR
git clone https://github.com/wang-hui/JetToolbox.git JMEAnalysis/JetToolbox -b electroWeakino_hui
scram b -j 2
cd ${_CONDOR_SCRATCH_DIR}
tar -xvf FileList.tar
pwd

cmsRun nanov6102x_on_mini94x_2017_mc_NANO.py $1

xrdcp nano_test.root root://cmseos.fnal.gov//${2}/nanoAOD_${3}.root
