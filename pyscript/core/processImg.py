from math import sqrt
from PIL import Image
import numpy as np

MODE = {
  "VARIANCE":1,
  "AVERAGE":2,
}
COLORS_m_ = {
  "0":(240,240,240),
  "1":(242,178,51),
  "2":(229,127,216),
  "3":(153,178,242),
  "4":(222,222,108),
  "5":(127,204,25),
  "6":(242,178,204),
  "7":(76,76,76),
  "8":(153,153,153),
  "9":(76,153,178),
  "a":(178,102,204),
  "b":(51,102,204),
  "c":(127,102,76),
  "d":(87,166,78),
  "e":(204,76,76),
  "f":(17,17,17),
}

def getSimilar(rgbarr,mode=MODE["AVERAGE"]):
  similars = {}
  for char,val in COLORS_m_.items():
    sum = 0
    if(mode==MODE["AVERAGE"]):
      for i in [0,1,2]:
        sum+=abs(val[i]-rgbarr[i])
      similars[char]=sum/3
    elif(mode==MODE["VARIANCE"]):
      for i in [0,1,2]:
        sum+=abs(val[i]-rgbarr[i])**2
      similars[char]=sqrt(sum)/3
    else:
      pass
  retc = ""
  minv = 9999999
  for c,v in similars.items():
    if v<minv:
      retc = c
      minv = v
  return retc

'''
def main():
  img = Image.open("..\\gzy.jpg").convert("RGB")
  imgsize = img.resize(DISPSIZE)
  imgsize.save("..\\outsize.jpg")
  colorarr = np.asarray(imgsize)
  arr = colorarr.tolist()
  towstr = ""
  for row in arr:
    for col in row:
      towstr+=getSimilar(col)
    towstr+='\n'
  print(towstr)
  with open("..\\output.nft","w",encoding="utf-8") as f:
    f.write(towstr)
main()
'''