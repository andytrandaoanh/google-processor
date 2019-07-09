import shortuuid
import textwrap
from datetime import datetime
import hashlib

def package_id(inputString):
	uidList = textwrap.wrap(inputString, 8)
	strOut = ''
	bFirst = True
	for uid in uidList:
		if bFirst: 
			strOut = uid 
			bFirst = False
		else:
			strOut += '-' + uid

	return strOut

def generate_id(inputString):
	DICTIONARY = 'abcdefgh0123456789'
	shortuuid.set_alphabet(DICTIONARY)	
	eventid = datetime.now().strftime('%Y%m%d%H%M%S%f')
	return(shortuuid.uuid(inputString + eventid))


def getUniqueID(inputString):
	uid = generate_id('inputString')
	return(package_id(uid))



