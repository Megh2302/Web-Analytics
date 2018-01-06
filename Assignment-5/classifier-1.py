"""
A simple script that demonstrates how we classify textual data with sklearn.

"""
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.svm import LinearSVC


#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname)
    for line in f:
        review,rating=line.strip().split('\t')  
        reviews.append(review.lower())    
        labels.append(int(rating))
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('reviews_train.txt')
rev_test,labels_test=loadData('reviews_test.txt')


#Build a counter based on the training dataset
#counter = CountVectorizer()
counter = TfidfVectorizer()
counter.fit(rev_train)


#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#train classifier
clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
#clf = MultinomialNB()
#clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,verbose=0)

#train all classifier on the same datasets
clf.fit(counts_train,labels_train)

#use hard voting to predict (majority voting)
pred=clf.predict(counts_test)

#print accuracy
print (accuracy_score(pred,labels_test))


