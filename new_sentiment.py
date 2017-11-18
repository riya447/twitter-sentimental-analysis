from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from Tkinter import *

train = [
    
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ("My boss is horrible.", "neg"),
    ("I am in love.", "pos") 
    ]
new_data = [
    ('i hate this place!', 'neg'),
    ('i am angry', 'neg'),
    ('filled with sorrow', 'neg'),
    ('it is so ugly', 'neg'),
    ('burning like hell', 'neg'),
    ("1 2 3 4 5 6 7 8 9 0", "error"),
    ('fine', 'pos'),
    ('i hate you', 'neg'),
    ('i love it', 'pos')
    ]

    

    
 
cl = NaiveBayesClassifier(train)
cl.classify("I feel amazing!")
cl.update(new_data)
cl.accuracy(new_data)


master = Tk()
e = Entry(master)
e.pack()

e.focus_set()

def callback():
    #print e.get() # This is the text you may want to use later
    'pos'
    blob = TextBlob(e.get(), classifier=cl)
    for s in blob.sentences:
        print(s)
        print(s.classify())
        print(s.sentiment)

b = Button(master, text = "OK", width = 10, command = callback)
b.pack()

mainloop()



