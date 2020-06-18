# ElectroWeakino nanoAOD production
This is a git repo to produce nanoAOD ntuples from miniAOD  
The step of making miniAOD can be found in this repo  
https://github.com/wang-hui/electroWeakino  
The analysis code can be found in this repo  
https://github.com/wang-hui/electroWeakino_analysis

1. setup CMSSW. Use CMSSW_10_2_18 for 2016, 2017 and 2018 data and MC NANOAODv6 according to the XPOG recommendations
```
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src
cmsenv
```

2. checkout NanoAODJMAR to store PF candidates in nanoAOD
```
git cms-addpkg PhysicsTools/NanoAOD
git clone git@github.com:cms-jet/NanoAODJMAR.git -b 102x PhysicsTools/NanoAODJMAR
```

3. checkout JetToolbox to recluster AK10 or fatter jets
```
git clone https://github.com/wang-hui/JetToolbox.git JMEAnalysis/JetToolbox -b electroWeakino_hui
```

4. checkout this repo
```
git clone https://github.com/wang-hui/electroWeakino_NanoAOD.git
```

5. temp fix for the PhysicsTools/NanoAOD and compile
```
mv electroWeakino_NanoAOD/SimpleFlatTableProducer.h PhysicsTools/NanoAOD/interface/
scram b -j 8
```

6. local test
```
cd electroWeakino_NanoAOD
cmsRun nanov6102x_on_mini94x_2017_mc_NANO.py
```

7. submit condor
```
cd Condor
python make_condor_cfg.py
condor_submit condor_submit.txt
```
