#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import glob

folder_name = "nanoAOD_test"
folder_path = "/eos/uscms/store/user/huiwang/ElectroWeakino/"
folder_path = ""
mass_point = "nano_mn1_300_mx1_310"
#mass_point = "nano_mn1_300_mx1_350"

file_list = glob.glob(folder_path + folder_name + "/" + mass_point + "*.root")

inputFile = file_list
outputFile = mass_point + "_plots.root"
#inputFile = ["/eos/uscms/store/user/huiwang/ElectroWeakino/TTJets_SingleLeptFromT_NANOAODSIM_102X_mc2017_realistic_v7-v1_F08E36CF-94D2-0946-BFBE-BBC75FE0AE71.root"]
#outputFile = "TTbar_plots.root"

maxEvents = 0
#maxEvents = 100000

class ExampleAnalysis(Module):
    def __init__(self):
	self.writeHistFile=True

    def beginJob(self,histFile=None,histDirName=None):
	Module.beginJob(self,histFile,histDirName)

	#basic kinematics
	self.PU_h=ROOT.TH1F('PU_h', 'pileup', 100, 0, 100)
        self.addObject(self.PU_h)
	self.nJets_h=ROOT.TH1F('nJets_h', 'nJets pt 20, eta 2.4', 20, 0, 20)
        self.addObject(self.nJets_h)
	self.nFatJets_h=ROOT.TH1F('nFatJets_h', 'nFatJets pt 20, eta 2.4', 20, 0, 20)
        self.addObject(self.nFatJets_h)
	self.fat_mother_mass_h=ROOT.TH1F('fat_mother_mass_h', 'mass of leading two FatJets pt 20, eta 2.4', 100, 0, 2000)
        self.addObject(self.fat_mother_mass_h)
	self.HT_h=ROOT.TH1F('HT_h', 'HT, jet pt 20, eta 2.4', 100, 0, 2000)
        self.addObject(self.HT_h)
	self.gen_HT_h=ROOT.TH1F('gen_HT_h', 'gen HT, gen jet pt 20, eta 2.4', 100, 0, 2000)
        self.addObject(self.gen_HT_h)
	self.mu_pt_h=ROOT.TH1F('mu_pt_h', 'muon pt', 100, 0, 100)
        self.addObject(self.mu_pt_h)
	self.gen_mu_pt_h=ROOT.TH1F('gen_mu_pt_h', 'gen muon pt', 100, 0, 100)
        self.addObject(self.gen_mu_pt_h)
	self.ele_pt_h=ROOT.TH1F('ele_pt_h', 'electron pt', 100, 0, 100)
        self.addObject(self.ele_pt_h)
	self.ele_veto_pt_h=ROOT.TH1F('ele_veto_pt_h', 'electron pt, veto ID', 100, 0, 100)
        self.addObject(self.ele_veto_pt_h)
	self.ele_iso1p2_pt_h=ROOT.TH1F('ele_iso1p2_pt_h', 'electron pt, relIso 1.2', 100, 0, 100)
        self.addObject(self.ele_iso1p2_pt_h)
	self.gen_ele_pt_h=ROOT.TH1F('gen_ele_pt_h', 'gen electron pt', 100, 0, 100)
        self.addObject(self.gen_ele_pt_h)

	#cutFlows
	self.cutFlow_fatjet_h=ROOT.TH1F('cutFlow_fatjet_h', '0: all, 1: nFatJet = 2, 2: n1 x1 gen match', 3, 0, 3)
        self.addObject(self.cutFlow_fatjet_h)
	self.cutFlow_ele_trigger_h=ROOT.TH1F('cutFlow_ele_trigger_h', '0: all, 1: pass trigger, 2: nEle(veto ID, pt 20, eta 2.4) > 0', 3, 0, 3)
        self.addObject(self.cutFlow_ele_trigger_h)
	self.cutFlow_mu_trigger_h=ROOT.TH1F('cutFlow_mu_trigger_h', '0: all, 1: pass trigger, 2: nMu(loose ID, pt 20, eta 2.4) > 0', 3, 0, 3)
        self.addObject(self.cutFlow_mu_trigger_h)
	self.cutFlow_HT_trigger_h=ROOT.TH1F('cutFlow_HT_trigger_h', '0: all, 1: pass trigger, 2: nMu(loose ID, pt 20, eta 2.4) > 0', 3, 0, 3)
        self.addObject(self.cutFlow_HT_trigger_h)
	self.Ele20_iso_h=ROOT.TH1F('Ele20_iso_h', '0: all, 1: ele pt > 20, eta < 2.4, 2: ele jetRelIso < 1.2, 3: ele miniPFRelIso_all < 1.2, 4: ele pfRelIso03_all < 1.2', 5, 0, 5)
        self.addObject(self.Ele20_iso_h)
	self.cutFlow_Ele15_IsoVVVL_PFHT450_h=ROOT.TH1F('cutFlow_Ele15_IsoVVVL_PFHT450_h', '0: all, 1: nEle > 0, 2: ele pt > 20, eta < 2.4, 3: ele relIso < 1.2, 4: HT > 550, 5: pass trigger', 6, 0, 6)
        self.addObject(self.cutFlow_Ele15_IsoVVVL_PFHT450_h)
	self.cutFlow_Mu15_IsoVVVL_PFHT450_h=ROOT.TH1F('cutFlow_Mu15_IsoVVVL_PFHT450_h', '0: all, 1: nMu > 0, 2: mu pt > 20, eta < 2.4, 3: mu relIso < 1.2, 4: HT > 550, 5: pass trigger', 6, 0, 6)
        self.addObject(self.cutFlow_Mu15_IsoVVVL_PFHT450_h)

    def analyze(self, event):
	pileup = Object(event, "Pileup")
	hlt = Object(event, "HLT")
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        fatjets = Collection(event, "FatJet")
        jets = Collection(event, "Jet")
        gen_jets = Collection(event, "GenJet")
        gen_fatjets = Collection(event, "GenJetAK8")
        gen_parts = Collection(event, "GenPart")

	nEle = len(electrons)
	nEle_pt20 = 0
	nEle_pt20_veto = 0
	nEle_pt20_iso1p2 = 0
	nEle_pt20_iso1p2_miniPFRelIso_all = 0
	nEle_pt20_iso1p2_pfRelIso03_all = 0

	nMu = len(muons)
	nMu_pt20 = 0
	nMu_pt20_iso1p2 = 0

	self.PU_h.Fill(pileup.nPU)

	nn1_mother = 0
	nx1_mother = 0
	n1_mother = ROOT.TLorentzVector()
	x1_mother = ROOT.TLorentzVector()
	gen_part_pdgId = []
	for gen_part in gen_parts:
		gen_part_pdgId.append(gen_part.pdgId)
		if abs(gen_part.pdgId) == 1000022 and gen_part.genPartIdxMother == 0:
			nn1_mother += 1
			n1_mother = gen_part.p4()
		if abs(gen_part.pdgId) == 1000024 and gen_part.genPartIdxMother == 0:
			nx1_mother += 1
			x1_mother = gen_part.p4()
		if gen_part.status == 1:
			if abs(gen_part.pdgId) == 11 and gen_part.pt > 5 and abs(gen_part.eta) < 2.4: self.gen_ele_pt_h.Fill(gen_part.pt)
			if abs(gen_part.pdgId) == 13 and gen_part.pt > 3 and abs(gen_part.eta) < 2.4: self.gen_mu_pt_h.Fill(gen_part.pt)
	#print gen_part_pdgId
	#print nn1_mother, nx1_mother

	for electron in electrons:
		self.ele_pt_h.Fill(electron.pt)
		if electron.pt > 20 and abs(electron.eta) < 2.4:
			nEle_pt20 += 1
			if electron.cutBased >= 1:
				nEle_pt20_veto += 1
			if electron.jetRelIso < 1.2:
				nEle_pt20_iso1p2 += 1
			if electron.miniPFRelIso_all < 1.2:
				nEle_pt20_iso1p2_miniPFRelIso_all += 1
			if electron.pfRelIso03_all < 1.2:
				nEle_pt20_iso1p2_pfRelIso03_all += 1
		if electron.cutBased >= 1: #cut-based ID Fall17 V2 (0:fail, 1:veto, 2:loose, 3:medium, 4:tight)
			self.ele_veto_pt_h.Fill(electron.pt)
		if electron.jetRelIso < 1.2:
			self.ele_iso1p2_pt_h.Fill(electron.pt)

	for muon in muons:
		self.mu_pt_h.Fill(muon.pt)
		if muon.pt > 20 and abs(muon.eta) < 2.4:
			nMu_pt20 += 1
			if muon.jetRelIso < 1.2:
				nMu_pt20_iso1p2 += 1

	ht = 0
	jets_pt20 = []
	fatjets_pt20 = []
	for jet in jets:
		if jet.pt > 20 and abs(jet.eta) < 2.4:
			jets_pt20.append(jet)
			ht = ht + jet.pt
	for fatjet in fatjets:
		if fatjet.pt > 20 and abs(fatjet.eta) < 2.4:
			fatjets_pt20.append(fatjet)

	nJets = len(jets_pt20)
	nFatJets = len(fatjets_pt20)

	self.cutFlow_fatjet_h.Fill(0)
	if nFatJets == 2:
		self.cutFlow_fatjet_h.Fill(1)
		n1_match = False
		x1_match = False
		for fatjet_pt20 in fatjets_pt20:
			if n1_mother.DeltaR(fatjet_pt20.p4()) < 0.8: n1_match = True
			if x1_mother.DeltaR(fatjet_pt20.p4()) < 0.8: x1_match = True
		if n1_match and x1_match: self.cutFlow_fatjet_h.Fill(2)
		fat_mother = ROOT.TLorentzVector()
		fat_mother = fatjets_pt20[0].p4() + fatjets_pt20[1].p4()
		self.fat_mother_mass_h.Fill(fat_mother.M())

	self.nJets_h.Fill(nJets)
	self.nFatJets_h.Fill(nFatJets)
	self.HT_h.Fill(ht)

	gen_ht = 0
	for gen_jet in gen_jets:
		if gen_jet.pt > 20 and abs(gen_jet.eta) < 2.4:
			gen_ht = gen_ht + gen_jet.pt
	#if len(gen_fatjets) > 0: 
