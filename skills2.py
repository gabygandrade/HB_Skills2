


#!/usr/bin/env python


"""Hackbright Skills 2: Python Data Structures.

There are a bunch of functions in this file that are not written, but
have documentation strings that explain how they should work. Your job
is to edit this file to write the bodies of these functions.

We expect that you will solve these problems using Python lists
and dictionaries. Some of these problems could be solved with Python
sets (a more advanced data type); if you've learned about sets, you
may use these here.

This file uses "doctests"; the explanation of how the functions should
work contains examples just like you'd see in the Python interpreter.
The examples are actually run and tested when this file is ran.

When you first run this test, it will show test failures for every
function--since the real functions haven't been written yet. As you
write the real functions, your test failure count will go down.

At the point where you've completed this skills assessment, the
only output from this program would be:

To begin: 17 Failures 

   ** ALL TESTS PASSED. GOOD WORK!

Good luck!

"""

def count_unique(string1):
    word_bank_list = string1.split()      # bind word_bank_list to a string made up of the elements in the input_string
    
    unique_words= {}                           # initialize an empty dict to hold all our unique_words
    for word in word_bank_list:                # iterate through all words in the word_bank_list
        unique_words[word] = unique_words.get(word, 0) + 1   # return the value associated with the word and bind it. If word is not found, add the word with value 1. If the word is found, add 1 to the current value
    return unique_words  

# print count_unique("Porcupine see, porcupine do.")
# 14 failures after this runs (b/c 3 tests)

    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}
  
    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

def common_items(list1, list2):
    common_list = []                        # Initialize an empty list to put common items in
    
    for item in list1:                      # iterate through all items in list1
        for other_item in list2:            # Iterate through all items in list 2.
            if item == other_item:          # If the item in list1 is the same as the item in list2,
                common_list.append(item)    # append the item to the common_list
            else:                           # otherwise
                pass                        # pass == null (nothing happens when it executes)
    return common_list

# print common_items([1, 2, 3, 4], [1, 1, 2, 2])
# 11 failures after this runs (b/c 3 tests)

    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between 
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

def unique_common_items(list1, list2):
    common_list = []                            # Initialize an empty list to put common items in
    
    for item in list1:                          # iterate through all items in list1
        for other_item in list2:                # Iterate through all items in list 2.
            if item == other_item and item not in common_list:          # If the item in list1 is the same as the item in list2, AND THAT ITEM IS NOT ALREADY IN THE LIST
                common_list.append(item)        # append the item to the common_list
            else:                               # otherwise
                pass                            # pass == null (nothing happens when it executes)
    return common_list

# print unique_common_items([1, 2, 3, 4], [1, 2])
# 9 failures after this runs
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between 
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `common_items`, this should find [1, 2]:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show 
    more than 1 or 2 once:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

def sum_zero(list1):
    new_set = set()       # Need a list of lists back, so should initialize an empty list

    for item in list1:  # iterate through each number
        if -item in list1:                # if the negative version of that number is in the list
            new_set.add(item, -item)            # add a list of that number and its negative version to new_set
    
    print sum_zero([1,2,3,-2,-1])

    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

        
    For example:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together, 
    that's fine, too:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """


def find_duplicates(words):
    new_list = []                   # initialize am epty list to hold words
    for i in words:                 # loop through words list 
        if i not in new_list:       # if i is not in new list
            new_list.append(i)      # add the word to the list 
        else:                        # if it is in new_list
            pass
    return new_list
                                    # convert new_dict to a tuple? can you convert second item in tuple to list?
# print sorted(find_duplicates(["Rose", "is", "a", "rose", "is", "a", "rose"]))

    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(find_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(find_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """


def word_length(words):
    pass                                  # FIXME: come back to this problem
#     new_dict = {}                       # inititalize an empty dict to put words in
#     for item in words:                  # iterate through each item in words list 
#         if len(item) not in new_dict:   # if the item's length is NOT already in dict 
#             new_dict[len(item)] = new_dict[item]    # add the item & items length to new_dict, ie. set key value pair equal to [((length of item),[words])]
#         else:                           # if the item's length IS already in the dict
#     return new_dict                     # add the item, but not the length 
    

# # QUESTION for HEATHER: How do I know what data type to use? 

# print word_length(["ok", "an", "apple", "a", "day"])

    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length.

    For example:

        >>> word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """


def adv_word_length_sorted_words(words):
    """Given list of words, return list of ascending [(len, [sorted-words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length. The list of words
    for that length should be sorted alphabetically.

    For example:

        >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    return []


def pirate_talk(phrase):
    pir_dict = {'sir': 'matey',
            'hotel': 'fleabag inn',
            'student': 'swabbie',
            'boy': 'matey',
            'madam': 'proud beauty',
            'professor': 'foul blaggart',
            'restaurant': 'gallery',
            'your': 'yer',
            'excuse': 'arr',
            'students': 'swammbies',
            'are': 'be',
            'lawyer': 'foul blaggart',
            'the': "th'",                     
            'restroom': 'head',
            'my': 'me',
            'hello': 'avast',
            'is': 'be',
            'man': 'matey',
        }

    ptalk = []               # create an empty list, that will be later converted into a string
    phrase = phrase.split()  # splits the phrase into a list of strings made up of words in the phrase 

    for word in phrase:                     # loop through all words in phrase
        if word in pir_dict:                # if word is in the pirate dictionary
            ptalk.append(pir_dict[word])    # append the key mapped to that word in the pirate dictionary to the ptalk list
        else:                               # if the word is NOT in the pirate dictionary
            ptalk.append(word)              # just add the word itself 
    return " ".join(ptalk)                  # return a string joined with spaces from the list ptalk

# print pirate_talk("my student is not a man"

    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.
   
    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """



    # if the word NOT IN pir_dict
    # add the word as is
    # if word IS IN pir_dict 
    # take the value for the word from the pir_dict dictionary (ie look up the value and replace it)

##############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE.


def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d

def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documenttion tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)
 

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "** ALL TESTS PASSED. GOOD WORK!" 
    print