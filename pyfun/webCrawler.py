import urllib.request
aurl = "https://www.dell.com/community/数据存储讨论区/网络基本功系列-细说网络那些事儿-3月26日更新/td-p/7045185"

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html

def saveHtml(file_name,file_content):
    with open(file_name.replace('/','_')+".html","wb") as f:
        f.write(file_content)

html = getHtml(aurl)
saveHtml('networkTraining',html)