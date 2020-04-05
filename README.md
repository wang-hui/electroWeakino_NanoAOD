# ElectroWeakino nanoAOD producer
This is a git repo to produce nanoAOD ntuples from miniAOD  
The step of making miniAOD can be found the this repo  
https://github.com/wang-hui/electroWeakino

1. setup CMSSW. Use 102X because it has more objects in nanoAOD
```
cmsrel CMSSW_10_2_9
cd CMSSW_10_2_9/src
cmsenv
```

2. checkout JetToolbox to recluster AK10 or fatter jets
```
git clone https://github.com/wang-hui/JetToolbox.git JMEAnalysis/JetToolbox -b electroWeakino_hui
scram b - j 4
```

3. checkout this repo
```
git clone https://github.com/wang-hui/electroWeakino_NanoAOD.git
cd electroWeakino_NanoAOD
```

4. local test
```
cmsRun jetToolbox_nanoAODv5_cfg.py
```

5. submit condor
```
cd Condor
python make_condor_cfg.py
condor_submit condor_submit.txt
```
