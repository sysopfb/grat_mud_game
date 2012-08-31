from helpers import *
from grat.grat import parser

def get_topic():
    """Get the topic the user wishes the game to be about."""
    pass


def create_url(topic):
    """Find a wikipedia page that is close to user's topic. ( usually going
    to be http://en.wikipedia.org/wiki/ + user's topic."""
    pass


def is_wiki( content ):
    """Test if the user's topic is a wikipedia article by checking if content
    contains the sentence 'http://en.wikipedia.org/wiki/' + topic or 
    'There were no results matching the query.' """
    pass


def topic_died( line ):
    """Checks if line contains any variant of the word death and returns True 
    if found, false otherwise."""
    pass

def create_yes_no( line ):
    """Creates a yes/no question from the sentences passed, returns string."""
    pass

def main():
    topic = get_topic()
    url = create_url(topic)
    webpage = parser.Page(url)
    if ( is_wiki(webpage) == False):
        print "We are sorry, the topic you have choosen is not a wikipedia article."

    sentences = webpage.find_all_sentences(True) # Yet to be implemented, true
                                                 # indicates to include anchors
    print create_intro(sentences)
    index = 0
    while True:
        if index - 1 >= len(sentences):
            break

        if topic_died( sentences[index] ):
            print "You Win, well sorta..."
            break

        question = create_yes_no( sentences[index] )
        while True:
            answer = raw_input(question).lower()
            if answer == 'y' or answer == 'n':
                break

        if answer == 'y':
            print "Good Choice"

        if answer == 'n':
            print "Too bad"

if __name__ == "__main__":
    main()