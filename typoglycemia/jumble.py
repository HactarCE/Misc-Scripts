#!/usr/bin/env python3

from random import shuffle
import re
import sys

options = ''.join(sys.argv[1:]).lower()

if 'h' in options:
    print("""\
Supply input through stdin.

Command line options:
h       Print this help page
f       Preserve first letter
f[n]    Preserve first n letters
l       Preserve last letter
l[n]    Preserve last n letters
k[n]    Preserve ("keep") at least n additional letters
%[n]    Preserve at least an additional n% of letters
d[n]    Restrict letter travel distance to a maximum of n

Options can be strung together or separated by whitespace; e.g.
f2ld3
f2 l d3
fl %50 k2

Behavior for redundant or invalid options is unspecified. All options are
case-insensitive. Only integers are allowed at this time.

Be wary of using low d[n] values with long words. This option is implemented
very poorly and can be extremely slow.
""")
    exit()

kwarg_letters = {
    'f': 'keep_first',
    'l': 'keep_last',
    'k': 'keep_n',
    '%': 'keep_percent',
    'd': 'max_distance'
}

kwargs = {}

if 'f' in kwargs:
    kwargs['keep_first'] = 1
if 'l' in kwargs:
    kwargs['keep_first'] = 1

for letter, option in kwarg_letters.items():
    if letter in options:
        m = re.search(rf'{letter}(\d+)', options)
        if m:
            kwargs[option] = int(m.group(1))
        else:
            kwargs[option] = True


# for k, v in kwargs.items():
#     print(f'{k}: {v}')


def swap(l, i1, i2):
    """Swap two indices in a list, in place (does not return the list)."""
    l[i1], l[i2] = l[i2], l[i1]


def resolve_index(l, i):
    """Swap two indices such that index i equals its value, in place (does not
    return the list)."""
    swap(l, i, l.index(i))


def get_max_displacement(permutation):
    """Returns the maximum absolute difference between each value and its index
    in a permutation."""
    return max(abs(i - permutation[i]) for i in range(len(permutation)))


def scramble_word(word, *, keep_first=False, keep_last=False, keep_n=0, keep_percent=0, max_distance=-1):
    if len(word) < 2 + keep_first + keep_last + keep_n:
        # If we're preserving less than (length of word)-2 letters, we can't
        # scramble the word.
        return word
    pre = ''
    if keep_first:
        pre, word = word[:keep_first], word[keep_first:]
    post = ''
    if keep_last:
        word, post = word[:-keep_last], word[-keep_last:]
    if max_distance < 0:
        max_distance = len(word)
    permutation = [max_distance + 1]
    # It's kinda lazy to use a loop like this (and quite dangerous too, with low
    # max_distance values and long words), but oh well.
    while get_max_displacement(permutation) > max_distance:
        # permutation will be a map of where each character originates.
        # e.g. [1 2 0] means 'abc' becomes 'bca'.
        permutation = list(range(len(word)))
        shuffle(permutation)
        # Now we have to swap random indices so that keep_n letters (or
        # keep_percent of letters) are preserved.
        if keep_percent:
            keep_n += int(len(word) * keep_percent / 100)
        if keep_n > len(word):
            return word
        indices_to_keep = list(range(len(word)))
        shuffle(indices_to_keep)
        indices_to_keep = indices_to_keep[:keep_n]
        for index in indices_to_keep:
            # Swap two letters to put this back where it belongs
            resolve_index(permutation, index)
        # print(indices_to_keep, permutation)
    word = ''.join(word[permutation[i]] for i in range(len(word)))
    return pre + word + post


# Take user input (ctrl-D to stop)
original_text = ''.join(line for line in sys.stdin)


# Regex is greedy by default; each of these patterns will consume as many
# characters as they can, so we don't have to worry about words being split into
# individual letters. The parentheses allow us to break each match into separate
# groups, with one being the word and one being the nonword
word_pattern = r'([a-zA-Z]*)' # any lowercase or capital letter
nonword_pattern = r'([^a-zA-Z]*)' # anything other than a lowercase or capital letter

scrambled_text = ''

for word, nonword in re.findall(word_pattern + nonword_pattern, original_text):
    scrambled_text += scramble_word(word, **kwargs) + nonword

print(scrambled_text)
