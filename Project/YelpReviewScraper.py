from bs4 import BeautifulSoup
import re
import time
import requests
from fake_useragent import UserAgent
import os



def run(city):
    ex = 0
    if not os.path.exists(city):
        os.mkdir(city)
    
    
    url='https://www.yelp.com/search?find_loc='+city+'&cflt=restaurants&start='
    ua=UserAgent()
    resCount = 0
    pageNum=100 # number of pages to collect

    fw=open('yelpReviews'+city+'.txt','w') # output file
	
    for p in range(0,pageNum): # for each page 

        print ('page',p+1)
        html=None
        pageLink = url+str(p*10)
    
        print(pageLink)
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': ua.random, })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(0.5) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 

        restaurantList=soup.findAll('div', 
                    {'class':re.compile('natural-search-result')}) # get all the review divs
        
        for restaurant in restaurantList:
            
            restaurantName,noOfReviews,reviewURL,area='NA','NA','NA','NA' # initialize critic and text 
            
            restaurantChunk=restaurant.find('span',{'class':None})
            if restaurantChunk:
                restaurantName=restaurantChunk.text#.encode('ascii','ignore')
                
            noOfReviewsChunk=restaurant.find('span',{'class':re.compile('review-count')})
            if noOfReviewsChunk: 
                noOfReviews=noOfReviewsChunk.text#.encode('ascii','ignore')

            reviewURLChunk=restaurant.find('a',{'href':re.compile('/biz/')})
            if reviewURLChunk:
                reviewURL=reviewURLChunk['href']
            
            areaChunk=restaurant.find('span',{'class':'neighborhood-str-list'})
            if areaChunk:
                area=areaChunk.text.strip()
            if noOfReviews == 'NA':
                continue
            if int(re.sub(' +',' ',noOfReviews.strip()).split(' ')[0]) >= 30:
                
                time.sleep(0.5)
                reviewLink = 'https://www.yelp.com'+reviewURL
		
                for j in range(5): # try 5 times
                    try:
                #use the browser to access the url
                        responseR=requests.get(reviewLink,headers = { 'User-Agent': ua.random, })
                        htmlR=responseR.content # get the html
                        break # we got the file, break the loop
                    except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                        print ('failed attempt',j)
                        time.sleep(0.5) # wait 2 secs
                    
                if not htmlR:continue # couldnt get the page, ignore
                    
                soupR = BeautifulSoup(htmlR.decode('ascii', 'ignore'),'lxml')
                
                tt_reviews = soupR.find('div',{'class':re.compile('js-review-feed-language')})
                t_reviews = tt_reviews.find('span',{'class':re.compile('js-dropdown-toggle-text')});
                t1_reviews = t_reviews.text.strip().split(' ')
                x1 = t1_reviews[0]
                x2 = int(t1_reviews[1][1:len(t1_reviews[1])-1])
                
                if x1 != 'English' or x2 < 30:
                    continue
                
                newDir = city+'/'+restaurantName.strip()
                
                if not os.path.exists(newDir):
                    os.mkdir(newDir)
                else:
                    ex = ex + 1
                    newDir = city+'/'+restaurantName.strip()+str(ex)
                    os.mkdir(newDir)
                fwr=open(os.path.join(newDir,restaurantName.strip()+'_review1.html'),'w')
                fwr.write(str(soupR))
                fwr.close()
                
                
                reviews=soupR.findAll('div', 
                                          {'class':re.compile('review-content')})
                fw.write(restaurantName.strip()+'\t'+area+'\t'+city)
                for review in reviews:

                    text='NA' # initialize critic and text 
                    
                    textChunk=review.find('p',{'lang':'en'})
                    if textChunk: text=textChunk.text#.encode('ascii','ignore')	
                    
                    fw.write('\t'+text.strip())
                
                reviewLink = reviewLink +'?start=20'
                time.sleep(1)
		
                for j in range(5): # try 5 times
                    try:
                #use the browser to access the url
                        responseR=requests.get(reviewLink,headers = { 'User-Agent': ua.random, })
                        htmlR=responseR.content # get the html
                        break # we got the file, break the loop
                    except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                        print ('failed attempt',j)
                        time.sleep(1) # wait 2 secs
                    
                if not htmlR:continue # couldnt get the page, ignore
                    
                soupR = BeautifulSoup(htmlR.decode('ascii', 'ignore'),'lxml')
                
                #f = open(os.path.join(OUTPUT_DIR, 'file.txt'), 'w')
                fwr=open(os.path.join(newDir,restaurantName.strip()+'_review2.html'),'w')
                fwr.write(str(soupR))
                fwr.close()
                
                reviews=soupR.findAll('div', 
                                          {'class':re.compile('review-content')})
                revCount = 0
                for review in reviews:
                    revCount = revCount +1
                    text='NA' # initialize critic and text 
                    
                    textChunk=review.find('p',{'lang':'en'})
                    if textChunk: text=textChunk.text#.encode('ascii','ignore')	
                    
                    fw.write('\t'+text.strip())
                    if revCount == 10: break
                
                businessInfo = soupR.findAll('div', 
                                          {'class':'short-def-list'})
            
                infos = businessInfo[0].findAll('dl')
                for info in infos:
                    business,result = 'NA','NA'
                    
                    businessChunk = info.find('dt')
                    if businessChunk: business = businessChunk.text.strip()
                    
                    resultChunk = info.find('dd')
                    if resultChunk: result = resultChunk.text.strip()
                    
                    busiInfo = business+':'+result
                    
                    fw.write('\t'+str(busiInfo))
                
                fw.write('\n')
                resCount = resCount +1
                print('No of restaurant reviewed:'+str(resCount))
                if resCount == 1000: break
            
             
		
        time.sleep(1)	# wait 1 sec 
        if resCount == 1000: break

    fw.close()

if __name__=='__main__':
    city='London'
    run(city)
    city='Paris'
    run(city)
    city='Berlin'
    run(city)
    city='Manchester'
    run(city)



