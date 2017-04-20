from nytimesarticle import articleAPI
from secret import API
import pprint
import json
import os
import time

def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    print articles.keys()
    for i in articles['response']['docs']:
        dic = {}
        dic['id'] = i['_id']
        if i['abstract'] is not None:
            dic['abstract'] = i['abstract'].encode("utf8")
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['desk'] = i['news_desk']
        dic['date'] = i['pub_date'] 
        dic['section'] = i['section_name']
        if i['snippet'] is not None:
            dic['snippet'] = i['snippet'].encode("utf8")
        dic['source'] = i['source']
        dic['type'] = i['type_of_material']
        dic['url'] = i['web_url']
        dic['word_count'] = i['word_count']
        # locations
        locations = []
        for x in range(0, len(i['keywords'])):
            if 'glocations' in i['keywords'][x]['name']:
                locations.append(i['keywords'][x]['value'])
        dic['locations'] = locations
        # subject
        subjects = []
        for x in range(0, len(i['keywords'])):
            if 'subject' in i['keywords'][x]['name']:
                subjects.append(i['keywords'][x]['value'])
        dic['subjects'] = subjects
        news.append(dic)
    return(news)


def get_articles(begin_date=None, end_date=None):

    api = articleAPI(API)
    all_articles = []
    
    if begin_date is None:
        begin_date = '20150101'

    if end_date is None:
        end_date = '20170420'


    for page in range(0, 20):
        request = api.search(q='Mexico',
               fq={'glocations.contains': 'Mexico'},
               begin_date=begin_date,
               end_date=end_date,
               sort='newest',
               page=page)
        articles = parse_articles(request)
        all_articles = all_articles + articles
        time.sleep(15)
    return all_articles


# mexico_search = get_articles()
# print "********************* Your response begin here"
# print type(mexico_search)
# print len(mexico_search)
# pprint.pprint(mexico_search)
# with open('data.json', 'ab') as outfile:
#     json.dump(mexico_search, outfile, sort_keys=True, indent=4,
#               ensure_ascii=False)


if __name__ == "__main__":

    prompt = """ Hello. This is your scrappy program. Do you want:
    1. to know the date of the last article
    2. See the whole json
    3. Make a search
    4. Quit
    """
    while True:
        ask_user = int(raw_input(prompt))

        if ask_user == 1:
            if not os.path.isfile('/Users/cristina/src/NewYorkTimes/data.json'):
                print "There is not file yet"
            else:
                with open('data.json') as feedsjson:
                    feeds = json.load(feedsjson)
                    last_article = feeds[-1]['date'][0:10]
                    end_date = last_article.replace("-", "")
                    print end_date
 
        elif ask_user == 2:
            if not os.path.isfile('/Users/cristina/src/NewYorkTimes/data.json'):
                print "There is not file yet"
            else:
                with open('data.json') as feedsjson:
                    feeds = json.load(feedsjson)
                    pprint.pprint(feeds)

        elif ask_user == 3:
            if not os.path.isfile('/Users/cristina/src/NewYorkTimes/data.json'):
                print "the begin_date is 20150101"
                search = get_articles()
                with open('data.json', 'wr') as outfile:
                    json.dump(search, outfile, sort_keys=True, indent=4, ensure_ascii=False)

            else:
                with open('data.json', 'ab') as feedsjson:
                    feeds = json.load(feedsjson)
                    last_article = feeds[-1]['date'][0:10]
                    end_date = last_article.replace("-", "")
                    print "the end_date is %s" % (end_date)
                    search = get_articles(end_date)
                    feeds.append(search)
                    with open('data.json', 'ab') as outfile:
                        json.dumps(feeds, outfile, sort_keys=True, indent=4, ensure_ascii=False)

        elif ask_user == 4:
            break

        else:
            print "I don't understand that directive"

