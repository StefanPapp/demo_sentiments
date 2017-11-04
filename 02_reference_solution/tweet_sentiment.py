import json
import sys

def create_afinn_dictionary(sentfile):
    afinnfile = open(sentfile)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    return scores

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sc = create_afinn_dictionary(sys.argv[1])
    otxt = open(sys.argv[2])
    tweets = {} # initialize an empty dictionary

    for line in otxt:
        counter = 0
        tweet = json.loads(line) # Convert the score to an integer.
        
        if 'text' in tweet:
            wordlist = tweet['text'].split()
            for x in wordlist: 
                if x in sc:
                    counter = counter + sc[x]
           # print tweet['text']
        print(counter)
     

if __name__ == '__main__':
    main()
