import os

RUMTIME = {
  "js2py":"js2py",
  "pillow":"PIL",
  "numpy":"numpy"
}

def installRuntime():
  for libn,impn in RUMTIME.items():
    try:
      __import__(impn)
    except:
      os.system(f"python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {libn}")
  