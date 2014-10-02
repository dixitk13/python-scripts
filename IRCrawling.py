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

#output file
output = open("output.txt","w+");

print('Number of arguments:', len(sys.argv), 'arguments.')
#checks the script arguments given or not
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

#stacks
urls = [url]
#temp stack to keep trace of
urls_stack = []
#unique stack to keep unique links
unique = []

#checks if the soup contains the the key phrase
def doesItHaveKeyPhrase(my_soup,url):
	if keyphraseGivenFlag:
		keyphraseContainsFlag = doesItContainKeyPhrase(my_soup, checkkeyphrase)
		if keyphraseContainsFlag:
			return True
		else:
			return False
	else:
		return True

#adds http:// to the URLS so that it can crawl
def addhttps(url):
    httplink = "https:"
    if "https://" in url[0:8]:
        return url
    elif "http://" in url[0:7]:
        return url
    elif "//" in url[0:2]:
        return httplink + url
    elif "/wiki" in url[0:5]:
        return "http://en.wikipedia.org" + url

# returns boolean values if the colon is present in the URL for checking
def returnNoColon(url):
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

#checks if the soup contains the key phrase
def doesItContainKeyPhrase(soup_var, keyphrase):
    for elem in soup_var(text=re.compile('(?i)' + keyphrase)):
        return True
    return False

#checks if the pattern is //wiki or //en.wikipedia.org/wiki for english wiki pages
def eitherWikiOrEnWiki(wikiNoWiki):
    patternCombine = pattern3 + pattern1
    if patternCombine in wikiNoWiki[0:30] or pattern1 in wikiNoWiki[0:6]:
        return True
    else:
        return False

#crawls the levels for unfocussed kind of crawling
def crawling(urls_single,urls_stack,depth):
    urls_single = addhttps(urls_single)
    r = urllib2.urlopen(urls_single)
    rread = r.read()
    if urls_single not in unique:
        unique.append(urls_single)
        if not depth>=3:
            soup = BeautifulSoup(rread)
            i = 1
            for link in soup.find_all('a'):
                i += 1
                if doesItHaveKeyPhrase(soup,urls_single) and eitherWikiOrEnWiki(repr(link.get('href'))) and pattern2 not in repr(link.get('href')) and link.get('href') not in urls_stack and returnNoColon(link.get('href')):
                    urls_stack.append(link.get('href'))


#crawls the levels for focussed kind of crawling
def crawlingFocussed(urls_single,urls_stack,depth):
    urls_single = addhttps(urls_single)
    r = urllib2.urlopen(urls_single)
    rread = r.read()
    if re.search(b"Information Retrieval",rread,re.IGNORECASE) is not None:
        if urls_single not in unique:
            unique.append(urls_single)
            if not depth>2:
                soup = BeautifulSoup(rread)
                i = 1
                for link in soup.find_all('a'):
                    i += 1
                    if doesItHaveKeyPhrase(soup,urls_single) and eitherWikiOrEnWiki(repr(link.get('href'))) and pattern2 not in repr(link.get('href')) and link.get('href') not in urls_stack and returnNoColon(link.get('href')):
                        urls_stack.append(link.get('href'))


#dict to hold the values
dict = {1: urls , 2: [], 3: []};

print('start crawling!')
for k in range(0,3):
    k+=1
    j=k+1
    #print ("-------------------------------------------We're on level : ", k, "---------------------------------------")
    urls_Level = []
    urls_Level = dict[k]
    while len(urls_Level) > 0:
        if keyphraseGivenFlag:
            crawlingFocussed(urls_Level[0],urls_stack,k)
        else:
            crawling(urls_Level[0],urls_stack,k)
        urls_Level.pop(0)
        ##print('adding in dict: ', dict[k])
    print('urls_stack: ', len(urls_stack) , ' ->',urls_stack)
    dict[j] = deepcopy(urls_stack)
    if k == 2 and not keyphraseGivenFlag:
        break;
    urls_stack = []


# prints the dict
print (dict[k])
if not keyphraseGivenFlag:
    print('UnFocussed ', urls_stack, '->', len(urls_stack))
    output.write('UnFocussed Length: ' + str(len(urls_stack)) +'\n')
    output.write('UnFocussed ->' + str(urls_stack));
else:
    print ('unique' , unique, '->' , len(unique))
    output.write('Focussed Length: ' + str(len(unique))+'\n')
    output.write('Focussed ->' + str(unique));
    #output.write('unique' , unique, '->' , len(unique));



