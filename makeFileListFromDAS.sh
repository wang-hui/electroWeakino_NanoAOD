set dataset = "/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"
set output = "miniAOD_2017_TTJets_SingleLeptFromT.list"

set dataset = "/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"
set output = "miniAOD_2017_QCD_HT1000to1500.list"

dasgoclient -query="file dataset=${dataset}" > ${output}
