# pretify
import requests
from bs4 import BeautifulSoup
import urllib.request as urllib2

#f = open('C:\Users\Dixit_Patel\Desktop\Working on a dream\StartStudying\sem1\Information Retrieval\python\test.txt', 'a')


url = "http://en.wikipedia.org/wiki/Gerard_Salton"
#url = "http://en.wikipedia.org/wiki/Kausalya"
urls = [url] #stack
visited = [url]
checkkeyphrase = "information retrieval"
pattern1 = "/wiki"
pattern2 = "/wiki/Main_Page"
#patr3 = "Contact_us"

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
		return "http://en.wikipdeia.org"+url

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
			
keyphrase = "information retrieval"
 
 
 
print('print0 ',urls[0], 'length', len(urls))
#while len(urls) > 0:
	#r = requests.get(urls[0])
print('************************')
print('Crawling : ',urls[0])
print('************************')
r = urllib2.urlopen(addhttps(urls[0]))	
#soup = BeautifulSoup(r.content,"html.parser")
soup = BeautifulSoup(r.read())
print('length: ',len(urls))
urls.pop(0)
i=1
for link in soup.find_all('a'):
	#print(link.get('href'))
	i+=1
	print('Crawling : ', i, ' ',link.get('href'))
	if pattern1 in repr(link.get('href')) and pattern2 not in repr(link.get('href')) and link.get('href') not in visited and returnNoColon(link.get('href')):
		print('adding in visited')
		#f.write('sizes of both: Visited: ' , link.get('href') , len(visited), 'URLS: ', len(urls))
		visited.append(link.get('href'))
		print('adding in urls')
		urls.append(link.get('href'))
		#print('sizes of both: Visited: ' , link.get('href') , len(visited), 'URLS: ', len(urls))
		
		
#f.close()
#print(soup.prettify())

print("Visited: ", i)
print(visited)

print("URLS:", urls)

	

