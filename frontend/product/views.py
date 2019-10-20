from django.shortcuts import render,HttpResponse, Http404
import whois
from alexa import AlexaInfo
import alexa
from myawis import *
import urllib.request, sys, re
import xmltodict, json
from seoanalyzer import analyze


# Create your views here.
def processor(tag):
    href = tag.get('href')
    if not href: return False
    return True if (href.find("google") == -1) else False

def index(request):
    domain = whois.whois('marketgoal.com')
    xml = urllib.request.urlopen('http://data.alexa.com/data?cli=11&dat=s&url={}'.format("www.marketgoal.com")).read()
    result= xmltodict.parse(xml)
    
    data = json.dumps(result).replace("@","")
    data_tojson = json.loads(data)

    # html = """
    # <div>hello</div>
    # <a href="/index.html">Not this one</a>"
    # <a href="http://google.com">Link 1</a>
    # <a href="http:/amazon.com">Link 2</a>
    # """
    # soup = BeautifulSoup('http://marketgoal.com')
    # http_links = soup.findAll('a', href=re.compile(r"^http"))
    # results = [a for a in http_links if a['href'].find('google') == -1]
    # print(results)

   # obj = CallAwis('AKIAJA5H7O5EY24LS5HQ' , '3NO5p4ebYtkwPaDavcLpgNUd+pwItyTYhlrvlHgd')
    # obj=CallAwis('AKIAJA5H7O5EY24LS5HQ','3NO5p4ebYtkwPaDavcLpgNUd+pwItyTYhlrvlHgd')
    # allalexaData = obj.urlinfo('http://www.pageturnpro.com/')
    # allalexaData = json.loads(json.dumps(xmltodict.parse(str(allalexaData))))
    # alexaRand = {}
    # for key,value in allalexaData['aws:UrlInfoResponse']['aws:Response']['aws:UrlInfoResult']['aws:Alexa'].items():
    #     if key == 'aws:TrafficData':
    #         alexaRand['Rank'] = value['aws:Rank']
    #         alexaRand['RankUs'] = value['aws:RankByCountry']['aws:Country']
            
    #xmltodict.unparse(allalexaData, pretty=True)
    #urlinfo = obj.urlinfo("www.pageturnpro.com")
    #allalexaData = obj.urlinfo('http://www.pageturnpro.com/aboutus.aspx')
    output = analyze('https://www.foodcourier.com','https://www.foodcourier.com/sitemap.xml')
    pageError = []
    for keys,song in output.items():
        #for datain in song:
        if type(song) == type([]):
            for datain in song:
                pageError.append(datain)

    return render(request,'product/index.html',{'domains':domain,'alexa':data_tojson["ALEXA"]["SD"][1],'pageError':pageError})

def cdhostDetail(request):
    return HttpResponse('host detail')