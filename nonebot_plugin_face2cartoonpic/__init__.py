from pathlib import Path

import nonebot
from nonebot.typing import T_State
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Message, MessageSegment,MessageEvent
from nonebot.adapters.onebot.v11.helpers import extract_image_urls
from nonebot.params import Arg
from nonebot.log import logger

from .limiter import limiter
from .tencentapi import get_pic
#=
from nonebot.plugin import PluginMetadata
__plugin_meta__ = PluginMetadata(
    name='人像变换',
    description='基于腾讯云的face2cartoon',
    usage='''人像变换/facechange/fc + 人像图片/回复有人像消息
    注：使用前需配置api的key,发送的图片需为人像''',
    extra={
        "version": "0.2.9",
        "repository": "https://github.com/ANGJustinl/nonebot_plugin_face2cartoonpic_main"
    }
)
#=
fc = on_command('人像变换',aliases={'facechange','fc'}, priority=5, block=True)

@fc.handle()
async def image2comic(event: MessageEvent, matcher: Matcher):
    message = reply.message if (reply := event.reply) else event.message
    if imgs := message["image"]:
        matcher.set_arg("imgs", imgs)
   
@fc.got("imgs", prompt="请发送用于启动的原图")
async def get_image(state: T_State, imgs: Message = Arg()):
    urls = extract_image_urls(imgs)
    if not urls:
        await fc.finish("没有找到图片,请重新启动并在启动语句后添加图片")
        
    state["urls"] = urls

@fc.handle()
async def _handle(matcher: Matcher,event: MessageEvent,state: T_State):
    
    user_id = event.user_id
    if not limiter.check(user_id):
        left_time = limiter.left_time(user_id)
        await matcher.finish(f'我知道你急了.但是你先别急,cd还有{left_time}秒')
        return 
    url_input = state["urls"][0]
    msg_raw = await get_pic(url_input)

    if msg_raw == 1:
        logger.error("画图失败,没有设置Secret_key\n error1")
        await fc.finish("寄，画图失败了,没有设置Secret_key", reply_message=True) 
    if msg_raw == 2:
        logger.error("画图失败,输入的不是人像\n error2")
        await fc.finish("寄，画图失败了,输入的不是人像(或api密钥错误)", reply_message=True)

    limiter.start_cd(user_id)
    url = msg_raw
    await fc.send(url)
    await fc.finish(MessageSegment.image(file=url, cache=False), at_sender=True)

_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").
    resolve()))