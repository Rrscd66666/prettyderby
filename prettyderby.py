from asyncio.windows_events import NULL
import emoji
import json
from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from asyncio import events
from asyncore import read
from cgi import test
from cgitb import reset
import json
from math import fabs
import random
from sre_constants import SUCCESS
from tkinter import E, Place
from unittest import result
from venv import create
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from nonebot.matcher import Matcher
from nonebot.plugin import on_command
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.adapters.onebot.v11 import MessageSegment


global pretty,playInfo,info1,info2,info3,info4,Qid
info1="1;1;1"
info2="2;2;2"
info3="3;3;3"
info4="1;4;4;4"
Qid=''
pretty=[]

playInfo={
    "id":"",
    "derbyMsg":"",
    "carMsg":"",
    "qid":""
}

def saveInfo():#读取信息
    with open("D:\python\Pretty"+'.json', 'w') as fp:
        json.dump(pretty, fp)
        fp.close()
 
def readInfo():#存储信息
    with open("D:\python\Pretty"+'.json', 'r') as fp:
        global pretty
        pretty=json.load(fp)
        fp.close()       

def strChange(info):#分解数据方便存储
    infoList=info.split(";")
    return infoList

def addInfo(info):#添加信息到数组里面
    try:
        readInfo()
    except Exception as e:
        saveInfo()
        readInfo()

    List=strChange(info)
    playInfo["id"]=List[0]
    playInfo["derbyMsg"]=List[1]
    playInfo["carMsg"]=List[2]
    # global Qid
    playInfo["qid"]=Qid
    pretty.append(playInfo)
    saveInfo()

def updateInfo(info):#添加信息到数组里面
    try:
        readInfo()
    except Exception as e:
        saveInfo()
        readInfo()
    
    List=strChange(info)
    if Qid==pretty[int(List[0])-1]["qid"] or Qid=="1743107384":    
        playInfo["id"]=List[1]
        playInfo["derbyMsg"]=List[2]
        playInfo["carMsg"]=List[3]
        playInfo["qid"]=Qid
        # print(int(List[0]))
        pretty[int(List[0])-1]=playInfo
        # print("1sd23")
        saveInfo()
        return "更新成功"  
    else: 
        return "你无权更新他人信息"  
    # print(pretty)
def showInfo():
    strInfo=emoji.emojize("    :large_blue_diamond:信息列表:large_blue_diamond:\n-----------------------------")
    try:
        readInfo()
        
        uid=0
    except Exception as e:
        saveInfo()
        readInfo()  
        return strInfo    
    for info in pretty:
        uid+=1
        strInfo+="\n🔍:"+str(uid)+"\n"+"🆔:"+info["id"]+"\n"+"🏵️:"+info["derbyMsg"]+"\n"+"♦️:"+info["carMsg"]+"\n-----------------------------"
    return strInfo    
def delInfo(index):
    try:
        readInfo()
    except Exception as e:
        saveInfo()
        readInfo()
    try:
        if Qid==pretty[index-1]["qid"] or Qid=="1260998824":        
            del pretty[index-1]
            saveInfo()
            return "删除成功"  
        else:
            return "你无权删除他人信息"    
    except Exception as es:
        print("delError")       

weather = on_command(cmd="upload", priority=2,block=True)
@weather.handle()
async def get_Qid(bot:Bot,event:Event):
    global Qid
    Qid=str(event.get_user_id())

@weather.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值

@weather.got("city", prompt="示例   /upload id;因子描述;支援卡")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    try:
        addInfo(city_name)
        # city_weather = await showInfo()
        await weather.send("添加成功")
    except Exception as e:
        await weather.send("")    


delInfoF = on_command("del",priority=50)
@delInfoF.handle()
async def get_Qid(bot:Bot,event:Event):
    global Qid
    Qid=str(event.get_user_id())

@delInfoF.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值

@delInfoF.got("city", prompt="示例   /del index ")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    try:
        result=delInfo(int(city_name))
        await delInfoF.send(result) 
    except Exception as e:
        await delInfoF.send("") 


showInfoF = on_command("info",priority=50)
@showInfoF.handle()
async def showInfoX(bot:Bot,event:Event):
    await showInfoF.send(showInfo()) 
    


updateInfoF = on_command("update",priority=50)
@updateInfoF.handle()
async def get_Qid(bot:Bot,event:Event):
    global Qid
    Qid=str(event.get_user_id())
@updateInfoF.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("city", args)  # 如果用户发送了参数则直接赋值

@updateInfoF.got("city", prompt="示例   /upload 序号;id;因子描述;支援卡")
async def handle_city(city: Message = Arg(), city_name: str = ArgPlainText("city")):
    try:
        result=updateInfo(city_name)
        await delInfoF.send(result)
    except Exception as e:
        await delInfoF.send("") 

showMenu = on_command("menu",priority=50)
@showMenu.handle()
async def showInfoX(bot:Bot,event:Event):
    await showMenu.send(emoji.emojize("      :large_blue_diamond:菜单:large_blue_diamond:\n      ---------------\n💫查看: /info\n💫上传:  /upload \n💫更新:  /upload \n💫删除:  /del\n💫规则:  /rule    ")) 


showRule = on_command("rule",priority=50)
@showRule.handle()
async def showInfoX(bot:Bot,event:Event):
    await showRule.send("      🐎填写规范例子🐎      \n\n💬因子规范: 几_几_\n💬支援规范: 几破_ _\n💬例 6速3耐 三破海湾")
# print(showInfo)
# updateInfo(info4)
# print(showInfo)
