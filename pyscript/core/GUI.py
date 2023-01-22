import tkinter as tk
import tkinter.ttk as ttk
import tkinter.tix as tix
import tkinter.scrolledtext as stext
import tkinter.filedialog as filedialog
from PIL import Image,ImageTk
import math

import os.path as path
from core.settings import Settings
from core.version import *
from core.win.InfoShower import InfoShower
from core.processImg import processImg
from core.presets import Preset

class App():
  def __init__(self,config,root=tix.Tk()):
    self.root=root
    self.config=config
    self.langFull = Settings(path.join(
      self.config.getConfig("lang.home"),self.config.getConfig("lang.default")
      ))
    self.lang = self.langFull.getSubSettings(["GUI",])
    
    self.root.mconf = self.config.getSubSettings(["GUI","main"])
    self.winconf = self.config.getSubSettings(["GUI","window"])
    self.root.title(self.lang.gc("main.title"))
    self.root.geometry("{0}x{1}+{2}+{3}".format(
      self.root.mconf.gc("width"),
      self.root.mconf.gc("height"),
      self.root.mconf.gc("xoffset"),
      self.root.mconf.gc("yoffset"),
      ))
    
    self.nb = ttk.Notebook(self.root)
    self.nb.pack(fill=tk.BOTH)
    
    self.home()
    self.info()
    self.uplog()
  def home(self):
    #主页面
    self.phome = ttk.Frame(self.nb)
    self.nb.add(self.phome,text=self.lang.gc("home.title"))
    
    # ------------ 软件介绍区 ----------------------------
    self.phome.descf = tk.LabelFrame(self.phome,text=self.lang.gc("home.descTitle"))
    self.phome.descf.grid(row=1,column=1)
    self.phome.descf.st = stext.ScrolledText(self.phome.descf,width=14,height=10,wrap=tk.WORD)
    self.phome.descf.st.insert(tk.END,self.langFull.gc("description"))
    self.phome.descf.st.pack(fill=tk.BOTH)
    
    # ------------ 按钮控制区 ----------------------------
    self.phome.btnf = ttk.LabelFrame(self.phome,text=self.lang.gc("home.btnFrame"))
    self.phome.btnf.grid(row=2,column=1,sticky="nsew")
    tk.Button(self.phome.btnf,text=self.lang.gc("home.btns.run"),command=lambda:self.process()).pack(fill=tk.X)
    tk.Button(self.phome.btnf,text=self.lang.gc("home.btns.refresh"),command=lambda:self.btn_refresh()).pack(fill=tk.X)
    tk.Button(self.phome.btnf,text=self.lang.gc("home.btns.exit"),command=lambda:self.root.destroy()).pack(fill=tk.X)
    
    # ------------ 文件输入区 ----------------------------
    self.phome.finf = tk.LabelFrame(self.phome,text=self.lang.gc("home.fin.title"))
    self.phome.finf.grid(row=1,column=2,sticky="nesw")
    self.inputfn = tk.StringVar(value=self.lang.gc("home.defaultFn"))
    self.phome.finf.sf = tk.Frame(self.phome.finf)
    self.phome.finf.sf.pack(fill=tk.X)
    self.finput = tk.Entry(self.phome.finf.sf,width=30,textvariable=self.inputfn)
    self.finput.pack(side=tk.LEFT,fill=tk.Y)
    tk.Button(self.phome.finf.sf,text=self.lang.gc("home.choose"),command=lambda:self.btn_refresh(lambda:self.inputfn.set(filedialog.askopenfilename(
      title=self.lang.gc("home.filedialog.title"),initialdir="C:\\",
      filetypes=[(self.lang.gc("home.filedialog.photof"),".jpg .png .jpeg"),(self.lang.gc("home.filedialog.allf"),"*")]
    )))).pack(side=tk.LEFT,fill=tk.Y)
    self.finput.sh = tk.Label(self.phome.finf)
    self.finput.sh.pack(fill=tk.X)
    
    # ------------ 转换设置区 ----------------------------
    self.psize = {
      "x":tk.IntVar(value=50),
      "y":tk.IntVar(value=50)
    }
    
    # ------------ 文件输出区 ----------------------------
    self.outputfn = tk.StringVar(value=self.lang.gc("home.defaultFn"))#其实是一个文件夹
    self.phome.foutf = tk.LabelFrame(self.phome,text=self.lang.gc("home.fout.title"))
    self.phome.foutf.grid(row=2,column=2,sticky="nesw")
    self.phome.foutf.sf = tk.Frame(self.phome.foutf)
    self.phome.foutf.sf.pack(fill=tk.X)
    self.foutput = tk.Entry(self.phome.foutf.sf,width=30,textvariable=self.outputfn)
    self.foutput.pack(side=tk.LEFT,fill=tk.Y)
    tk.Button(self.phome.foutf.sf,text=self.lang.gc("home.choose"),command=lambda:self.outputfn.set(
      filedialog.askdirectory(
        title=self.lang.gc("home.filedialog.title"),initialdir="C:\\"
      )
      )).pack(side=tk.LEFT,fill=tk.Y)
    self.szframe = tk.LabelFrame(self.phome.foutf,text=self.lang.gc("home.fout.size"))
    self.szframe.pack(fill=tk.X)
    tk.Label(self.szframe,text="x").grid(row=1,column=1)
    tk.Entry(self.szframe,textvariable=self.psize["x"]).grid(row=2,column=1)
    tk.Label(self.szframe,text="y").grid(row=1,column=2)
    tk.Entry(self.szframe,textvariable=self.psize["y"]).grid(row=2,column=2)
    self.foutput.sh = tk.Label(self.phome.foutf)
    self.foutput.sh.pack(fill=tk.X)
  def process(self):
    img = self.finput.img
    with open(path.join(
      self.config.gc("presets.home"),
      self.config.gc("presets.default")
    ),"r",encoding="utf-8") as f:
      preset = f.read()
    size = [self.psize["x"].get(),self.psize["y"].get()]
    cont = processImg(img,size,Preset(preset).getColor(),self.config.gc("process.mode"))
    with open(path.join(self.outputfn.get(),"output.nft"),"w",encoding="utf-8") as f:
      f.write(cont)
  def btn_refresh(self,callpre=lambda:1):
    callpre()
    self.finput.img = Image.open(self.inputfn.get()).convert("RGB")
    # self.finput.toshow_img = self.finput.img.resize([
    #   math.ceil(self.finput.img.height * self.config.gc("GUI.info.photoScaleRate")),
    #   math.ceil(self.finput.img.width  * self.config.gc("GUI.info.photoScaleRate"))
    # ])
    self.finput.toshow_img = self.finput.img.resize(
      self.config.gc("GUI.info.labelPhotoSize")
    )
    self.finput.sh.mimg = ImageTk.PhotoImage(self.finput.toshow_img)
    self.finput.sh.config(image=self.finput.sh.mimg)
    
    
  def info(self):
    #信息页面
    self.pinfo = ttk.Frame(self.nb)
    self.nb.add(self.pinfo,text=self.lang.gc("info.title"))
    
    self.infoshower = InfoShower(self.pinfo)
    self.infoshower.getContainer().pack(fill=tk.BOTH)
    
    infoma = {
      self.lang.gc("info.shower.author"):
        self.readonlyMultiText(self.infoshower,"DouNsM"),
      self.lang.gc("info.shower.version"):
        self.readonlyMultiText(self.infoshower,"{0}\n{1}".format(
          self.lang.gc("info.shower.vver")+VERSION["version"],
          self.lang.gc("info.shower.vdat")+VERSION["date"]
        )),
      self.lang.gc("info.shower.todo"):
        self.readonlyMultiText(self.infoshower,"未来的新功能，有好的建议可以在Bilibili或本项目的Github上提出来\n项目Github地址：{0}\n{1}\n{2}".format(
          "","-"*10,"\n".join(map(lambda s:" - {}".format(s),TD_LIST))
        ))
    }
    self.infoshower.refresh(infoma)
  
  def readonlyMultiText(self,infos,text):
    s = stext.ScrolledText(infos.getRoot(),
      width=self.winconf.gc("scrolledText.width"),
      height=self.winconf.gc("scrolledText.height"),
      
      )
    s.insert(tk.END,text)
    return s
  
  def uplog(self):
    #更新日志界面
    self.puplog = ttk.Frame(self.nb)
    self.nb.add(self.puplog,text=self.lang.gc("uplog.title"))
    self.uplogshower = InfoShower(self.puplog)
    self.uplogshower.getContainer().pack(fill=tk.BOTH)
    logs = {}
    rev_logs = list(UPDATE_LOG.items());
    rev_logs.reverse()
    for (k,v) in rev_logs:
      logs[k]=self.readonlyMultiText(self.uplogshower,v)
    self.uplogshower.refresh(logs)
    
  def mainloop(self):
    self.root.mainloop()