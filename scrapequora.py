import feedparser
import hashlib
import json
from bs4 import BeautifulSoup


d = feedparser.parse("http://www.quora.com/VJ_UG/answers/rss")
for e in d["entries"] :
    title = e["title"]
    summary = e["summary"]
    h = hashlib.sha224(title).hexdigest()
    summary = summary.replace("<br />","__LINEBREAK__")    
    soup = BeautifulSoup(summary)
    
    answer = soup.get_text()[11:]
    answer = answer[:-21]
    answer = answer.replace("__LINEBREAK__","\n")
    answer = answer.strip()
    print title
    print answer
    j = {"question":title,"answer":answer,"link":e["link"]}
    f=open(h+".quora.txt",'w')
    f.write(json.dumps(j))
    f.close()
