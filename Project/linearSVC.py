
#from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.svm import LinearSVC


#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    label1=[]
    label2=[]
    label3=[]
    label4=[]
    label5=[]
    #label2=[]
    f=open(fname)
    for line in f:
        review =line.strip().split('\t')  
        reviews.append(review[0].lower())    
        label1.append(int(review[1]))
        label2.append(int(review[2]))
        label3.append(int(review[3]))
        label4.append(int(review[4]))
        label5.append(int(review[5]))
    f.close()
    return reviews,label1, label2, label3, label4, label5
#label3, label4, label5

rev_train,label1_train, label2_train,label3_train,label4_train,label5_train =loadData('train_review_All.txt')
rev_test,label1_test, label2_test, label3_test, label4_test, label5_test =loadData('train_review_All.txt')


#Build a counter based on the training dataset

counter1 = TfidfVectorizer(stop_words=u'english',ngram_range=(2,3),lowercase=True)
counter1.fit(rev_train)
counter2 = TfidfVectorizer()
counter2.fit(rev_train)
counter3 = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', stop_words='english')
counter3.fit(rev_train)
counter4 = CountVectorizer(stop_words=u'english',ngram_range=(2,4),lowercase=True)
counter4.fit(rev_train)
counter5 = CountVectorizer()
counter5.fit(rev_train)


#count the number of times each term appears in a document and transform each doc into a count vector
counts_train1 = counter1.transform(rev_train)#transform the training data
counts_test1 = counter1.transform(rev_test)#transform the testing data

counts_train2 = counter2.transform(rev_train)#transform the training data
counts_test2 = counter2.transform(rev_test)

counts_train3 = counter3.transform(rev_train)#transform the training data
counts_test3 = counter3.transform(rev_test)

counts_train4 = counter4.transform(rev_train)#transform the training data
counts_test4 = counter4.transform(rev_test)

counts_train5 = counter5.transform(rev_train)#transform the training data
counts_test5 = counter5.transform(rev_test)



clf = LinearSVC()
clf.fit(counts_train1,label1_train)
pred1=clf.predict(counts_test1)

clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train2,label1_train)
pred2=clf.predict(counts_test2)

clf = LinearSVC(C=1.0, dual=True ,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train3,label1_train)
pred3=clf.predict(counts_test3)

clf = LinearSVC(penalty='l1', loss='squared_hinge', random_state=6, dual=False, tol=1e-3, intercept_scaling=5)
clf.fit(counts_train4,label1_train)
pred4=clf.predict(counts_test4)

clf = LinearSVC()
clf.fit(counts_train5,label1_train)
pred5=clf.predict(counts_test5)

#print accuracy
print "______________________Accuracy of goodforkids___________________________"
#fw.write("\n")
print "LinearSVC(goodforkids):      counter: Tfidfvectorization " 
print ('Accuracy:' + str(accuracy_score(pred1,label1_test)))

print "LinearSVC(goodforkids):      counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred2,label1_test))) 

print "LinearSVC(goodforkids):      counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred3,label1_test))) 

print "LinearSVC(goodforkids):      counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred4,label1_test))) 

print "LinearSVC(goodforkids):      counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred5,label1_test))) 


#is wifi
clf = LinearSVC()
clf.fit(counts_train1,label2_train)
pred6=clf.predict(counts_test1)

clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train2,label2_train)
pred7=clf.predict(counts_test2)

clf = LinearSVC(C=1.0, dual=True ,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train3,label2_train)
pred8=clf.predict(counts_test3)

clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1)
clf.fit(counts_train4,label2_train)
pred9=clf.predict(counts_test4)

clf = LinearSVC()
clf.fit(counts_train5,label2_train)
pred10=clf.predict(counts_test5)

print "________________________Accuracy for isWIFI______________________________"

print "LinearSVC(iswifi):        counter: Tfidfvectorization " 
print ('Accuracy:' +  str(accuracy_score(pred6,label2_test)))

print "LinearSVC(iswifi):        counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred7,label2_test))) 

