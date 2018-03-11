import os, glob

src = raw_input("Give location of your src file : ")
pyFiles = glob.glob(src + "/*.py")

for File in pyFiles:
	print "changing filename -- " + File
	finalFile = File + "x"
	cmd = "mv " + File + " " +  finalFile
	os.system(cmd)

print os.getcwd()
with open(src + "/__init__.py", 'wb') as f:
	f.write(" ")

print "Renamed all files sucessfully"
