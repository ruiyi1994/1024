import requests
from bs4 import BeautifulSoup
import time
r = requests.get("http://cl.fatt.pw/thread0806.php?fid=20")
r.encoding = "gb2312"
html_doc = BeautifulSoup(r.text, "html.parser")
h3s = html_doc.findAll("h3")
links = []
names = []
for i in range(7, len(h3s)):
    link = h3s[i].find("a").attrs["href"]
    name = h3s[i].find("a").get_text()
    links.append(link)
    names.append(name)
print(links)
for i in range(len(links)):
    time.sleep(3)
    url = r"http://cl.fatt.pw/"+links[i]
    r = requests.get(url)
    r.encoding = "gb2312"
    print(r.status_code)
    p_doc = BeautifulSoup(r.text, "html.parser")
    div = p_doc.find("div", {"class": "tpc_content do_not_catch"})
    p = div.get_text()
    with open(names[i]+".txt", "w", encoding="utf-8") as f:
        f.write(p)
    print("成功下载"+names[i]+".txt")