print "LinearSVC(iswifi):        counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred8,label2_test))) 

print "LinearSVC(iswifi):        counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred9,label2_test))) 

print "LinearSVC(iswifi):        counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred10,label2_test))) 

#Good for groups
clf = LinearSVC()
clf.fit(counts_train1,label3_train)
pred11=clf.predict(counts_test1)

clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train2,label3_train)
pred12=clf.predict(counts_test2)

clf = LinearSVC(C=1.0, dual=True ,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train3,label3_train)
pred13=clf.predict(counts_test3)

clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1)
clf.fit(counts_train4,label3_train)
pred14=clf.predict(counts_test4)

clf = LinearSVC()
clf.fit(counts_train5,label3_train)
pred15=clf.predict(counts_test5)

#print accuracy
print "________________________Accuracy of goodforgroups_____________________"
print "LinearSVC(goodforgroups):        counter: Tfidfvectorization " 
print ('Accuracy:' +  str(accuracy_score(pred11,label3_test)))

print "LinearSVC(goodforgroups):        counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred12,label3_test))) 

print "LinearSVC(goodforgroups):        counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred13,label3_test))) 

print "LinearSVC(goodforgroups):        counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred14,label3_test))) 

print "LinearSVC(goodforgroups):        counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred15,label3_test))) 

     


#Good for parking
clf = LinearSVC()
clf.fit(counts_train1,label4_train)
pred16=clf.predict(counts_test1)

clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train2,label4_train)
pred17=clf.predict(counts_test2)

clf = LinearSVC(C=1.0, dual=True ,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train3,label4_train)
pred18=clf.predict(counts_test3)

clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1)
clf.fit(counts_train4,label4_train)
pred19=clf.predict(counts_test4)

clf = LinearSVC()
clf.fit(counts_train5,label4_train)
pred20=clf.predict(counts_test5)

#print accuracy
print "_______________________Accuracy of goodforparking______________________"
print "LinearSVC(goodforparking):       counter: Tfidfvectorization " 
print ('Accuracy:' +  str(accuracy_score(pred16,label4_test)))

print "LinearSVC(goodforparking):       counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred17,label4_test))) 

print "LinearSVC(goodforparking):       counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred18,label4_test))) 

print "LinearSVC(goodforparking):       counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred19,label4_test))) 

print "LinearSVC(goodforparking):       counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred20,label4_test))) 

#Good for outdoor seating
clf = LinearSVC()
clf.fit(counts_train1,label5_train)
pred21=clf.predict(counts_test1)

clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train2,label5_train)
pred22=clf.predict(counts_test2)

clf = LinearSVC(C=1.0, dual=True ,intercept_scaling=1, loss='hinge', max_iter=1000,multi_class='ovr', random_state=None, tol=0.0001,verbose=0)
clf.fit(counts_train3,label5_train)
pred23=clf.predict(counts_test3)

clf = LinearSVC(C=1.0, dual=True, fit_intercept=True,intercept_scaling=1)
clf.fit(counts_train4,label5_train)
pred24=clf.predict(counts_test4)

clf = LinearSVC()
clf.fit(counts_train5,label5_train)
pred25=clf.predict(counts_test5)



#print accuracy
print "_____________________Accuracy of goodforOutdoorSeating____________________"
print "LinearSVC(goodforOutdoorSeating):       counter: Tfidfvectorization " 
print ('Accuracy:' +  str(accuracy_score(pred21,label5_test)))

print "LinearSVC(goodforOutdoorSeating):        counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred22,label5_test))) 

print "LinearSVC(goodforOutdoorSeating):       counter: TfidfVectorization " 
print ("Accuracy:" + str(accuracy_score(pred23,label5_test))) 

print "LinearSVC(goodforOutdoorSeating):       counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred24,label5_test))) 

print "LinearSVC(goodforOutdoorSeating):       counter: countVectorization " 
print ("Accuracy:" + str(accuracy_score(pred25,label5_test))) 






