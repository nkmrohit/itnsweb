from django.shortcuts import render, HttpResponse
from seoanalyzer import analyze
from pytrends.request import TrendReq
import time
import os
from random import randint
import pandas as pd
from pytrends.request import TrendReq
import json 
import yaml
import simplejson as json
import numpy
# Create your views here.

def index(request):
    return render(request,'about/index.html',{'aboutData':'data'})
def seo(request):
    #output = analyze('https://seositecheckup.com/', 'https://www.marketgoal.com/sitemap_index.xml')
    output = analyze('http://www.feedbackinfra.com/contact.php')
    customList = []
    for keys,song in output.items():
        #for datain in song:
        if type(song) == type([]):
            for datain in song:
                #if datain.get('url') != 'None':
                customList.append(datain)
    return render(request,'about/seo.html',{'seoData':customList})

def GoogleTrendsSlopeCalculator(request):
    # Add your Gmail username to the google_username variable and your Gmail password to the google_password variable.
    google_username = "neerajmaurya.21mnnit@gmail.com"
    google_password = "neerajmaurya21071988"
    connector = TrendReq(google_username, google_password)

    # This script downloads a series of CSV files from Google Trends. Please specify a filepath for where you'd like these files to be stored in the below variable.
    path = ""

    # Specify the filename of a CSV with a list of keywords in the variable, keyordcsv. The CSV should be one column, with header equal to Keywords (case sensitive).
    keywordcsv = "http://localhost:8000/static/keywords.csv"
    keywords = pd.read_csv(keywordcsv)
    pytrend = TrendReq()

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(kw_list=['pizza', 'bagel'])

    # Interest Over Time
    interest_over_time_df = pytrend.interest_over_time()
    print(interest_over_time_df.head())
   
def test(request):
    datass = " "
   
    