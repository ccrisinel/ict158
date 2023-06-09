import pymongo
import json
from csv import DictReader
import pymysql
import pymysql.cursors
import os
from datetime import datetime


client = pymongo.MongoClient("localhost", 27017)


db = client.test



# csv fileused id Geeks.csv
filename="cities.csv"

# opening the file using "with"
# statement

with open(filename, 'r') as f:

	dict_reader = DictReader(f, delimiter="\t")

	list_of_dict = list(dict_reader)

	#print(list_of_dict)

for dictionary in list_of_dict:
	if None in dictionary:
		del dictionary[None]

db.Cities.drop()
#print(list_of_dict[0])
db.Cities.insert_many(list_of_dict)

print(db.Cities.find_one())



list_of_dict_json=[]
with open('ipRecords.json') as f:
	for line in f:
		data = json.loads(line)
		del data['_id']  # remove the _id field from the JSON object
		list_of_dict_json.append(data)

for dictionary in list_of_dict_json:
	if None in dictionary:
		del dictionary[None]
#print(list_of_dict_json)
db.IpRecords.drop()

db.IpRecords.insert_many(list_of_dict_json)

print(db.IpRecords.find_one())

os.system("mongoexport --collection=Cities --db=test --out=Cities_export.json")
os.system("mongoexport --collection=IpRecords --db=test --out=IpRecords_export.json")


# Open database connection
conn = pymysql.connect(
	host='localhost',
	user='user',
	password='password',
	database='ict158'
)

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# SQL query to insert a new record


sql = """
    INSERT INTO ict158.Cities
    (`key`, firstName, asciiName, altNames, latitude, longitude, featureClass, featureCode, countryCode, altCountryCode, admin1code, admin2code, admin3code, admin4code, population, elevation, digitalElevationModel, timezone, modificationDate, altNamesSel, adminXcode, areaCode)
    VALUES (%(key)s,%(firstName)s, %(asciiName)s, %(altNames)s, %(latitude)s, %(longitude)s, %(featureClass)s, %(featureCode)s, %(countryCode)s, %(altCountryCode)s, %(admin1code)s, %(admin2code)s, %(admin3code)s, %(admin4code)s, %(population)s, %(elevation)s, %(digitalElevationModel)s, %(timezone)s, %(modificationDate)s, %(altNamesSel)s, %(adminXcode)s, %(areaCode)s);
"""


cities_export=[]

with open('Cities_export.json') as f:
	for line in f:
		data = json.loads(line)
		del data['_id']  # remove the _id field from the JSON object
		cities_export.append(data)

longest_string = max(
    [max(d.values(), key=len) for d in cities_export], key=len
)

cities_export = [{k: None if v == '' else v for k, v in d.items()} for d in cities_export]

print(longest_string)

# Execute the SQL command
cursor.execute("DELETE FROM IpRecords;")
cursor.execute("DELETE FROM Cities;")
cursor.executemany(sql, cities_export)





sql = """
INSERT INTO IpRecords (version, ip, searchPageCount, autoSearchCount, searchCount,
							passFailedCount, passRecoveryCount, languageTag, userAgent,
							lastAccessTime, isAdmin, crawlCount, crawlManCount,
							badCrawlManCount, hackManCount, blackErrorCount,
							whiteErrorCount, errorHistory, searchHistory, countryGuess,
							cityGuessSafe, cityGuess)
VALUES (%(version)s, %(ip)s, %(searchPageCount)s, %(autoSearchCount)s,
        %(searchCount)s, %(passFailedCount)s, %(passRecoveryCount)s, %(languageTag)s,
        %(userAgent)s, %(lastAccessTime)s, %(isAdmin)s, %(crawlCount)s, %(crawlManCount)s,
        %(badCrawlManCount)s, %(hackManCount)s, %(blackErrorCount)s, %(whiteErrorCount)s,
        %(errorHistory)s, %(searchHistory)s, %(countryGuess)s, %(cityGuessSafe)s, %(cityGuess)s)
"""




iprecords_export=[]

with open('IpRecords_export.json') as f:
	for line in f:
		data = json.loads(line)
		del data['_id']  # remove the _id field from the JSON object
		data["errorHistory"] = json.dumps(data["errorHistory"])
		data["searchHistory"] = json.dumps(data["searchHistory"])

		last_access_time = datetime.strptime(data["lastAccessTime"], "%Y-%m-%dT%H:%M:%S.%f%z")
		data["lastAccessTime"] = last_access_time.strftime("%Y-%m-%d %H:%M:%S")


		iprecords_export.append(data)



iprecords_export = [{k: None if v == '' else v for k, v in d.items()} for d in iprecords_export]



# Execute the SQL command

cursor.executemany(sql, iprecords_export)










# Commit your changes in the database
conn.commit()

# disconnect from server
conn.close()















# mariadb to mangodb
# Open database connection
conn = pymysql.connect(
	host='localhost',
	user='user',
	password='password',
	database='ict158'
)

# prepare a cursor object using cursor() method
cursor = conn.cursor(pymysql.cursors.DictCursor)
# SQL query to insert a new record


sql = """SELECT * FROM ict158.Cities"""
cursor.execute(sql)
cities_from_mariadb = cursor.fetchall()




cursor.close()
conn.close()


