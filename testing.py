while len(urls) > 0:
	try:
		print(urls[0])
		htmltext = requests.get(urls[0])
	except:
		print(urls[0])
		
	soup = BeautifulSoup(htmltext.content,"html.parser")
	
	urls.pop(0)
	print(len(urls))
	
	for tag in soup.findAll('a',href=true):
		tag['href'] = urllib.parse.urljoin(url,tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])
			
print(visited) 		