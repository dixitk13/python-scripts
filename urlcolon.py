#test url : 's
url1 = "//en.wikipedia.org/w/index.php?title=Template:Hindu-myth-stub&action=edit"
url11 = "//en.wikipedia.org/w/index.php?title=TemplateHindu-myth-stub&action=edit"
url2 = "https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=onate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en"
url22 = "https://donate.wikimedia.org/wiki/SpecialFundraiserRedirector?utm_source=onate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en"
url3 = "http://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=onate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en"
url33 = "http://donate.wikimedia.org/wiki/SpecialFundraiserRedirector?utm_source=onate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en"

pattern = ":"

import re
from bs4 import BeautifulSoup
import sys
html_text = """
<h2>Information retrieval</h2>
<h2>$keyphrase</h2>
<h1>foo #126666678901</h1>
<h2>this is interesting #126666678901</h2>
<h2>this is blah #124445678901</h2>
"""
keyphraseGivenFlag = True
checkkeyphrase = "Information retrieval"
soup = BeautifulSoup(html_text)
stack = []

#	for mysoup in soup.find_all(text=re.compile('^Information$')):

#for elem in soup(text=re.compile(r' #\S{11}')):
# for elem in soup(text=re.compile('Information')):
    # print(elem)
	
def eitherWikiOrEnWiki(wikiNoWiki):
	patternCombine = pattern3+pattern1
	#htttpPatternCombine = "http://"
	if patternCombine in wikiNoWiki[0:30] or pattern1 in wikiNoWiki[0:6]: #or patternCombine in wikiNoWiki[0:30]:
		return True
	else:
		return False
	
pattern1 = "/wiki"
pattern3 = "//en.wikipedia.org"
pattern2 = "/wiki/Main_Page"
patternCombine = pattern3+pattern1
urls1 = "http://en.wikipedia.org/wiki/Gerard_Salton"
urls2 = "/wiki/Amit_Singhal"
urls3 = "//de.wikipedia.org/wiki/Gerard_Salton"
print('wikinowiki : ',eitherWikiOrEnWiki(urls2))	

def doesItContainKeyPhrase(soup_var,keyphrase):
	print('key is', keyphrase)
	for elem in soup_var(text=re.compile('(?i)'+keyphrase)):
		return True
	return False

print("Is it? : ",doesItContainKeyPhrase(soup,sys.argv[1]))
	
def addhttps(url):
	httplink="https:"
	print('starts with', url)
	if "https://" in url[0:8]:
		return url
	elif "http://" in url[0:7]:
		return url
	elif "//" in url[0:2]:
		return httplink+url

def returnNoColon(url):
	print('starts with', url3)
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
		
def doesItHaveKeyPhrase(my_soup,urls_stack):
	if keyphraseGivenFlag:
		keyphraseContainsFlag = doesItContainKeyPhrase(my_soup, checkkeyphrase)
		print('doesItContainKeyPhrase: ', keyphraseContainsFlag)
		if keyphraseContainsFlag :
			print('################visited has keyPhrase')
			urls_stack.append("crap")
			return True
		else:
			return False
	else:
		return True		
		
print(doesItHaveKeyPhrase(soup,stack))
		
#print('funcall: ',url2[8:])
# print('url1 value : ',returnNoColon(url1))
# print('url11 value : ',returnNoColon(url11))
# print('url2 value : ',returnNoColon(url2))
# print('url22 value : ',returnNoColon(url22))
# print('url3 value : ',returnNoColon(url3))
# print('url33 value : ',returnNoColon(url33))


# print('addhttps url1 value : ',addhttps(url1))
# print('addhttps url11 value : ',addhttps(url11))
# print('addhttps url2 value : ',addhttps(url2))
# print('addhttps url22 value : ',addhttps(url22))
# print('addhttps url3 value : ',addhttps(url3))
# print('addhttps url33 value : ',addhttps(url33))


