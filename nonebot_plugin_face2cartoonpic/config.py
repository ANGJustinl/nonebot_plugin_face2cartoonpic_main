from pydantic import BaseSettings
import nonebot

class Config(BaseSettings):
    Secret_Id: str = ''  # 腾讯云Secretid
    Secret_Key: str = ''  # 腾讯云SecretKey
    FaceCartoonPic_cd_time: int = 60  # cd时间，单位秒
    class Config:
        extra = "ignore"


global_config = nonebot.get_driver().config
FaceCartoonPic_config = Config(**global_config.dict())  # 载入配置