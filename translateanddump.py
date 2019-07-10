#!/usr/bin/env python
# coding: utf-8

# In[23]:


import configparser
from googletrans import Translator
import json
import codecs


# In[32]:


# Imports the Google Cloud client library
from google.cloud import translate
# Instantiates a client
translate_client = translate.Client()

def get_gcp_translations(text, target):
    # Translates some text into Russian
    translation = translate_client.translate(
      text,
      target_language=target)
    return translation['translatedText']

def get_translations(arg):
    translations = translator.translate(arg, dest='ja')
    return(translations.text)

def get_str(arg):
    res =[]
    trans_target = 'ja'
    if isinstance(arg, str):
        arg = get_gcp_translations(arg, trans_target)
    elif isinstance(arg, list):
        for i in range(len(arg)):
            if isinstance(arg[i], str):
                arg[i] = get_gcp_translations(arg[i], trans_target)
            else:
                get_str(arg[i])
    elif isinstance(arg, dict):
        for k, v in arg.items():
            if isinstance(v, str):
                arg[k]=get_gcp_translations(v, trans_target)
            else:
                get_str(v)
    return res


# In[34]:


if __name__ == "__main__":
    # load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    inputfile = config['default']['inputfile']
    outputfile = config['default']['outputfile']
    translator = Translator()

    with open(inputfile, encoding='utf-8') as f:
        data = json.load(f)
        stringvalue = get_str(data)
        f.close()
    
    print(data)
    
    with codecs.open(outputfile, "w", "utf-8") as fh:
       # fh = open(outputfile,'w', encoding='utf-8')
       json.dump(data,fh,indent=4,ensure_ascii=False)
       fh.close()

