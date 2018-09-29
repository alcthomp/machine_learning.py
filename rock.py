from elasticsearch import Elasticsearch
es = Elasticsearch()
import json
import requests

keyList = []
keyList2 = {}

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def getProperties(d):
   propertiesValues= []
   for key, value in d.items():
	propertiesValues.append(value)
   #print(propertiesValues)

def getKeysDrillDown(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         getKeysDrillDown(value, indent+1)
	 if key == "properties":
		getProperties(value)
      else:
         print('\t' * (indent+1) + str(value))
	 print(" ")


def getIndexes(): 
	res = requests.get('http://192.168.1.16:9200/_aliases') 
	data=(res.content)
	jsondata= json.loads(data)
	#pretty((jsondata))
	x=0
	for key, value in jsondata.iteritems():
		keyList.insert(x,key)
		x=+1
	#print(keyList)

def getKeys(indexName):
	res = requests.get('http://192.168.1.16:9200/'+indexName+'/_mappings') 
	data=(res.content)
	keyList2= json.loads(data)
	getKeysDrillDown(keyList2)

	#print(keyList2)  #list of indexes in 
	#indexName/properties
	#pretty(keyList2)
	#print(keylist2['mappings'['_default_'['properties']]])

def testES(testindex):
	#res = es.index(index=testindex, doc_type='json', id=1)
	#print(res['result'])

	res = es.get(index=testindex, doc_type='json', id=1)
	print(res['_source'])

	es.indices.refresh(index=testindex)

	res = es.search(index=testindex, body={"query": {"match_all": {}}})
	print("Got %d Hits:" % res['hits']['total'])
	for hit in res['hits']['hits']:
   		print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
			
def main():
	getIndexes()
	#getKeys(keyList[5])
	#getKeysDrillDown(keyList2)
	testES(keyList[5])


if __name__=="__main__":
	main()

#http://localhost:9200/_aliases
#http://localhost:9200/index1.1*/_search?pretty=true&q=*:*
#from elasticsearch import Elasticsearch
#es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#info = es.search(index="INDEXNAME", body={"query": {"match": {'KEY':'VALUE'}}})
#info = es.search(index="lab1.1-broker", body={"query": {"@timestamp":"May 11th 2018, 14:39:07.118"}})
#print(info)
#with open("data_file.json", "w") as write_file:
    #json.dump(data, write_file)


#r = requests.get('http://localhost:9200') 
#r = requests.get('LOCATION'+ 'things')
#es.index(index='INDEXNAME', doc_type='TYPE', id=i, body=json.loads(r.content))

 
