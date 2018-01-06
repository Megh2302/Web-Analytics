
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import ExtraTreeClassifier


#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labelParkAvail=[]
    labelWifi=[]
    labelgoodGrp=[]
    labelgoodKids=[]
    labelOutDoorSeating=[]
    f=open(fname)
    for line in f:
        review,goodKids,wifi,goodGrp,parkAvail,outDoorSeating=line.strip().split('\t')  
        reviews.append(review.lower())    
        labelgoodKids.append(int(goodKids))
        labelWifi.append(int(wifi))
        labelgoodGrp.append(int(goodGrp))
        labelParkAvail.append(int(parkAvail))
        labelOutDoorSeating.append(int(outDoorSeating))
    f.close()
    return reviews,labelgoodKids,labelWifi,labelgoodGrp,labelParkAvail,labelOutDoorSeating

rev_train,goodKids_train,wifi_train,goodGrp_train,parkAvail_train,outdoor_train=loadData('train_review_All.txt')
rev_test,goodKids_test,wifi_test,goodGrp_test,parkAvail_test,outdoor_test=loadData('test_review_All.txt')


## Run 1
counter = CountVectorizer()
counter.fit(rev_train)


#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#open results file
fw=open('results.txt','w') # output file
#train classifier
clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Run 1')
print ('Results CountVectorizer Good For Kids', res)
fw.write('Run 1 Using CountVectorizer and MultinomialNB for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results CountVectorizer Wifi',res)
fw.write('Run 1 Using CountVectorizer and MultinomialNB for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results CountVectorizer Good for Group',res)
fw.write('Run 1 Using CountVectorizer and MultinomialNB for GoodGrp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results CountVectorizer Parking Avaliable',res)
fw.write('Run 1 Using CountVectorizer and MultinomialNB for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results CountVectorizer Good for OutDoorSeating',res)
fw.write('Run 1 Using CountVectorizer and MultinomialNB for OutDoor, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")


## Next Run 2
print ('Run 2')
counter = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', ngram_range=(1,5),stop_words='english')
counter.fit(rev_train)
#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data


#train classifier
clf = MultinomialNB(alpha=0.5, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Results TfidfVectorizer Good For Kids', res)
fw.write('Run 2 Using TfidfVectorizer and MultinomialNB for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=0.5, class_prior=None, fit_prior=True)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results TfidfVectorizer Wifi',res)
fw.write('Run 2 Using TfidfVectorizer and MultinomialNB for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=0.5, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results TfidfVectorizer Good for Group',res)
fw.write('Run 2 Using TfidfVectorizer and MultinomialNB for Good for Grp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=0.5, class_prior=None, fit_prior=True)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results TfidfVectorizer Parking Avaliable ',res)
fw.write('Run 2 Using TfidfVectorizer and MultinomialNB for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=0.5, class_prior=None, fit_prior=True)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results TfidfVectorizer Good for OutDoorSeating',res)
fw.write('Run 2  Using TfidfVectorizer and MultinomialNB for OutDoor Seating, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")
#####-Next Run 3
print ('Run 3')
counter = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', ngram_range=(4,5),stop_words='english')
counter.fit(rev_train)
#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data


#train classifier
clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Results TfidfVectorizer Range 4 to 5 Good For Kids', res)
fw.write('Run 3 Using TfidfVectorizer and Range 4 to 5 MultinomialNB for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results TfidfVectorizer Range 4 to 5  Wifi',res)
fw.write('Run 3 Using TfidfVectorizer Range 4 to 5 and MultinomialNB for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results TfidfVectorizer Range 4 to 5 Good for Group',res)
fw.write('Run 3 Using TfidfVectorizer Range 4 to 5 and MultinomialNB for Good for Grp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results TfidfVectorizer Range 4 to 5 Parking Avaliable',res)
fw.write('Run 3 Using TfidfVectorizer Range 4 to 5 and MultinomialNB for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results TfidfVectorizer Range 4 to 5 Good for OutDoorSeating',res)
fw.write('Run 3 Using TfidfVectorizer Range 4 to 5 and MultinomialNB for OutDoor Seating, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")

## Next Run 4
print ('Run 4')
counter = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', ngram_range=(1,2),stop_words='english')
counter.fit(rev_train)
#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data


#train classifier
clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Results TfidfVectorizer Range 1 to 2 Good For Kids', res)
fw.write('Run 4 Using TfidfVectorizer and Range 1 to 2 MultinomialNB for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results TfidfVectorizer Range 1 to 2  Wifi',res)
fw.write('Run 4 Using TfidfVectorizer Range 1 to 2 and MultinomialNB for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results TfidfVectorizer Range 1 to 2 Good for Group',res)
fw.write('Run 4 Using TfidfVectorizer Range 1 to 2 and MultinomialNB for Good for Grp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results TfidfVectorizer Range 1 to 2 Parking Avaliable',res)
fw.write('Run 4 Using TfidfVectorizer Range 1 to 2 and MultinomialNB for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results TfidfVectorizer Range 1 to 2 Good for OutDoorSeating',res)
fw.write('Run 4 Using TfidfVectorizer Range 1 to 2 and MultinomialNB for OutDoor Seating, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")
## Next Run 5
print ('Run 5')
counter = CountVectorizer()
counter.fit(rev_train)


#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#open results file
#train classifier
clf = MultinomialNB(alpha=2.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Results CountVectorizer Alpha 2 Good For Kids', res)
fw.write('Run 5 Using CountVectorizer and MultinomialNB for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=2.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results CountVectorizer Alpha 2 Wifi',res)
fw.write('Run 5 Using CountVectorizer and MultinomialNB Alpha 2 for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=2.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results CountVectorizer Alpha 2 Good for Group',res)
fw.write('Run 5 Using CountVectorizer and MultinomialNB Alpha 2 for GoodGrp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=2.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results CountVectorizer Alpha 2 Parking Avaliable',res)
fw.write('Run 5 Using CountVectorizer and MultinomialNB Alpha 2 for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = MultinomialNB(alpha=2.0, class_prior=None, fit_prior=True)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results CountVectorizer Alpha 2 Good for OutDoorSeating',res)
fw.write('Run 5 Using CountVectorizer and MultinomialNB Alpha 2 for OutDoor, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")

fw.close




