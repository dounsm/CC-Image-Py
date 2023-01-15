# Settings Reading and Writing

import json

class Settings():
  def __init__(self,filepath="?",loads={}):
    self.parsed = {}
    self.gc = self.getConfig
    if(filepath=="?"):
      Settings.parse(loads,self.parsed)
    else:
      self.fp = filepath
      self.load()
  def load(self):
    with open(self.fp,"r",encoding="utf-8") as f:
      self.fcontent = json.loads(f.read())
    Settings.parse(self.fcontent,self.parsed)
  def parse(toparse,todump,pre=""):
    for k,v in toparse.items():
      if(type(v)==dict):
        Settings.parse(v,todump,(pre+"." if pre else "")+k)
      else:
        todump[(pre+"." if pre else "")+k]=v
  def getConfig(self,key):
    return self.parsed[key]
  def getSubSettings(self,originKeys):
    toload = self.fcontent
    for originKey in originKeys:
      toload = toload[originKey]
    return Settings(loads=toload)
  #TODO serialize,dump
    