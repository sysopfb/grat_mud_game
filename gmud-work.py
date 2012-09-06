'''
Sept62012
The code takes awhile to tag all the words. Just showing how to tag words though.
'''

import pickle



pfile = open("brown/categories.pickle")
data = pickle.load(pfile)
pfile.close()
corpus_filenames = [x[0] for x in data]
#Debug line
#print corpus_filenames


def create_yes_no( line, topic ):
    """Creates a yes/no question from the sentences passed, returns string."""
    
    topic = topic.lower()
    
    #prepare the line by making everything lowercase for easy matching
    # Also split up the sentence by commas
    #lower_line_split = line.lower().split(", ")
    line_split = line.split(", ")
    
    #List to hold our tagged words
    tagged_line = []
    #Loop to call find tag and build our list
    for ln in line_split:
        for word in ln.split(" "):
            tag = find_tag(word)
            tagged_line.append((word, tag))
    return tagged_line
    #for ln in line_split:
        
        #Something is happening to the topic at hand
        #if topic in ln:
            #Try to figure out what it is
            #tags = pos_tagger(ln)
            
        #See if the string begins with someones name, if it is assume an action has happened
        #for word in ln.split(" ")[:3]:
        #    if check_if_name(word):
        #        return ln.rstrip(".?!") + "!" + '\n' + "Would you like to continue?"

def find_tag(wordToFind):
    for fn in corpus_filenames:
        try:
            fp = open("brown/" + fn)
        except IOError:
            continue
        for line in fp:
            for word in line.split(" "):
                data = word.split("/")
                if data[0] == wordToFind:
                    fp.close()
                    return data[1]
                    
        fp.close()
    return 'NIL'
                
                
            
            
def pos_tagger( ln ):
    #Tags are NN(Noun), VB(Verb), JJ(Adjective), AT(Article)
    pass
    
def check_if_name( word ):
    return False


def main():
    #test line
    line = "When, in 355, Claudius Silvanus revolted against Emperor Constantius II in Gaul, Ursicinus was sent to him with a letter of recall by Constantius."
    
    print create_yes_no(line, "test")
    
main()
