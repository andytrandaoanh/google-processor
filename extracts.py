import os, sys
import re
from nltk import tokenize
import json


def open_dir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)

def read_text_file(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        return data
    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)    
        



def cleanText(input_text):	    
	line = input_text
	line = line.replace('\n',' ')
	line = line.replace('\t',' ')
	return line

def getCorrectPath(fileIn, dirIn, dirOut):
	TEXT_EXTENSION = ".txt"
	JSON_EXTENSION = ".json"
	temp_path = fileIn

	temp_path = os.path.basename(temp_path)
	fname, fext = os.path.splitext(temp_path)
	pathIn =  os.path.join(dirIn, fname + TEXT_EXTENSION)
	pathOut =  os.path.join(dirOut, fname + JSON_EXTENSION) 
	return(pathIn, pathOut)

def write_list_to_file(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:
        	if (str(item) != ''):
        		file.write(item + "\n")


def extractSentences(fileIn, dirIn, dirOut):
	
	pathIn, pathOut =  getCorrectPath(fileIn, dirIn, dirOut)
	#print ('pathIn:', pathIn, 'pathOut', pathOut)
	contents = read_text_file(pathIn)

	sentences = tokenize.sent_tokenize(contents)
	#print(sentences)
	index = 0
	results =[]
	MIN_LENGTH = 20

	for sentence in sentences:	
		if (len(sentence) > MIN_LENGTH):
			index += 1
			sent_cont = cleanText(sentence)
			sentence_object = {"sent_num": index, "sent_cont": sent_cont }	
			results.append([sentence_object])				
		
	#print(results)
	with open(pathOut, 'w', encoding ="utf-8") as outfile:  
		json.dump(results, outfile)

	open_dir(dirOut)
	sys.exit()
