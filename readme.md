# 适用于CC电脑的NFT格式图片转换器

## 简介

这个项目是为了在CC电脑上显示图片

本程序“能用就行”，由临时写成的`Python`脚本套上GUI而来

欢迎各位大神二创&改进

有新的想法或建议可以在此处或[我的Bilibili账号](https://space.bilibili.com/521215943)告诉我

## 使用说明

其实图形化界面就很直观了

但是有几点需要注意：

 - 建议将显示屏的缩放设为最小(`0.5`)，即执行`<device>.setTextScale(0.5)`
 - 程序中所需要的大小用`<device>.getSize()`获取，输出分别为`x`和`y`

一个电脑中的示例`lua`绘图程序如下：

**注意：需要把示例程序中对应显示屏方向替换成实际使用方向**

```lua
-- startup.lua
-- 此程序开机自启动
shell.run("monitor right draw");
```

```lua
-- draw.lua
term.clear(); --清屏
term.setCursorPos(1,1); --设置光标位置
local p = peripheral.wrap("right"); --包装显示屏外设
p.setTextScale(0.5); --设置分辨率最高
local img = paintutils.loadImage("output.nft"); --加载图片文件
paintutils.drawImage(img,1,1); --绘制图片
```

本程序是支持多语言的，只要添加对应的语言文件`lang/xxx.json`，并在`settings.json`里设置

本程序除了标准的`ComputerCraft`颜色预设，也能支持用户自定义的颜色预设

## 备注&补充
 - (20230122) 英文语言文件还没有做好（目前只支持中文），后续会完善... 我也只是初三学生，英语水平并不高，欢迎大佬提供专业翻译 o(*￣▽￣*)ブ
 - (20230122) 还没有构建exe，可以手动执行`main.py`来使用，第一次使用可能会弹出命令窗口自动安装所需的`Python`模块（默认使用清华镜像源）

