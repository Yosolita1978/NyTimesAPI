from nytimesarticle import articleAPI
from secret import API
import pprint
import csv


def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['id'] = i['_id']
        if i['abstract'] is not None:
            dic['abstract'] = i['abstract'].encode("utf8")
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['desk'] = i['news_desk']
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        dic['section'] = i['section_name']
        if i['snippet'] is not None:
            dic['snippet'] = i['snippet'].encode("utf8")
        dic['source'] = i['source']
        dic['type'] = i['type_of_material']
        dic['url'] = i['web_url']
        dic['word_count'] = i['word_count']
        # locations
        locations = []
        for x in range(0,len(i['keywords'])):
            if 'glocations' in i['keywords'][x]['name']:
                locations.append(i['keywords'][x]['value'])
        dic['locations'] = locations
        # subject
        subjects = []
        for x in range(0,len(i['keywords'])):
            if 'subject' in i['keywords'][x]['name']:
                subjects.append(i['keywords'][x]['value'])
        dic['subjects'] = subjects   
        news.append(dic)
    return(news)

def get_articles():
   
    api = articleAPI(API)
    all_articles = []
    pages = [0, 1, 2]
    for page in pages:
        request = api.search(q = 'Mexico',
               fq = {'source':['Reuters','AP', 'The New York Times']},
               begin_date = '20160101', 
               page=str(page))
        articles = parse_articles(request)
        all_articles = all_articles + articles
    return(all_articles)


mexico_search =  get_articles()
print "********************* Your response begin here"
print len(mexico_search)
pprint.pprint(mexico_search)

keys = mexico_search[0].keys()
with open('mex-mentions.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(mexico_search)









