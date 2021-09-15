import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    file_name = None
    while file_name == None:
        try:
            file_name = input("Enter the name of the file: ").strip()
            f=open(file_name)
            f.close()
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name = None

    return open(file_name)
    
   

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    rawSentences = fp.read().lower().splitlines()
    numSentences = len(rawSentences)
    newSentences = []
    words = []
    dictionary = {}
    
    words = process_lines(rawSentences)
    for x in range(numSentences):
        for y in words[x]:
            if is_word(y):
                    if y not in dictionary:
                        dictionary.update({y: {x+1}})
                    else:
                        dictionary[y].add(x+1)
    return dictionary
    

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    newSet = set()
    returnList = []
    newWords = []
    newWord = ''
    query = query.strip()
    if len(query) == 0:
        return ['not exist', '']
    else:
        words = query.lower().strip().split()
        newWords = remove_punctuation(words)
        for x in newWords:
            if x not in D:
                return ['not exist', x]
            else:
                newSet = D[x]
        for x in newWords:
                if x in D:
                    newSet = newSet.intersection(D[x])
        returnList = list(newSet)
        returnList.sort()
        return returnList
    
def remove_punctuation(words):
    ''' (list) -> list
        takes list of sentences and returns the list of sentences with the punctuation removed'''
    newSentences = []
    for x in range(len(words)):
       newSentences.append('') 
    for x in range(len(words)):
        for y in words[x]:
            if y not in string.punctuation:
                newSentences[x] = newSentences[x] + y
    return newSentences


def is_word(word):
    ''' (str) -> bool
        returns True is the length of the string is greater than 1 and if it only contains letters'''
    if len(word) >=2:
        if word.isalpha():
            return True
    return False

def process_lines(words):
    ''' (list) -> list
        returs a list of words that come from splitting the sentences and removing punctuation'''
    wordsL = []
    newSentences = []
    for x in range(len(words)):
        wordsL.append({})
    newSentences = remove_punctuation(words)
    for x in range(len(words)):
        wordsL[x] = newSentences[x].split()
    return wordsL
                
##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
while query != 'q':
    LineList = find_coexistance(d, query)
    if len(LineList) == 0:
        print("The words you entered do not coexist in a same line of the file.")
    elif LineList[0] != 'not exist':
        print("The one or more words you entered coexisted in the following lines of the file:")
        for x in LineList:
            print(x, end = ' ')
        print('')
    else:
        print("The word: '" + LineList[1] + "' not in the file")
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE

