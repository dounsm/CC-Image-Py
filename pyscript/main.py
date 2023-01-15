from core.runtime import installRuntime
from core.settings import Settings
from core.GUI import App
installRuntime() #安装运行库

config = Settings()
App(config).mainloop()
