import os, sys
import mysql.connector
from mysql.connector import errorcode

def getConnection(dbname=''):
	try:
		connection = mysql.connector.connect(
		user='andyanh', password='DGandyanh#1234',
	    host='127.0.0.1', database = dbname)
		if connection.is_connected():
			return connection 
	except Error as e:
		return e

def getWordList():
	DB_NAME = "lexicon"
	db = getConnection(DB_NAME)
	cursor = db.cursor()
	select_sql= ("select word_form from pure_words order by 1;")
	try:
		
		words =[]
		cursor.execute(select_sql)
		data = cursor.fetchall()
		for w in data:
			words.append(w[0])

		return words
	except Exception as e:
		print("Error encountered:", e)
	finally:
		cursor.close
		db.close
	