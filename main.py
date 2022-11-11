# coding=utf-8           # -*- coding: utf-8 -*-
from jsmin import jsmin
import os
import re



def minifyC(nameJSFile):

  with open(nameJSFile) as js_file:
    
    try:
      minifiedJSCode = jsmin(js_file.read(), quote_chars="'\"`")
      
      newJSFile = open(nameJSFile, "w")
      newJSFile.write(minifiedJSCode)
      newJSFile.close()
    except:
      print("На этом файле произошла ошибка обработки")
      print("#"*50)
    
def getAllFiles(folder):
  tree = list(os.walk(folder))
  
  for i in tree:
    for x in i[2]:
      if x[0] != ".":
        resultFile = x.split(".")
        if len(resultFile) == 2:
          ef = resultFile[1]
          if (ef == "js") | (ef == "php") | (ef == "css"):
            print(i[0]+"\\"+x)
            minifyC(i[0]+"\\"+x)
        

if __name__ == '__main__':
  getAllFiles("pwa")
