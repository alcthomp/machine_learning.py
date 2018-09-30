
import scipy
import numpy
import anaconda
import sklearn
 #Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import model_selection

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
def importML():
        # Check the versions of libraries

        # Python version
        import sys
        print('Python: {}'.format(sys.version))
        # scipy
        import scipy
        print('scipy: {}'.format(scipy.__version__))
        # numpy
        import numpy 
        print('numpy: {}'.format(numpy.__version__))
        # matplotlib
        import matplotlib
        print('matplotlib: {}'.format(matplotlib.__version__))
        # pandas 
        import pandas 
        print('pandas: {}'.format(pandas.__version__))
        # scikit-learn
        import sklearn
        print('sklearn: {}'.format(sklearn.__version__))




def crap():
          print("hello")
        print(dataset.shape)
        print(dataset.describe())
        print(dataset.groupby('class').size())
        dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
        plt.show()
        dataset.hist()
        plt.show()
        # histograms
        dataset.hist()
        plt.show()
        scatter_matrix(dataset)
        plt.show()

        
        clf = RandomForestClassifier(n_jobs=4,n_estimators=ops.numtrees, oob_score=True)
        Y,_=pd.factorize(train['class'])
        clf.fit(train.drop('class',axis=1),y)
        test['prediction'] = clf.predict(testnoclass)

	#malware-traffic-analysis.net
        #contagio malware dump
def main():
        importML()   
if __name__ == "__main__":
        main()



#./train_flows_rf.py -o data/http-malware.log http-training.log

#./analyze_flows.py http-production-2016-05-02     
