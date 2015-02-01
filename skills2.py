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

   ** ALL TESTS PASSED. GOOD WORK!

Good luck!

"""

def count_unique(input_string):
    word_bank_list = input_string.split()      # bind word_bank_list to a string made up of the elements in the input_string
    
    unique_words= {}                           # initialize an empty dict to hold all our unique_words
    for word in word_bank_list:                # iterate through all words in the word_bank_list
        unique_words[word] = unique_words.get(word, 0) + 1   # return the value associated with the word and bind it. If word is not found, add the word with value 1. If the word is found, add 1 to the current value
    return unique_words        

# print count_unique("Porcupine see, porcupine do.")

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

print common_items([1, 2, 3, 4], [1, 1, 2, 2])

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

print unique_common_items([1, 2, 3, 4], [1, 2])

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
   """Return list of x,y number pair lists from a list where x+y==0"""
   # num_pairs = []                      # initialize an empty list to hold number pairs - pairs should be in a list themselves
   # for item in list1:                  # loop through list1 
   #      other_item = list1[1]
   #      for other_item in list1:   # the next item in the list is the item at the index 1 higher.
   #          print "item is: ", item
   #          print "other item is: ", other_item
   #          if item + other_item == 0:   # check whether: the num you are looping by (x) + y == 0
   #              num_pairs.append([list1[item], list1[other_item]])      # if it is, append that list to the num_pairs list
   #          else:                       # if its not,
   #              continue                # continue with the next iteration of the loop (ie. next other_item)
   #      return num_pairs

print sum_zero([1, 2, 3, -2, -1]) 


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
    new_list = []               # initialize an empty list to put new list in
                                # loop through all items in the words list
                                # check to see if word you're looping over is EXACTLY the same as the other word ("is")
                                # if so, append it to the list 

"""Given a list of words, return the list with duplicates removed.

For example:

    >>> sorted(find_duplicates(
    ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
    ['a', 'is', 'rose']

You should treat differently-capitalized words as different:

    >>> sorted(find_duplicates(
    ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
    ['Rose', 'a', 'is', 'rose']"""

    return []


def word_length(words):
"""Given list of words, return list of ascending [(len, [words])].

Given a list of words, return a list of tuples, ordered by word-length.
Each tuple should have two items--the length of the words for that 
word-length, and the list of words of that word length.

For example:

    >>> word_length(["ok", "an", "apple", "a", "day"])
    [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

"""

# given a LIST of words, return a LIST of TUPLES, ORDERED by word LENGTHb
# each TUPLE should have 2 items: (LENGTH of the words, [LIST of words of that word length]) 

new_dict = {}                               # inititalize an empty list to put words and length in
    for item in words:                      # loop through each word in list. 
        word_len = words[item].length()     # word_len is bound to the length of the word that you are iterating over
        if word_len not in new_dict:        # for each item, check to see if the LENGTH of that word is already in the list 
                                            # if it the length NOT, add the word to list and the word length to new_list
        else:                       # if the length IS already in the list, 
                                    # find the tuple with the correct length (by looking for the key)
                                    # add that word to the list of words that have that length

# QUESTION: Should we first create a dictionary, so we can access by keys? Then convert this dictionary to a list of tuples? 
# if do this with sets, have to make sure can sort it after b/c sets are unordered
return []

# check the length of each item
# if the item length IS NOT already in the list, add the length and the word to the list
# if the item length IS ALREADY INT HE LIST, just add the word to the list that corresponds to that item length


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

return ""


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