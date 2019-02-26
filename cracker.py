'''SHA-1 Cracker takes a user's hash and attemps to solve for it's plaintext value using a dictionary of over 46,000 words'''
import hashlib, sys

# string to hold word with potential matched hash
word_match = ''

# string to hold salt if orginal hash is not cracked
salt = 'f0744d60dd500c92c0d37c16174cc58d3c4bdd8e'
salt_word = ''

# gather each word's SHA-1 hash and test each word in the list against the user's hash
# if a match exists between the word's hash and the user's hash, add to guess_list
def crack(hash, salt='', separate=False):
    # access list of words for reading only
    world_list = open('10-million-password-list-top-1000000.txt', 'r')

    # serves as a counter for the amount of guesses gone through
    guesses = 0

    if separate:
        dictionary = {}
        for word in graduate_dict:
            guesses += 1
            if hash == word:
                return [word, guesses]
    else:
        for word in world_list:
            word = word.rstrip('\n')
            word = salt + word
            word_hash = hashlib.sha1(word).hexdigest()
            guesses += 1

            if hash == word_hash:
                return [word, guesses]

    return ['', guesses]

# filters hash to populate a dictionary with hashes that begin with the passed in hash
def filter_hashes(hash):
    world_list = open('10-million-password-list-top-1000000.txt', 'r')

    dictionary = {}
    for word_1 in world_list:
        word_1 = word_1.rstrip('\n')
        for word_2 in world_list:
            word_2 = word_2.rstrip('\n')
            word = word_1 + ' ' + word_2
            word_hash = hashlib.sha1(word).hexdigest()

            if word_hash.startswith(hash):
                dictionary[word_hash] = word

    return dictionary

# prints reults found from each hash
def printResult(match, found=True):
    if found:
        print('The cracked hash is: ' + match[0] +'. This took ' + str(match[1]) + ' guesses.')
    else:
        print('No results found for your hash: ' + match + '.')

# get hash input from command line and convert to lower-case for future comparison
sha1_hash = sys.argv[1]
sha1_hash = sha1_hash.lower()

# attempt to crack primary hash without salt
word_match = crack(sha1_hash)

if len(word_match[0]) > 0:
    printResult(word_match)
elif len(word_match) < 1:
    # use salt to crack hash
    salt_word = crack(salt)
    salt_hash = crack(sha1_hash, salt_word[0])

    if len(salt_hash[0]) > 0:
        printResult(salt_hash)
else:
    # populate dictionary with similar hashes
    graduate_dict = filter_hashes(sha1_hash[0])
    # crack  hash
    graduate_hash = crack(sha1_hash, salt=' ', separate=True)

    if len(graduate_hash[0]) > 0:
        printResult(graduate_hash)
    else:
        printResult(graduate_hash, False)
    