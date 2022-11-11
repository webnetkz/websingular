# coding=utf-8           # -*- coding: utf-8 -*-
from jsmin import jsmin
import os



def minifyC(nameJSFile):

  with open(nameJSFile) as js_file:
    
    minifiedJSCode = jsmin(js_file.read(), quote_chars="'\"`")
    
    newJSFile = open(nameJSFile, "w")
    newJSFile.write(minifiedJSCode)
    newJSFile.close()
    
def getAllFiles(folder):
  tree = list(os.walk(folder))
  
  for i in tree:

    # Игнорирует не нужные кталоги
    gitFolder = folder+"\.git"

    if gitFolder in i[0]:
      del i

    # Удаляет пустые кталоги
    elif (not i[1]) & (not i[2]):
      del i 

    else:
      print("Processing folder: ", i[0])
      for x in i[2]:
        pathToFile = i[0]+"\\"+x
        print("Start compression :", pathToFile)
        minifyC(pathToFile)
        print("Finish compression")

if __name__ == '__main__':
  getAllFiles("./pwa/app")
