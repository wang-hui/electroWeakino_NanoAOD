# ElectroWeakino nanoAOD producer
This is a git repo to make ntuple from miniAOD to nanoAOD  
The step of making miniAOD can be found the this repo  
https://github.com/wang-hui/electroWeakino

1. setup CMSSW. Use 102X because it has more objects in nanoAOD
```
cmsrel CMSSW_10_2_9
cd CMSSW_10_2_9/src
cmsenv
```

2. checkout this repo
```
git clone git@github.com:wang-hui/electroWeakino_NanoAOD.git
cd electroWeakino_NanoAOD
```

3. local test
```
cmsRun step1_NANO.py
```

4. submit condor
```
cd Condor
python make_condor_cfg.py
condor_submit condor_submit.txt
```
