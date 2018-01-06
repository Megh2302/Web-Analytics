#Megh Yogeshkumar Vankawala
#CWID:10421684
#Assignment:Scraper.py

from bs4 import BeautifulSoup
import re
import time
import requests

def getCritic(review):
            critic='NA' 
            criticChunk=review.find('a',{'href':re.compile('/critic/')})
            if criticChunk: critic=criticChunk.text
            return critic

def getRating(review):
    ratings='NA'
    ratingsChunk=review.find('div',{'class':'review_icon icon small rotten'})
    if ratingsChunk: ratings='rotten'
    ratingsChunk=review.find('div',{'class':'review_icon icon small fresh'}) 
    if ratingsChunk: ratings='fresh'
    return ratings

def getSource(review):
    source='NA'
    sourceChunk=review.find('em',{'class':'subtle'})
    if sourceChunk: source=sourceChunk.text
    return source

def getDate(review):
    date='NA'
    dateChunk=review.find('div',{'class':'review_date subtle small'})
    if dateChunk: date=dateChunk.text
    return date

def getTextLen(review):
    textlen='NA'
    textlenChunk=review.find('div',{'class':'the_review'})
    if textlenChunk: textlen=len(textlenChunk.text)
    return textlen

def run(url):

    pageNum=1 # number of pages to collect
    fw=open('reviews.txt','w')
    for p in range(1,pageNum+1): # for each page 

        
        html=None

        if p==1: pageLink=url # url for page 1
        else: pageLink=url+'?page='+str(p)+'&sort=' # make the page url
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 

        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs
        
        for review in reviews:
            x=str(getCritic(review))
            print("Critic: "+x)
            y=str(getRating(review))
            print("Ratings: "+y)
            z=str(getSource(review))
            print("Source: "+z)
            a=str(getDate(review))
            print("Date:"+a)
            b=str(getTextLen(review))
            print("Length of Review: "+b)
            print(" ")
            
            
            fw.write("Critic: "+x+'\n'+"Ratings: "+y+'\n'+"Source: "+z+'\n'+"Date:"+a+'\n'+"Length of Review: "+b+'\n'+'\n') 
		
    fw.close()

            
if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    run(url)

