from PIL import Image,ImageDraw
import numpy as np

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

def main():
  width = 0
  height = 0
  fn = input("Input file: ")
  with open(fn,"r",encoding="utf-8") as f:
    cont = f.read()
  print(cont)
  count=0
  for ch in cont:
    if(ch=='\n'):
      width=count
      count=0
      height+=1
    else:
      count+=1
  print("Size: {}x{}".format(width,height))
  img = Image.new(mode="RGB",size=[width,height])
  draw = ImageDraw.Draw(img)
  xpos=0
  ypos=0
  for ch in cont:
    if(ch=='\n'):
      ypos+=1
      xpos=0
    else:
      draw.point((xpos,ypos),fill=COLORS_m_[ch])
      xpos+=1
  img.save("./re.png")
   
main()