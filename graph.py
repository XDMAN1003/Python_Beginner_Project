# This is our Markov Chain representation
import random
import string
import pprint
import re
import lyricsgenius


# Define the graph in terms of vertices

class Vertex:
    def __init__(self,value): # value will be the word
        self.value = value
        self.adjacent = {} # nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []


    def add_edge_to(self,vertex,weight = 0):
        # this is adding an edge to the vertex we input with weight
        self.adjacent[vertex] = weight

    def increment_edge(self,vertex):
        # this is incrementing the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex,0)+1

    def get_probability_map(self):
        for (vertex,weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)


    def next_word(self):
        # randomly select next work  **Based on the weights!!
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]


# Now that we have our vertex representation
class Graph:
    def __init__(self):
        self.vertices = {} # map string to Vertex

    def get_vertex(self,value):
        # what are the values o all the vertices?
        # in other words, return all possible words
        return set(self.vertices.keys())

    def add_vertex(self,value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self,value):
        # what if the value isnt in the graph?
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]
        #Get the vertex object

    def get_next_word(self, current_vertex):
       return self.vertices[current_vertex.value].next_word()

    def generate_probability_mapping(self):
       for vertex in self.vertices.values():
           vertex.get_probability_map()

# Get the word from the text

def get_words_from_text(text_path):
    with open(text_path,'rb') as f:
        text = f.read().decode("utf-8")
        # print(text)
        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        text = re.sub(r'\[(.+)\]', ' ', text)

        # Turn whitespace into space
        text = ' '.join(text.split())
        # Lower the text (Easy to compare text)
        text = text.lower()
        # Remove all punctuation
        text = text.translate(str.maketrans("","",string.punctuation))
    words = text.split() #split on space again
    return words

def make_graph(words):
    g = Graph()
    previous_word = None

    # for each word
    for word in words:
    # check that word is in the graph, and if not then add it
        word_vertex = g.get_vertex(word)
    # if there was a previous word -> add edge if it does not already exixts in the graph
        if previous_word:
            previous_word.increment_edge(word_vertex)
    # increase the weight by 1
    # set our word to the previous word and iterate!
        previous_word = word_vertex
    # now remember that we want to generate the probability mapping b4 composing
    # Great place to do it b4 return to the graph object
    g.generate_probability_mapping()

    return g

def compose(g,words,length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # Pick a random word to start
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

def main(song):
    # Step 1: Get word from text
    words = []
    words.extend(get_words_from_text('{song}.txt'.format(song=song)))
    # Step 2: Make a graph using those word
    g = make_graph(words)
    # Step 3: Get the next word for x number of words (defined by user)
    # Step 4: Show the user!
    composition = compose(g,words,100)
    # Return a string, where all the words are separate by a space
    return ' '.join(composition)

if __name__ == '__main__':
    singer = input("Enter your favourite singer: ")
    song_title = input("Enter a song you like: ")
    # generate an api key and paste it
    # https://genius.com/api-clients
    genius = lyricsgenius.Genius("In-ao9lQbqI_mxuSesOwrb309ssdS_dECNAtD3NC9nZ5apOnXfQivoDqjqwqqz2BLqT5jYjKUc2ZAmzCsHD4Jg")
    song = genius.search_song(song_title, singer)
    lyrics = song.lyrics
    with open('{}.txt'.format(' '.join(''.join(song_title.split('\'')).split(' '))), 'w',
              encoding="utf-8") as f:
        f.writelines(lyrics.split('\\n'))
    print("\nMarkov Chain Composer")
    text = main(song_title)
    li = list(text.split(" "))
    for i in range(0, len(li), 6):
        print(" ".join(li[i:i + 6]))





