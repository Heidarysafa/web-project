# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:21:06 2017
The perpuse of this script is to get the xml output from dejaclick plugin and extract
the links with the time spend on that page
@author: Mojtaba Heidarysafa
"""
import xml.etree.ElementTree as ET
import pandas as pd

# this will open the xml file replace the path with the path to your file 
with open('C:/wiki2.xml') as file:
    xml_data= file.read()
print(xml_data)
# build the tree object from xml 
xml_object = ET.fromstring(xml_data) 
#extract the links from xml tree object
urls = [] 
for tag in xml_object.findall('actions/action/attributes/attrib'):
    if tag.attrib['name']=='urlfinalized':
        url= tag.text.replace('%3A',':')
        url= url.replace('%2F','/')
        url = url.replace('%23','#')
        urls.append(url)
#extract the time from xml tree object
spend_time=[]
for tag in xml_object.findall('actions/action/event/replayhints/hint'):
    if tag.attrib['name']=='thinktime':
        spend_time.append(tag.text)
#create a data fame to attach links and times
data_frame= pd.DataFrame(
    {'URL': urls,
     'Sepnd_time': spend_time,
      })
data_frame.to_csv('C:/Users/Moji/Desktop/dejackick.csv', index=False, encoding='utf-8') 
       