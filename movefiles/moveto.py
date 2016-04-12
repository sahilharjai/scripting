import os
import sys
import shutil
def abspath1(path):
	return os.path.join(os.path.abspath(os.path.dirname(__file__)),os.path.expanduser(path))

def movehelper(ext,src,dest):
	files=os.path.listdir(src)
	print(files)
	for f in files:
		if os.isdir(f):
			new_src=os.path.join(src,f)
			movehelper(ext,new_src,dest)
		else:
			print(f.split(".")[-1])
			if f.split(".")[-1]==ext:
				filename=src.split("/")[-1].split(".")[0]
				shutil.copy2(src+'/'+f,dest+"/"+filename+"."+ext)



def moveto(ext,src,dest):
	src=abspath1(src)
	dest=abspath1(dest)
	print(src)
	#movehelper(ext,src,dest)
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Enter a website url to fetch images")
    else:
    	moveto(sys.argv[1],sys.argv[2],sys.argv[3])


