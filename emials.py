import urllib2
import html2text
import os
import re
keywords=['http']
f=urllib2.Request("http://iiit.ac.in/people/faculty")
response=urllib2.urlopen(f)
the_page=response.read()
email_file=html2text.html2text(the_page)
print email_file
k=type(email_file)
string=email_file.encode('ascii','ignore')
text=open("output.txt" , "r+")
text.write(string)
for line in text:
	if 'http' in line:
		line=line[line.find("(")+1:line.find(")")]
		print line
text.close()


