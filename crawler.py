#webcrawler functions
import requests
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
if(len(sys.argv)>2):
	print('Seed URL :', sys.argv[1])
	url = sys.argv[1]
	print('Check Keyphrase: ', sys.argv[2])
	checkkeyphrase = sys.argv[2]
	keyphraseGivenFlag = True
	print('keyphraseGivenFlag set: ', keyphraseGivenFlag)
elif(len(sys.argv)>1):
	print('Keyphrase: ', sys.argv[1])
	url = sys.argv[1]
	

urls = [url] #stack
visited = [url]
visited_have_keyPhrase = [url]

# defined functions
def addhttps(url):
	httplink="https:"
	#print('starts with', url)
	if "https://" in url[0:8]:
		return url
	elif "http://" in url[0:7]:
		return url
	elif "//" in url[0:2]:
		return httplink+url
	elif "/wiki" in url[0:5]:
		return "http://en.wikipedia.org"+url


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
			
def doesItContainKeyPhrase(soup_var,keyphrase):
	print('key is', keyphrase)
	for elem in soup_var(text=re.compile('(?i)'+keyphrase)):
		return True
	return False			
				
def eitherWikiOrEnWiki(wikiNoWiki):
	patternCombine = pattern3+pattern1
	#htttpPatternCombine = "http://"
	if patternCombine in wikiNoWiki[0:30] or pattern1 in wikiNoWiki[0:6]: #or patternCombine in wikiNoWiki[0:30]:
		return True
	else:
		return False
		
#print('print0 ',urls[0], 'length', len(urls))	

def crawling(urls_single):
	print('inside', urls_single)
	r = urllib2.urlopen(addhttps(urls_single))	
	#soup = BeautifulSoup(r.content,"html.parser")
	soup = BeautifulSoup(r.read())
	#print (soup)
	# for mysoup in soup.find_all(text=re.compile('Information')):
		# print('inside mysoup')
		# print('*******************this is my soup', mysoup)
	if keyphraseGivenFlag:
		keyphraseContainsFlag = doesItContainKeyPhrase(soup,checkkeyphrase)
		print('doesItContainKeyPhrase: ',keyphraseContainsFlag)
		if keyphraseContainsFlag and addhttps(urls_single) not in visited_have_keyPhrase and eitherWikiOrEnWiki(urls_single):
			print('################visited has keyPhrase', urls_single)
			visited_have_keyPhrase.append(addhttps(urls_single))
	else:
		if addhttps(urls_single) not in visited_have_keyPhrase and eitherWikiOrEnWiki(urls_single):
			print('???????????????Doesnt have keyPhrase', urls_single)
			visited_have_keyPhrase.append(addhttps(urls_single))
			
	print('length: ',len(urls_single))
	#urls.pop(0)
	i=1
	for link in soup.find_all('a'):
		#print(link.get('href'))
		i+=1
		#print('Crawling : ',i)
		#print('Checking : ', i, ' ',link.get('href'))
		if eitherWikiOrEnWiki(repr(link.get('href'))) and pattern2 not in repr(link.get('href')) and link.get('href') not in visited and returnNoColon(link.get('href')):
			#print('adding in visited and urls ', link.get('href'))	
			#f.write('sizes of both: Visited: ' , link.get('href') , len(visited), 'URLS: ', len(urls))
			visited.append(link.get('href'))
			#print('adding in urls')
			urls.append(link.get('href'))
			#print('Inside the visited are', visited)
			#print('sizes of both: Visited: ' , link.get('href') , len(visited), 'URLS: ', len(urls))
			
print('starting crawler', urls[0])
crawling(urls[0])	
#print('end crawler, level1 ends', urls)

# print('start level2', len(urls))
urls_level2 = deepcopy(urls) #stack
# print('urls_level2: ', urls_level2)
#print('visited len', len(visited), ' and the visited are', visited)
while len(urls_level2) > 0:
	print('*************size of urls_level2' , len(urls_level2))
	crawling(urls_level2[0])
	urls_level2.pop(0)
		
	


print('crawler visited :  ' , ' length:' , len(visited_have_keyPhrase) , ' :: '  , visited_have_keyPhrase)

	
	