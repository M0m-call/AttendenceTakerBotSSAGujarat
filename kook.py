'''
This file assumes that kepacha.png is in the relative path
then extracts text from that using google cloud api
returns capatcha text
'''

from google.cloud import vision
import os 
def kepacha():

  
  #Image.open('kepacha.png')

  
  with open("j.json",'w') as j:
    j.write(os.getenv('KEY'))


  os.environ['GOOGLE_APPLICATION_CREDENTIALS']="j.json"
  #invoking google cloud vision API
  client = vision.ImageAnnotatorClient()
  image = vision.AnnotateImageRequest()
        
  #
      
  with open('kepacha.png', 'rb') as image_file:
      content = image_file.read()
      response = client.text_detection({
          'content': content})
  for r in response.text_annotations:
      d = {
          'text': r.description
      }
  
  #clean file
  os.remove("j.json")

  #return the captcha.
  return d['text']