def preRun():
    fin1=open('yelpReviewsLondon.txt')
    fin2=open('yelpReviewsBerlin.txt')
    fin3=open('yelpReviewsParis.txt')
    fin4=open('yelpReviewsManchester.txt')
    fw=open('yelpReviewsAll.txt','w')
    
    for line in fin1:
        fw.write(line)
    for line in fin2:
        fw.write(line)
    for line in fin3:
        fw.write(line)
    for line in fin4:
        fw.write(line)
    
    fin1.close()
    fin2.close()
    fin3.close()
    fin4.close()
    fw.close()
    
def run():
    
    fin=open('yelpReviewsAll.txt')
    fw1=open('train_review_All.txt','w')
    fw2=open('test_review_All.txt','w')
    
    lineNo = 0
    
    for line in fin:
        lineNo = lineNo +1
        
        dataAll =line.lower().strip().split('\t')
        reviews = []
        goodForKids = 0
        goodForGroups = 0
        isWiFi = 1
        parking = 0
        outdoorSeating = 0
        x = len(dataAll)
        
        
        
        if x < 33 :
            lineNo = lineNo-1
            continue
        if len(dataAll[32]) < 50:
            lineNo = lineNo-1
            continue
        for i in range(33,x):
            data = dataAll[i].split(':')
            if data[0] == 'good for kids':
                if data[1] == 'yes':
                    goodForKids = 1
            if data[0] == 'wi-fi':
                if data[1] == 'no':
                    isWiFi = 0
            if data[0] == 'good for groups':
                if data[1] == 'yes':
                    goodForGroups = 1
            if data[0] == 'parking':
                if data[1].find('private lot') >= 0:
                    parking = 1
                elif data[1].find('garage') >= 0:
                    parking = 1
                elif data[1].find('valet') >= 0:
                    parking = 1
            if data[0] == 'outdoor seating':
                if data[1] == 'yes':
                    outdoorSeating = 1
    
        for i in range(3,33):
            reviews.append(dataAll[i])
        
               
        
        megaReview = ''
        for i in range(0,30):
            megaReview = megaReview + ' ' + reviews[i]
        
        if lineNo%10 < 8:
            
            fw1.write(megaReview+'\t'+str(goodForKids)
                                    +'\t'+str(isWiFi)
                                    +'\t'+str(goodForGroups)
                                    +'\t'+str(parking)
                                    +'\t'+str(outdoorSeating)+'\n')    
            
            
            
        else:
            fw2.write(megaReview+'\t'+str(goodForKids)
                                    +'\t'+str(isWiFi)
                                    +'\t'+str(goodForGroups)
                                    +'\t'+str(parking)
                                    +'\t'+str(outdoorSeating)+'\n')
            
    print('Total reviews:'+str(lineNo))    
    fin.close()
    fw1.close()
    fw2.close()
 

if __name__ == "__main__":
    preRun()
    run()