import nltk
import os
import shutil

path = os.path.abspath(os.getcwd())

if(os.path.isdir(path+'\\nltk_data')):
  shutil.rmtree(path+'\\nltk_data')

os.mkdir('nltk_data')

os.environ['NLTK_DATA'] = path+'\\nltk_data'

if('NLTK_DATA' == path+'\\nltk_data'):
  nltk.download('wordnet')
  nltk.download('stopwords')
else:
  print('Failed to set environment variable')