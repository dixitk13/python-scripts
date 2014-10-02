from bs4 import BeautifulSoup
from urllib import parse
#import urllib2
linksarray=[]
page='http://www.mathsisfun.com/' #this value will be use to complete the link.
c=urllib2.urlopen('http://www.mathsisfun.com')
data=c.read()
soup = BeautifulSoup(data)

links=soup.findAll('a')#finds all the links in the page.
for link in links:
    str_links=link.get('href')
    linksarray.append(page+str(str_links))
linkstr=str(linksarray)
file_links=open('links2.html','w')
for linking in range (len(linksarray)):
    hyperlink="<a href="+linksarray[linking]+">"+linksarray[linking]+"</a>"
   
    linkstr=str(hyperlink)
    file_links.write(linkstr)
file_links.close()
for i in range (len(linksarray)):
    try:
        nextdata=urllib2.urlopen(linksarray[i])
        namestr=str(i)
        name=namestr+".html"
        data2=nextdata.read()
        file1=open(name,'w')
        file1.write(data2)
        file1.close()
        print(i)
    except:
        i=i+1
        print("could not open link:",linksarray[i])