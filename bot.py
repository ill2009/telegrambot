import datetime
import os
import time

import requests
import telegram
from dotenv import load_dotenv

load_dotenv()

def weather():
    url='https://wttr.in'
    parameters={
        'format':2,
        'M':'',
    }
    response=requests.get(url,params=parameters)
    return response.text

def send_message(text) :
    telegramtoken=os.getenv('telegramtoken')
    bot=telegram.Bot(token=telegramtoken)
    Id= int(os.getenv('Id'))
    bot.send_message(chat_id=Id,text=text)
    return
def proverka(today):
    a=weather()
    if today == 1:
        timetable=open ('вторник.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет, Илья, вот твоё расписание на вторник: {timetable},\n погода на завтра : \n {a}'
        send_message(message)
    if today == 2:
        timetable=open ('среда.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет, Илья, вот твоё расписание на среду: {timetable},\n погода на завтра : \n {a}'
        send_message(message)
    if today == 3:
        timetable=open ('четверг.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет, Илья, вот твоё расписание на четверг: {timetable},\n погода на завтра : \n  {a}'
        send_message(message)
    if today == 4:
        timetable=open ('пятница.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет, Илья, вот твоё расписание на пятницу: {timetable},\n погода на завтра : \n {a}'
        send_message(message)
    if today == 5:
        timetable=open ('суббота.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на субботу: {timetable}, \n погода на завтра : \n {a}'
        send_message(message)
    if today == 6:
        timetable=open ('воскресенье.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на воскресенье: {timetable}, \n погода на завтра : \n {a}'
        send_message(message) 
    if today == 0:
        timetable=open ('понедельник.txt','r',encoding='utf-8')
        timetable=timetable.read()
        message=f'Привет Илья, вот твоё расписание на понедельник: {timetable},\n погода на завтра :  \n {a}'
        send_message(message)
def main():
    run = True
    while run:
        weekday=datetime.datetime.today().weekday()
        now=datetime.datetime.now()
        day=now.replace(hour=6,minute=30)
        if now==day:
            proverka(weekday)
            time.sleep(60)

    

if __name__ == '__main__':
    main()
