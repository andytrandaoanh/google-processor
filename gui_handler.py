from pymongo import MongoClient
import sys, json, time
import system_handler
from generate_id import getUniqueID

def assembleDoc(bookData, wordForm, sentence, sentID):
	
	newDoc = {'book_id': bookData['book_id'], 
		'book_title': bookData['book_title'], 
		'book_author': bookData['book_author'],
		'book_year': bookData['book_year'],  
		'key_word' : wordForm, 
		'sent_content' : sentence, 
		'sent_num': sentID}
	return newDoc

def insertDBOne(doc, db):
	try:
		
		if doc['key_word']:
		#print(doc['key_word'])
			volumnName = 'vol_' +  doc['key_word'][:1].lower()
			#print (volumnName)
			collection = db[volumnName]
			objid = collection.insert_one(doc).inserted_id
			
	except Exception as e:
		print('Error: ', e)

		

def prepareMongoWrite(inPath, outDir):

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
								'defid': getUniqueID(word),
								'word': word,
								'phonetic': phonetic,
								'category': category,
								'definition' : sense['definition']
							}
							definitionList.append(definition)
							time.sleep(0.1)
	#print(definitionList)
	#system_handler.writeListToFile(definitionList, outPath)
	
	system_handler.writeDataToJSON(definitionList, outPath)
	system_handler.openDir(outDir)
	sys.exit()
