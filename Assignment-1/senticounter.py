
#Name: Megh YOgeshkumar Vankawal 
#CWID:10421684
#BIA-660-WS 
#Assignment: Sentiment Counter

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()
    return newLex

def run(path):
    #load the positive lexicon
    posLex=loadLexicon('positive-words.txt')
    freq = {}
    fin=open(path)
    for line in fin: 
        words=line.lower().strip().split(' ')   
        for word in words: #for every word in the review
            if word in posLex:
                freq.setdefault(word,0)  
                freq[word] = freq[word] + 1  
                break
    fin.close()
    return freq

if __name__ == "__main__": 
    senticounter=run('textfile')
    for word in senticounter:
        print(word,"appears in",senticounter.get(word),"reviews.")