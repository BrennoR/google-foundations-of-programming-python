# Find longest word in dictionary that is a subsequence of a given string


# Greedy approach, O(N*W)
def find_longest(S: str, D: set) -> str:
    longest = ""
    for word in D:
        if len(word) > len(longest):
            i = 0
            while i < len(S):
                if S[i] == word[0]:
                    k = i
                    j = 1
                    while k < len(S) and j < len(word):
                        if S[k] == word[j]:
                            j += 1
                        k += 1

                    if j == len(word):
                        longest = word
                i += 1

    return longest


# Greedy approach w/ sorted set of words, O(N*W)
def find_longest_2(S: str, D: set) -> str:
    D = sorted(D, key=lambda x: len(x), reverse=True)
    for word in D:
        i = 0
        while i < len(S):
            if S[i] == word[0]:
                k = i
                j = 1
                while k < len(S) and j < len(word):
                    if S[k] == word[j]:
                        j += 1
                    k += 1

                if j == len(word):
                    return word
            i += 1

    return ""


# Greedy approach w/ dictionary indices, O(N + L * log(log(N)))
def find_longest_3(S: str, D: set) -> str:
    indices = dict()
    for idx, ch in enumerate(S):
        if ch not in indices:
            indices[ch] = [idx]
        else:
            indices[ch].append(idx)

    D = sorted(D, key=lambda x: len(x), reverse=True)
    for word in D:
        i = -1
        j = 0
        while i < len(S):
            if word[j] in indices:
                for val in indices[word[j]]:    # binary search will be even faster
                    if val > i:
                        i = val
                        j += 1
                        if j == len(word):
                            return word
            else:
                break


# Official Solution
import collections


# O(N + L)
def find_longest_word_in_string(letters, words):
    letter_positions = collections.defaultdict(list)
    # For each letter in 'letters', collect all the indices at which it appears.
    # O(#letters) space and speed.
    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)
    # For words, in descending order by length...
    # Bails out early on first matched word, and within word on
    # impossible letter/position combinations, but worst case is
    # O(#words # avg-len) * O(#letters / 26) time; constant space.
    # With some work, could be O(#W * avg-len) * log2(#letters/26)
    # But since binary search has more overhead
    # than simple iteration, log2(#letters) is about as
    # expensive as simple iterations as long as
    # the length of the arrays for each letter is
    # “small”.  If letters are randomly present in the
    # search string, the log2 is about equal in speed to simple traversal
    # up to lengths of a few hundred characters.
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        found = True
        for letter in word:
            if letter not in letter_positions:
                found = False
                break
            # Find any remaining valid positions in search string where this
            # letter appears.  It would be better to do this with binary search,
            # but this is very Python-ic.
            possible_positions = [p for p in letter_positions[letter] if p >= pos]
            if not possible_positions:
                found = False
                break
            pos = possible_positions[0] + 1

        # We didn't break out of the loop, so all letters have valid positions
        if found:
            return word


string = "abppplee"
words = {"able", "ale", "appyle", "bale", "kangaroo"}

print(find_longest_word_in_string(string, words))
