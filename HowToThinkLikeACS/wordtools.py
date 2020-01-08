LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]


def replace_special_chars(s, to_rep=''):
    """
    Replace all special characters from string s.
    """
    
    # Change string to lowercase.
    lowered = s.lower()
    
    # Make list with all special characters in s.
    specials = [spec for spec in lowered if spec not in LETTERS]
    
    # Replace all special characters with to_rep.
    for special in specials:
        lowered = lowered.replace(special, to_rep)
    return lowered


def cleanword(s):
    """
    Remove all non-letter characters from a singe-word string.
    """
    return replace_special_chars(s, to_rep='')


def has_dashdash(s):
    """
    Return whether the string s contains two dashes.
    """
    return '--' in s


def extract_words(s):
    """
    Return a list with only the words in the string s.
    """
    # Replace special characters with a blank space.
    aux = replace_special_chars(s, to_rep=' ')
    
    return aux.split()
    

def wordcount(word, word_list):
    """
    Count the number of instances of word in the list word_list.
    """
    counter = 0
    for w in word_list:
        if word == w:
            counter += 1
    return counter


def wordset(word_list):
    """
    Return unique instances of each word.
    """
    resut = list(set(word_list))
    resut.sort()
    return resut


def longestword(word_list):
    """
    Return maximum number of letters in word_list.
    """
    max_word = 0
    for word in word_list:
        aux_len = len(word)
        if aux_len > max_word:
            max_word = aux_len
    return max_word
