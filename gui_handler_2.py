from pymongo import MongoClient
import sys, json, time
import system_handler


def processSingle(inPath, outDir):

	#print(inPath, outDir)

	outPath = system_handler.getRawPath(inPath, outDir)
	#print('outPath:', outPath)
	with open(inPath) as f:
		Entries = json.load(f)
	#print(Entries[0])
	
	definitionList = []

	for Entry in Entries:
		for subEntry in Entry:
			#for key, value in subEntry.items():
			#	print('\nkey:', key, '\nvalue:', value )
			word = None
			phonetic = None
			category = None

			subKeys = list(subEntry.keys())
			if ('word' in subKeys):
				word = subEntry['word']
			if ('phonetic' in subKeys):
				phonetic = subEntry['phonetic']
			if ('meaning' in subKeys):
				meaning =  subEntry['meaning']
				#print('meaning object:', meaning)
				meaningKeys = list(meaning.keys())
				for meaningKey in meaningKeys:
					category = meaningKey
					senses = meaning[meaningKey]
					#print('category', category)
					for sense in senses:
						senseKeys = list(sense.keys())
						if ('definition' in senseKeys):
							definition = {
								#'defid': getUniqueID(word),
								'word': word,
								'phonetic': phonetic,
								'category': category,
								'definition' : sense['definition']
							}
							definitionList.append(definition)
							#time.sleep(0.1)
	#print(definitionList)
	#system_handler.writeListToFile(definitionList, outPath)
	
	system_handler.writeDataToJSON(definitionList, outPath)




def processMultiple(inDir, outDir):
	#print(inDir, outDir)
	jsonList = system_handler.getFileFromFolder(inDir)
	#print(jsonList)
	for jsonPath in jsonList:
		processSingle(jsonPath, outDir)


	system_handler.openDir(outDir)
	sys.exit()