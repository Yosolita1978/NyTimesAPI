import json
import io


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


def convert_json_for_d3(json):

    read_data = read_json(json)
    all_words = find_common_headlines(read_data)
    commons_words = dict(find_max(all_words))
    with io.open('obama.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(commons_words, ensure_ascii=False))


print (convert_json_for_d3('data_obama.json'))