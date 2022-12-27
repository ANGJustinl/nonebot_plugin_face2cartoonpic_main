<div align="center">
  
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>


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

---  
 </div> 
  
## 💿 安装

### 1. nb-cli安装（推荐）
bot根目录下打开命令行，执行nb命令安装插件，插件配置会自动添加至配置文件  
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
  
## 📖 配置
--- 
  
官方指南 https://cloud.tencent.com/document/product/1202/41796  
  
先到腾讯云这里获取服务资源包 https://console.cloud.tencent.com/ft/resource
  
再去 https://console.cloud.tencent.com/cam/capi 的api密钥管理获取api密钥
  
---
  
bot根目录下.env文件
  
```  
  
Secret_Id = ""这两个写从腾讯云获取的api密钥
  
Secret_Key = ""
  
FaceCartoonPic_cd_time = 60{int}默认60  
  
```  
## 🎉 使用
### 指令表
| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
| 人物变换 + 图片 | 否 | 群聊/私聊 | 对发送的图片启用模型, 支持回复图片 |

使用示例：

    /人物变换 <图像>

**注意**

默认情况下, 您应该在指令前加上命令前缀, 通常是 /
