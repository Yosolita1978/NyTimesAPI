import json


def read_json(files):
    with open(files) as feedsjson:
        feeds = json.load(feedsjson)
    return feeds


def find_common_headlines(list_dicts):
    headlines_words = {}
    regulars = set(["to", "of", "and", "a", "an", "in", "the", "that", "it", "It", "for", "on", "as", "at", "The", "A", "Is", "with", "With", "AN", "from", "From", "in", "In"])
    for dic in list_dicts:
        headline = dic["headline"]
        for word in headline.split():
            if word == "Mexico" or word == "Mexico:" or word == "Mexico,":
                continue
            if word in regulars:
                continue
            if word not in headlines_words:
                headlines_words[word] = 1
            else:
                headlines_words[word] += 1

    return headlines_words

def find_max(dic):

    words = dic.items()
    def getKey(tup):
        word, value = tup
        return value

    commons = sorted(words, key=getKey, reverse=True)
    return commons


def find_desk(list_dicts):
    desk_dic = {}
    for dic in list_dicts:
        desk = dic["desk"]
        if desk == None:
            continue
        if desk not in desk_dic:
            desk_dic[desk] = 1
        else:
            desk_dic[desk] += 1

    return desk_dic

def find_max_desk(dic):

    deskes = dic.items()
    def getKey(tup):
        word, value = tup
        return value

    commons_desks = sorted(deskes, key=getKey, reverse=True)
    return commons_desks

trump = read_json('data_trump.json')
words = find_common_headlines(trump)
commons = find_max(words)

print "The most commons words in the headlines about Mexico in the 100 first days of Trump are:"
for tup in commons[:11]:
    print tup

obama = read_json('data_obama.json')
words_obama = find_common_headlines(obama)
commons_obama = find_max(words_obama)

print "The most commons words in the headlines about Mexico in the 100 first days of Obama are:"
for tup in commons_obama[:11]:
    print tup

trump_desk = find_desk(trump)
favorite_desk_trump = find_max_desk(trump_desk)
print "News about Mexico in the Trump administration came from these desks:"
for tup in favorite_desk_trump:
    print tup

obama_desk = find_desk(obama)
favorite_desk_obama = find_max_desk(obama_desk)
print "News about Mexico in the Obama administration came from these desks:"
for tup in favorite_desk_obama:
    print tup

