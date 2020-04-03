import glob
from shutil import copyfile

folder_name = "miniAOD_test"
folder_path = "/eos/uscms/store/user/huiwang/ElectroWeakino/"
file_list = glob.glob(folder_path + folder_name + '/mini*.root')

header = ""

for file_name in file_list:
	useful_part = file_name.split("mn1_")[1].split(".")[0]
	mn1 = useful_part.split("_mx1_")[0]
	mx1 = useful_part.split("_mx1_")[1].split("_")[0]
	file_index = useful_part.split("_mx1_")[1].split("_")[1]
	header = header + "\nArguments = " + mn1 + " " + mx1 + " " + file_index
	header = header + "\nQueue"

copyfile("condor_submit.back", "condor_submit.txt")
f = open("condor_submit.txt", "a")
f.write(header)
f.close()
