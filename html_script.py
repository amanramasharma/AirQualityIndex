import os
import time
import requests
import sys

'''Create a function called retrieve_html
this will get the data from site "en.tutiempo.net" of Banglore City (INDIA) from year 2010-2020
'''
def retrieve_html():
    #firstly we create a loop for year then nested loop for month under nested loop
    for year in range(2010,2021):
        for month in range(1,13):
            """we put if else cond. because in url for month  1-9 url channge (0 before month number) after 9th month url change"""
            if(month<10):
                url= 'https://en.tutiempo.net/climate/0%i-%i/ws-432950.html'.format(month,year)
            else:
                url= 'https://en.tutiempo.net/climate/%i-%i/ws-432950.html'.format(month,year)
        
            # put url in "texts" 
            texts=requests.get(url)
        
            # then encode the html url to utf
            text_utf = texts.text.encode('utf=8')
        
            # Creating a folder for each year in Data/Html_data folder
            if not os.path.exists("Data/Html_data/{}".format(year)):
                os.makedirs("Data/Html_data/{}".format(year))
            
            # Put the html url data inside the folder acc. to year  
            with open("Data/Html_data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
        
        sys.stdout.flush()
        
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time Taken {}".format(stop_time-start_time))