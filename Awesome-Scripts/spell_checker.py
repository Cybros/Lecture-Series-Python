import re                                   # regular expressions
from collections import Counter             # Counter dict

fh = open('big.txt', 'r').read()            # retrieves big.txt

def words(text):
    return re.findall(r'\w+', text)         # returns every possible word from the text


WORDS = Counter(words(fh))


def probability(word):                    # calculating probab of the word being used by user on the basis of no. of occurences of that word in the file
    N = sum( WORDS.values())
    return WORDS[word]*(1.0) / N          # no. of occurences of a word / total words in the file


def correction(word):
    print 'Did you mean:'
    print max( candidates(word), key=probability)          # returns most probable word from the list on the basis of the probablity calculated
    resp = raw_input('Enter no/yes to continue other suggestions-')
    if resp == 'no':
        return 'Stopped'
    elif resp == 'yes':
        print 'Suggestions :-'
    return sorted(list(candidates(word)), reverse=True)[:20]


# All known words of edit distance 1 are infinitely more probable than known words of edit distance 2,
# and infinitely less probable than a known word of edit distance 0.

def candidates(word):
    return valid([word]) or valid(edits1(word)) or valid(edits2(word)) or [word]


def valid(words):
    return set(w for w in words if w in WORDS)      # finds all valid words from the huge list of possible edits


def edits1(word):                                   # makes all possible edits of dist 1 in the word
    letters= 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:])          for i in range( len(word)+ 1)]          # splitting word
    deletes = [ L + R[1:]          for L, R in splits if R]                         # deleting every possible combination of the word
    transposes = [ L + R[1] + R[0] + R[2:]       for L, R in splits if len(R)>1]    # swaps every adjacent pair of letters
    replaces = [ L + c + R[1:]       for L, R in splits if R for c in letters]      # replaces every letter with letters
    inserts = [L + c + R       for L, R in splits for c in letters]                 # inserts at all possible places
    return set(deletes + transposes + replaces + inserts)                           # returns a list of all possible edits


def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))     #makes all possible edits of dist 2 in the word


para = raw_input('Enter your text:\n')
words = para.split()
string = ''
for word in words:
    string = correction( word.strip())

print string
