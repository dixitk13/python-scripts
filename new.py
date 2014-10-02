__author__ = 'Dixit_Patel'


# webcrawler functions

from bs4 import BeautifulSoup
from copy import deepcopy
import sys
import re
import urllib.request as urllib2

url = "http://en.wikipedia.org/wiki/Gerard_Salton"
#checkkeyphrase = "information retrieval"
pattern1 = "/wiki"
pattern3 = "//en.wikipedia.org"
#pattern3 = "//en.wikipedia.org/wiki"
pattern2 = "/wiki/Main_Page"
keyphraseGivenFlag = False

print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Seed URL :', sys.argv[1])
if len(sys.argv) > 2:
    print('Seed URL :', sys.argv[1])
    url = sys.argv[1]
    print('Check Keyphrase: ', sys.argv[2])
    checkkeyphrase = sys.argv[2]
    keyphraseGivenFlag = True
    print('keyphraseGivenFlag set: ', keyphraseGivenFlag)
elif (len(sys.argv) > 1):
    print('Keyphrase: ', sys.argv[1])
    url = sys.argv[1]

urls = [url]  #stack
urls_stack = []
urls_cannonical_stack = []
visited = [url]
visited_have_keyPhrase = [url]
unique = []

# defined functions
def doesItHaveKeyPhrase(my_soup,url):
	if keyphraseGivenFlag:
		keyphraseContainsFlag = doesItContainKeyPhrase(my_soup, checkkeyphrase)
		#print('doesItContainKeyPhrase: ', keyphraseContainsFlag)
		if keyphraseContainsFlag:    #and addhttps(url) not in urls_stack and eitherWikiOrEnWiki(url):
			#print('################visited has keyPhrase', url)
			#urls_stack.append(addhttps(url))
			return True
		else:
			return False
	else:
		return True

def addhttps(url):
    httplink = "https:"
    #print('starts with', url)
    if "https://" in url[0:8]:
        return url
    elif "http://" in url[0:7]:
        return url
    elif "//" in url[0:2]:
        return httplink + url
    elif "/wiki" in url[0:5]:
        return "http://en.wikipedia.org" + url


def returnNoColon(url):
    #print('starts with', url)
    if "https://" in url[0:8]:
        if ":" not in url[8:]:
            return True
        else:
            return False
    elif "http://" in url[0:7]:
        if ":" not in url[7:]:
            return True
        else:
            return False
    elif ":" not in url:
        return True
    else:
        return False


def doesItContainKeyPhrase(soup_var, keyphrase):
    #print('key is', keyphrase)
    for elem in soup_var(text=re.compile('(?i)' + keyphrase)):
        return True
    return False


def eitherWikiOrEnWiki(wikiNoWiki):
    patternCombine = pattern3 + pattern1
    #htttpPatternCombine = "http://"
    if patternCombine in wikiNoWiki[0:30] or pattern1 in wikiNoWiki[0:6]:  #or patternCombine in wikiNoWiki[0:30]:
        return True
    else:
        return False


#print('print0 ',urls[0], 'length', len(urls))

def crawling(urls_single,urls_stack,depth):
    urls_single = addhttps(urls_single)
    #print('inside', urls_single)
    r = urllib2.urlopen(urls_single)
    rread = r.read()

    if re.search(b"Information Retrieval",rread,re.IGNORECASE) is not None:
        #print('dasod')
        if urls_single not in unique:
            print ('adding in blank', len(unique), ' - > ', urls_single )
            unique.append(urls_single)
    if not depth>=3:
        soup = BeautifulSoup(rread)
        i = 1
        for link in soup.find_all('a'):
            #print(link.get('href'))
            i += 1
            #print('Checking : ', i, ' ',link.get('href'))
            if doesItHaveKeyPhrase(soup,urls_single) and eitherWikiOrEnWiki(repr(link.get('href'))) and pattern2 not in repr(link.get('href')) and link.get('href') not in urls_stack and returnNoColon(link.get('href')):
            #if doesItHaveKeyPhrase(soup,urls_single) and pattern2 not in repr(link.get('href')) and link.get('href') not in urls_stack and returnNoColon(repr(link.get('href'))):
                urls_stack.append(link.get('href'))
                #urls_cannonical_stack.append()


dict = {1: urls , 2: [], 3: []};

print('start crawling!')
for k in range(0,3):
    k+=1
    j=k+1
    print ("-------------------------------------------We're on level : ", k, "---------------------------------------")
    levelNumber = "Level" + str(k)
    #levelNumberj = "Level" + str(j)
    #urls_Levelj = "urls_Level" + str(k)
    #urls_Level = "urls_Level" + str(k)
    #urls_Levelj = []
    urls_Level = []
    urls_Level = dict[k]
    while len(urls_Level) > 0:
        #print("****************", ' length: ', len(urls_Level),  urls_Level)
        crawling(urls_Level[0],urls_stack,k)
        urls_Level.pop(0)
        ##print('adding in dict: ', dict[k])
    print('urls_stack: ', len(urls_stack) , ' ->',urls_stack)
    dict[j] = deepcopy(urls_stack)
    if k == 2 and not keyphraseGivenFlag:
        break;
    urls_stack = []
    print ('XYZ: ', str(k), ':  ', dict[k])
    print ('XYZ: ', str(j), ':  ', dict[j])
    #print (dict[k])

#print('crawler visited :  ', ' length:', len(visited_have_keyPhrase), ' :: ', visited_have_keyPhrase)
print (dict[k])
if not keyphraseGivenFlag:
    print('UnFocussed ', len(urls_stack), '->', urls_stack)
else:
    print ('Focussed', len(unique), '->' , unique)

#print ('unique', len(unique), '->' , unique)


