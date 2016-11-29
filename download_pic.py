import requests
from bs4 import BeautifulSoup
r = requests.get("http://cl.fatt.pw/htm_data/8/1611/2155700.html")
print("已获取网页")
html_doc = BeautifulSoup(r.text, "html.parser")
div = html_doc.find("div", {"class": "tpc_content do_not_catch"})
inputs = div.findAll("input")
links = []
for i in range(len(inputs)):
    link = inputs[i].attrs["src"]
    links.append(link)
print("已经抓取链接>>>")
filenames = [i for i in range(len(links))]
for i in range(len(links)):
    print("正在获取图片>>>>>>")
    rPic = requests.get(links[i])
    print("正在下载图片>>>>>>"+str(links[i]))
    with open(str(filenames[i])+'.jpg', "wb") as f:
        f.write(rPic.content)
