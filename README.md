<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">
  
# nonebot_plugin_face2cartoonpic
  
_✨基于腾讯云合成图的以图绘图的Nonebot插件✨_

  ---
  
<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/ANGJustinl/nonebot_plugin_face2cartoonpic" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_face2cartoonpic">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_face2cartoonpic.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
</a>

  
## 💿 安装

### 1. nb-cli安装（推荐）
在你bot工程的文件夹下，运行cmd（运行路径要对啊），执行nb命令安装插件，插件配置会自动添加至配置文件  
```
nb plugin install nonebot_plugin_face2cartoonpic
```

### 2. pip安装
```
pip install nonebot_plugin_face2cartoonpic --upgrade
```  
打开 nonebot2 项目的 ```bot.py``` 文件, 在其中写入  
```nonebot.load_plugin('nonebot_plugin_abstain_diary')```  
  
或在bot路径```pyproject.toml```的```[tool.nonebot]```的```plugins```中添加```nonebot_plugin_face2cartoonpic```即可  
pyproject.toml配置例如：  
``` 
[tool.nonebot]
plugin_dirs = ["src/plugins"]
plugins = ["nonebot_plugin_face2cartoonpic","xxxxx"]
```
