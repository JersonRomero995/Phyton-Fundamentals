# Static and Instance Methods
class WordSet:
    def __init__(self):
        self.words = set()
    
    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(text):
        #chaining functions
        text = text.replace('!','').replace('.','').replace(',','').replace('\'','')
        return text.lower()
    
wordSet = WordSet()
wordSet.addText('Hi, I\'m Ryan! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)


class WordSet:
    replacePuncs = ['!', '.', ',', '\'']
    def __init__(self):
        self.words = set()
        
    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)
            
        
    def cleanText(text):
        # chaining functions
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, '')
        return text.lower()
    
        
wordSet = WordSet()

wordSet.addText('Hi, I\'m Ryan! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)

#Decorators

class WordSet:
    replacePuncs = ['!', '.', ',', '\'']
    def __init__(self):
        self.words = set()
        
    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)


    @staticmethod
    def cleanText(text):
        #chaining functions
        for punc in wordSet.replacePuncs:
            text = text.replace(punc, '')
            return text.lower()

wordSet = WordSet()

wordSet.addText('Hi, I\'m Ryan! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)

# Instance Methods (Normal Methods)
python

def addText(self, text):
    text = WordSet.cleanText(text)
    for word in text.split():
        self.words.add(word)
# addText is an instance method because:

#It has self as the first parameter
#It can access instance attributes like self.words
#It needs to be called on an object: wordSet.addText(...)

#Static Methods
python

def cleanText(text):  # No self parameter!
    for punc in WordSet.replacePuncs:
        text = text.replace(punc, '')
    return text.lower()
# cleanText is being used as a static method because:

#It doesn't have self as a parameter
#It doesn't need access to any instance data
#It's just a utility function that happens to live in the class
#Notice it's called with the class name: WordSet.cleanText(text)

#The @staticmethod Decorator
#In the third version, the code properly uses the decorator:
python

@staticmethod
def cleanText(text):
    for punc in wordSet.replacePuncs:  # Note: there's a bug here
        text = text.replace(punc, '')
        return text.lower()
#The @staticmethod decorator tells Python "this method doesn't need self." Without it, you'd get an error when calling the method because Python would try to automatically pass self.
#Benefits of using @staticmethod:

#Makes your intent clear
#Can call it from either the class (WordSet.cleanText(...)) or an instance (self.cleanText(...))
#Doesn't receive the instance automatically

#When to use static methods:

#The function logically belongs to the class but doesn't need instance data
#It's a utility function related to the class's purpose
#You want to organize related functions together

#Bug to note: In the decorator version, there's actually a mistake - it uses wordSet.replacePuncs (a specific instance) instead of WordSet.replacePuncs (the class). It should be WordSet.replacePuncs to access the class attribute properly.
#The key distinction: instance methods work with specific object data (self), while static methods are just organized within the class but don't need access to instance-specific information.