import os, sys
import json
from mysql_handler import prepare_data_for_update 


def getCorrectPath(fileIn, dirIn):
	
	JSON_EXTENSION = ".json"
	temp_path = fileIn
	temp_path = os.path.basename(temp_path)
	fname, fext = os.path.splitext(temp_path)
	pathOut =  os.path.join(dirIn, fname + JSON_EXTENSION) 
	return(pathOut)

def read_text_file(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        words = data.split()
        return words

    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)    
 
def write_list_to_file(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:
        	if (str(item) != ''):
        		file.write(item + "\n")



def uploadData(inPath, dbDir, bookID):
	#print('inPath:', inPath, 'dbDir:', dbDir, 'bookID:', bookID)
	#print(pathNin, pathSin)
	jsonPath = getCorrectPath(inPath, dbDir)
	#print(jsonPath)
	with open(jsonPath) as f:
		sentences = json.load(f)
	
	dbData = []
	for sentence in sentences:
		temp = sentence[0]
		dbData.append((int(bookID), temp['sent_cont'], temp['sent_num']))
		
	prepare_data_for_update(dbData)