#		for gen_fatjet in gen_fatjets:
#			print len(gen_fatjets), gen_fatjet.hadronFlavour, gen_fatjet.partonFlavour

	self.gen_HT_h.Fill(gen_ht)

	self.cutFlow_ele_trigger_h.Fill(0)
	self.cutFlow_Ele15_IsoVVVL_PFHT450_h.Fill(0)
	self.Ele20_iso_h.Fill(0)
	if nEle > 0:
		self.cutFlow_Ele15_IsoVVVL_PFHT450_h.Fill(1)
		if nEle_pt20 > 0:
			self.cutFlow_Ele15_IsoVVVL_PFHT450_h.Fill(2)
			self.Ele20_iso_h.Fill(1)
			if nEle_pt20_iso1p2 > 0:
				self.cutFlow_Ele15_IsoVVVL_PFHT450_h.Fill(3)
				self.Ele20_iso_h.Fill(2)
				if ht > 550: self.cutFlow_Ele15_IsoVVVL_PFHT450_h.Fill(4)
			if nEle_pt20_iso1p2_miniPFRelIso_all > 0:
				self.Ele20_iso_h.Fill(3)
			if nEle_pt20_iso1p2_pfRelIso03_all > 0:
				self.Ele20_iso_h.Fill(4)
	if hlt.Ele15_IsoVVVL_PFHT450:
		self.cutFlow_Ele15_IsoVVVL_PFHT450_h.Fill(5)
		self.cutFlow_ele_trigger_h.Fill(1)
		if nEle_pt20_veto > 0:
			self.cutFlow_ele_trigger_h.Fill(2)

	self.cutFlow_mu_trigger_h.Fill(0)
	self.cutFlow_Mu15_IsoVVVL_PFHT450_h.Fill(0)
	if nMu > 0:
		self.cutFlow_Mu15_IsoVVVL_PFHT450_h.Fill(1)
		if nMu_pt20 > 0:
			self.cutFlow_Mu15_IsoVVVL_PFHT450_h.Fill(2)
			if nMu_pt20_iso1p2 > 0:
				self.cutFlow_Mu15_IsoVVVL_PFHT450_h.Fill(3)
				if ht > 550: self.cutFlow_Mu15_IsoVVVL_PFHT450_h.Fill(4)
	if hlt.Mu15_IsoVVVL_PFHT450:
		self.cutFlow_Mu15_IsoVVVL_PFHT450_h.Fill(5) 
		self.cutFlow_mu_trigger_h.Fill(1)
		if nMu_pt20 > 0:
			self.cutFlow_mu_trigger_h.Fill(2)
	self.cutFlow_HT_trigger_h.Fill(0)
	if hlt.PFHT1050:
		self.cutFlow_HT_trigger_h.Fill(1)
		if nMu_pt20 > 0:
			self.cutFlow_HT_trigger_h.Fill(2)

        return True

preselection=""
p=PostProcessor(".",inputFile,cut=preselection,branchsel=None,modules=[ExampleAnalysis()],noOut=True,histFileName=outputFile,histDirName="plots",maxEntries = maxEvents)
p.run()
