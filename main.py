#!/usr/bin/env python
# coding: utf-8

# In[5]:


import configparser
from googletrans import Translator
import json


# In[2]:


def get_translations(arg):
    translations = translator.translate(arg, dest='ja')
    return(translations.text)


# In[3]:


def get_str(arg):
    res =[]
    if isinstance(arg, str):
        res.append(arg)
    elif isinstance(arg, list):
        for item in arg:
            res += get_str(item)
    elif isinstance(arg, dict):
        for value in arg.values():
            res += get_str(value)
    return res


# In[7]:


if __name__ == "__main__":
    # load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    inputfile = config['default']['inputfile']
    with open(inputfile, encoding='utf-8') as f:
        data = json.load(f)
        stringvalue = get_str(data)
        f.close()
    translator = Translator()
    for x in stringvalue:
        #print(x)
        print(get_translations(x))


# In[ ]:





# In[ ]:




