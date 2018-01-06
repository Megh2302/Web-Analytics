import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load

# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms

def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
   
    for line in lex_conn:
        newLex.add(line.strip())
    lex_conn.close()

    return newLex

def processSentence(sentence,posLex,negLex,tagger,c):
    
    POStags=['NN','RB']
    POSterms=getPOSterms(sentence,POStags,tagger)
    nouns = POSterms['NN']
    adverbs = POSterms['RB']
    
    solution = []
    
    fiveGrams = ngrams(sentence, 5) 
    for tag in fiveGrams: 
        if tag[0] == 'not' and tag[2] in adverbs and (tag[3] in posLex or tag[3] in negLex) and (tag[4] in nouns and c in tag[4]): # checking for the condition 
            solution.append(tag)
    
    fourGrams = ngrams(sentence, 4)        
    for tag in fourGrams: 
        if tag[0] == 'not' and (tag[2] in posLex or tag[2] in negLex) and (tag[3] in nouns and c in tag[3]): # checking for the condition 
            solution.append(tag)
    
    return solution

def run(fpath):

    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)
    output=[]
    posLex=loadLexicon('positive-words.txt')
    negLex=loadLexicon('negative-words.txt')

    # for each sentence
    for sentence in sentences:

        sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
        sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces
        terms = nltk.word_tokenize(sentence.lower())
        c='e'
        output+=processSentence(terms,posLex,negLex,tagger,c)
		
    return output
 

if __name__=='__main__':
    print (run('input.txt'))



