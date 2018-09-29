import json
from pprint import pprint\
from elasticsearch import Elasticsearch
es = Elasticsearch()

trafficList = ["srcIP","srcPort","dstIP","dstPort"]

def main(): 
	
        clf = RandomForestClassifier(n_jobs=4,n_estimators=ops.numtrees, oob_score=True)
        Y,_=pd.factorize(train['class'])
        clf.fit(train.drop('class',axis=1),y)
        test['prediction'] = clf.predict(testnoclass)

        #scikit-learn

	#malware-traffic-analysis.net
        #contagio malware dump

        
if __name__ == "__main__":
    main()


#./train_flows_rf.py -o data/http-malware.log http-training.log

#./analyze_flows.py http-production-2016-05-02     
