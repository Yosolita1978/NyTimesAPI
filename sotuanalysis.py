

def countwords(filename):
    word_counter = {}
    regulars = set(["to", "of", "and", "a", "an", "in", "the", "that", "it", "It", "for", "on", "as", "at", "The", "A", "Is", "with", "With", "AN", "from", "From", "in", "In", "---", "--"])
    with open(filename, 'r') as document:
        for line in document:
            word_list = line.replace(',', '').replace('\'', '').replace('.', '').lower().split()
            for word in word_list:
                if word in regulars:
                    continue
                if word not in word_counter:
                    word_counter[word] = 1
                else:
                    word_counter[word] = word_counter[word] + 1

    return word_counter


def find_max(dic):

    words = dic.items()

    def getKey(tup):
        word, value = tup
        return value

    commons = sorted(words, key=getKey, reverse=True)
    return commons


def convert(tup, dic):
    dic = dict(tup)
    return dic


Counter = countwords('sotu2018.txt')
max_words = find_max(Counter)
print type(max_words)
words_dictionary = {}
words = convert(max_words, words_dictionary)
print words