import urllib.request, re
#f = urllib.request.urlopen('http://www.python.org/')
#print(f.read(1000).decode('utf-8'))
myurl = "http://en.wikipedia.org/wiki/Gerard_Salton"
for i in re.findall('''href=["'](.[^"']+)["']''', urllib.request.urlopen(myurl).read(), re.I):
        print(i)
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
                print(ee)				
                textfile.write(ee+'\n')
				
		
textfile.close()
				