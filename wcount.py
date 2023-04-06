#####################
#   Word Counter    #
#####################

def word_count(s):
    correct_s = ''
    # for every character in the string, remove (if exist), every 
    # punctuation or numbers. Then save it in correct_s
    for c in s:
        if c not in '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~)1234567890':
            correct_s += c
    # split the string in a list using spaces as reference
    l = correct_s.lower().split(' ')
    words = {}
    # in an empty dictionary, add all the words as a key (if it's not in)
    # for every word is added (key), 1 is assigned as value.
    # if the word is already, one is added to the value.
    for i in l:
        # first if is in case user put more than 1 space
        if i != '':
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1
    
    return words