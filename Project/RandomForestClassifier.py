"""
Megh Vankawala, Maulik Jajal, Rimaben Patel, Akriti Srivastava, Divyesh Thakkar
RandomForestClassifier for all business Info such as: Good for Kids, Good for Groups,
Wifi, Parking Availablity , Outdoor seating Availablity  

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


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
clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Run 1')
print ('Results CountVectorizer Good For Kids', res)
fw.write('Run 1 Using CountVectorizer and RandomForestClassifier with n_estimators=1400 for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results CountVectorizer Wifi',res)
fw.write('Run 1 Using CountVectorizer and RandomForestClassifier with n_estimators=1400 for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results CountVectorizer Good for Group',res)
fw.write('Run 1 Using CountVectorizer and RandomForestClassifier with n_estimators=1400 for GoodGrp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results CountVectorizer Parking Avaliable',res)
fw.write('Run 1 Using CountVectorizer and RandomForestClassifier with n_estimators=1400 for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results CountVectorizer Good for OutDoorSeating',res)
fw.write('Run 1 Using CountVectorizer and RandomForestClassifier with n_estimators=1400 for OutDoor, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")

## Next Run 2
print ('Run 2')
counter = CountVectorizer()
counter.fit(rev_train)


#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data

#open results file
#train classifier
clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Results CountVectorizer Good For Kids', res)
fw.write('Run 2 Using CountVectorizer and RandomForestClassifier with n_estimators=1550 for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results CountVectorizer Wifi',res)
fw.write('Run 2 Using CountVectorizer and RandomForestClassifier with n_estimators=1550 for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results CountVectorizer  Good for Group',res)
fw.write('Run 2 Using CountVectorizer and RandomForestClassifier with n_estimators=1550 for GoodGrp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results CountVectorizer Parking Avaliable',res)
fw.write('Run 2 Using CountVectorizer and RandomForestClassifier with n_estimators=1550 for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results CountVectorizer Good for OutDoorSeating',res)
fw.write('Run 2 Using CountVectorizer and RandomForestClassifier with n_estimators=1550 for OutDoor, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")

## Next Run 3
print ('Run 3')
counter = TfidfVectorizer()
counter.fit(rev_train)
#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data


#train classifier
clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Results TfidfVectorizer with no parameter Good For Kids', res)
fw.write('Run 3 Using TfidfVectorizer and RandomForestClassifier with n_estimators=1400  for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results TfidfVectorizer with no parameter Wifi',res)
fw.write('Run 3 Using TfidfVectorizer and RandomForestClassifier with n_estimators=1400 for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results TfidfVectorizer with no parameter Good for Group',res)
fw.write('Run 3 Using TfidfVectorizer and RandomForestClassifier with n_estimators=1400 for Good for Grp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results TfidfVectorizer with no parameter Parking Avaliable ',res)
fw.write('Run 3 Using TfidfVectorizer and RandomForestClassifier with n_estimators=1400 for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1400, criterion='entropy',max_features='log2', oob_score=True,max_depth=5000,min_samples_split=162,random_state=150, n_jobs=8)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results TfidfVectorizer with no parameter Good for OutDoorSeating',res)
fw.write('Run 3  Using TfidfVectorizer and RandomForestClassifier with n_estimators=1400 for OutDoor Seating, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")


#####-Next Run 4
print ('Run 4')
counter = TfidfVectorizer()
counter.fit(rev_train)
#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data


#train classifier
clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Results TfidfVectorizer with no parameter Good For Kids', res)
fw.write('Run 4 Using TfidfVectorizer and RandomForestClassifier with n_estimators=1550 for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results TfidfVectorizer with no parameter  Wifi',res)
fw.write('Run 4 Using TfidfVectorizer and RandomForestClassifier with n_estimators=1550 for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results TfidfVectorizer with no parameter Good for Group',res)
fw.write('Run 4 Using TfidfVectorizer and RandomForestClassifier with n_estimators=1550 for Good for Grp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results TfidfVectorizer with no parameter Parking Avaliable',res)
fw.write('Run 4 Using TfidfVectorizer and RandomForestClassifier with n_estimators=1550 for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_features='auto', oob_score=False, n_jobs=1, max_depth=5000,min_samples_split=162,random_state=None)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results TfidfVectorizer with no parameter Good for OutDoorSeating',res)
fw.write('Run 4 Using TfidfVectorizer and RandomForestClassifier with n_estimators=1550 for OutDoor Seating, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")

## Next Run 5
print ('Run 5')
counter = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', ngram_range=(4,5),stop_words='english')
counter.fit(rev_train)
#count the number of times each term appears in a document and transform each doc into a count vector
counts_train = counter.transform(rev_train)#transform the training data
counts_test = counter.transform(rev_test)#transform the testing data


#train classifier
clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_depth=None,min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False,class_weight=None)
clf.fit(counts_train,goodKids_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodKids_test)
print ('Results TfidfVectorizer Range 4 to 5 Good For Kids', res)
fw.write('Run 5 Using TfidfVectorizer and Range 4 to 5 RandomForestClassifier with all parameter for Good For Kids, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_depth=None,min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False,class_weight=None)
clf.fit(counts_train,wifi_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,wifi_test)
print ('Results TfidfVectorizer Range 4 to 5  Wifi',res)
fw.write('Run 5 Using TfidfVectorizer Range 4 to 5 and RandomForestClassifier with all parameter for Wifi, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_depth=None,min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False,class_weight=None)
clf.fit(counts_train,goodGrp_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,goodGrp_test)
print ('Results TfidfVectorizer Range 4 to 5 Good for Group',res)
fw.write('Run 5 Using TfidfVectorizer Range 4 to 5 and RandomForestClassifier with all parameter for Good for Grp, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_depth=None,min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False,class_weight=None)
clf.fit(counts_train,parkAvail_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,parkAvail_test)
print ('Results TfidfVectorizer Range 4 to 5 Parking Avaliable',res)
fw.write('Run 5 Using TfidfVectorizer Range 4 to 5 and RandomForestClassifier with all parameter for Parking Avaliable, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")

clf = RandomForestClassifier(n_estimators=1550, criterion='gini', max_depth=None,min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False,class_weight=None)
clf.fit(counts_train,outdoor_train)
pred=clf.predict(counts_test)
res = accuracy_score(pred,outdoor_test)
print ('Results TfidfVectorizer Range 4 to 5 Good for OutDoorSeating',res)
fw.write('Run 5 Using TfidfVectorizer Range 4 to 5 and RandomForestClassifier with all parameter for OutDoor Seating, results are: '+ str(res) +' \n') # write to file 
fw.write("------\n")
fw.write("------\n")

fw.close()




