import os, sys, json

def openDir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)

def getRawPath(pathIn, dirOut):
	#TEXT_EXT = ".txt"
	temp_path = pathIn
	#dirOut = os.path.dirname(temp_path)
	temp_path = os.path.basename(temp_path)
	#fname, fext = os.path.splitext(temp_path)
	pathOut =  os.path.join(dirOut, temp_path) 
	return(pathOut)

	
def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)  

def writeListToFile(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:    
            file.write(item + "\n")

def writeDataToJSON(dataIn, pathOut):
	with open(pathOut, 'w', encoding ="utf-8") as outfile:  
		json.dump(dataIn, outfile)
