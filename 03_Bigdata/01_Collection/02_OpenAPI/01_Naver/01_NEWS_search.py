import urllib.request
import datetime
import json

app_id = "4CKadBAJECoFJ4QWEtiX"
app_pw = "Ufny4nJsgd"

def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",app_id)
    req.add_header("X-Naver-Client-Secret",app_pw)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url:%s => Request Success" % (datetime.datetime.now(), url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None

def getNaverSearchResult(sNode, search_text, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" %sNode
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text), page_start, display)
    url = base + node + parameters
    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)
count = 0
def getPostData(post,jsonResult):

    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'title': title,'description': description, 'org_link':org_link,'pDate':pDate})
    global count
    count += 1
    return

def main():
    jsonResult = []

    sNode = 'news'
    search_text = '아베'
    display_count = 100

    nStart = 1
    for index in range(10):
        if index > 0:
            nStart += 100
        jsonSearch = getNaverSearchResult(sNode,search_text,nStart,display_count)
        index = index+1
        for post in jsonSearch['items']:
            getPostData(post,jsonResult)

    with open('%s_naver_%s.json'%(search_text,sNode), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print("%s_naver_%s.json Saved" %(search_text, sNode))
    print(count)
if __name__ == '__main__':
    main()
