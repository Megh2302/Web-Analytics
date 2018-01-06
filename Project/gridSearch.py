
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from nltk.corpus import stopwords
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer


def loadData(fname,i):
    reviews=[]
    labels=[]
    f=open(fname)
    
    
    for line in f:
        review =line.strip().split('\t')  
        
        reviews.append(review[0].lower())
        
        labels.append(review[i])
    f.close()
    return reviews,labels

# i = 1 GoodForKids
# i = 2 isWiFi
# i = 3 GoodForGroups
# i = 4 Parking
# i = 5 outdoorSeating
j = 1    
for i in range(1,11):

    if i == 1: print('Prediction for GoodForKids ')
    if i == 3: print('Prediction for isWiFi ')
    if i == 5: print('Prediction for GoodForGroups ')
    if i == 7: print('Prediction for Parking')
    if i == 9: print('Prediction for OutdoorSeating ')
    
    rev_train,labels_train=loadData('train_review_All.txt',j)
    rev_test,labels_test=loadData('test_review_All.txt',j)
    
    if i%2 != 0: 
        counter = CountVectorizer(stop_words=stopwords.words('english'))
        print('Using CountVectorizer \n')
    else: 
        counter = TfidfVectorizer(stop_words=stopwords.words('english'))
        print('Using TfidfVectorizer \n')
        j = j + 1
        
    counter.fit(rev_train)
    
    
    counts_train = counter.transform(rev_train)
    counts_test = counter.transform(rev_test)
    
    KNN_classifier=KNeighborsClassifier()
    LREG_classifier=LogisticRegression()
    DT_classifier = DecisionTreeClassifier()
    NB_classifier = MultinomialNB()
    
    predictors=[('knn',KNN_classifier),('lreg',LREG_classifier),('dt',DT_classifier),('nb',NB_classifier)]
    
    VT=VotingClassifier(predictors)
    
    
    #=======================================================================================
    
    NB_grid = [ {'alpha':[0.8, 0.85, 0.9, 0.95, 1.0],'fit_prior':[True,False]}]
    
    gridsearchNB  = GridSearchCV(NB_classifier, NB_grid, cv=10)
    
    gridsearchNB.fit(counts_train,labels_train)
    
    predicted=gridsearchNB.predict(counts_test)
    
    print('Accuracy for MultinomialNB')
    print (accuracy_score(predicted,labels_test))
    print(' ')
    
    #=======================================================================================
    
    KNN_grid = [{'n_neighbors': [1,3,5,7,9,11,13,15,17], 'weights':['uniform','distance']}]
    
    gridsearchKNN = GridSearchCV(KNN_classifier, KNN_grid, cv=10)
    
    gridsearchKNN.fit(counts_train,labels_train)
    
    predicted=gridsearchKNN.predict(counts_test)
    
    print('Accuracy for KNeighborsClassifier')
    print (accuracy_score(predicted,labels_test))
    print(' ')
    #=======================================================================================
    
    DT_grid = [{'max_depth': [3,4,5,6,7,8,9,10,11,12],'criterion':['gini','entropy']}]
    
    gridsearchDT  = GridSearchCV(DT_classifier, DT_grid, cv=10)
    
    gridsearchDT.fit(counts_train,labels_train)
    
    predicted=gridsearchDT.predict(counts_test)
    
    print('Accuracy for DecisionTreeClassifier')
    print (accuracy_score(predicted,labels_test))
    print(' ')
    #=======================================================================================
    
    LREG_grid = [ {'C':[0.5,1,1.5,2],'penalty':['l1','l2']}]
    
    gridsearchLREG  = GridSearchCV(LREG_classifier, LREG_grid, cv=10)
    
    gridsearchLREG.fit(counts_train,labels_train)
    
    predicted=gridsearchLREG.predict(counts_test)
    
    print('Accuracy for LogisticRegression')
    print (accuracy_score(predicted,labels_test))
    print(' ')
    #=======================================================================================
    
    VT.fit(counts_train,labels_train)
    
    predicted=VT.predict(counts_test)
    
    print('Accuracy for GridSearch')
    print (accuracy_score(predicted,labels_test))
    print(' ')
    