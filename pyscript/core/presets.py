# operator for presets

import js2py
from core.settings import Settings

class Preset():
  def __init__(self,filecont:str):
    self.raw = filecont
    self.env = js2py.EvalJs()
    self.env.execute(self.raw)
  def getColor(self):
    return self.env.eval(Settings("./settings.json").gc("presets.entry"))
    
if __name__ == "__main__":
  with open("../presets/ComputerCraft.js","r",encoding="utf-8") as f:
    cont = f.read()
  present = Preset(cont)
  print(present.env.eval("main()"))