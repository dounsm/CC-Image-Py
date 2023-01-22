from math import sqrt
from PIL import Image
import numpy as np

MODE = {
  "VARIANCE":1,
  "AVERAGE":2,
}

def getSimilar(rgbarr,COLORS_m_,mode=MODE["AVERAGE"]):
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

def processImg(img,size,colors,mode):
  # print(img,size,colors,mode)
  arr = np.asarray(img.convert("RGB").resize(size)).tolist()
  towstr = ""
  for row in arr:
    for col in row:
      towstr+=getSimilar(col,colors,mode)
    towstr+='\n'
  return towstr
  
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