import telebot
import Constants as c
import os
import pandas as pd
import browser
import give_list as gl
'''
First I need to take input from user to get the
data of students which are absent today.
'''

#to save output of students in a file named rolling.txt
f = open("rolling.txt", 'w')

#for fetching students name by their numbers

df = pd.read_csv("class1.csv")


def fetch_name(roll_no, df):
    return (list(df.iloc[int(roll_no) + 1]))[1].split(" ")[0]


#creting bot instace
TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

flag = False


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, c.h)


@bot.message_handler(commands=['start'])
def handle_start(message):
    global flag
    flag = True
    bot.send_message(message.chat.id, c.start_msg)


@bot.message_handler(func=lambda x: flag == True and x.text != '/end')
def handle_inscope(message):

    roll_no = message.text.strip().split(',')

    x = 0
    for j in roll_no:
        if j.isdigit() == False:
            bot.reply_to(message, "invalid input")
            x = 1

    if x == 0:
        for j in roll_no:
            f.write(str(j) + ",")
            #f.write(",")
            f.flush()
            print(j)
            bot.send_message(message.chat.id, f"{j} : {str(fetch_name(j,df))}")
        bot.send_message(message.chat.id, "noted")


@bot.message_handler(commands=['end'])
def handle_end(message):
    #close rolling file and dataframe
    f.close()
    global df
    del df
    global flag
    flag = False
    bot.send_message(message.chat.id, c.end_msg)


@bot.message_handler(commands=['update'])
def handle_update(message):
    bot.send_message(message.chat.id, c.update_msg)

    browser.login()

    bot.send_message(message.chat.id, "login success!")

    #bot.send_message(message.chat.id, "captcha suceess")
    browser.update_data(gl.a_student_data())
    bot.send_message(message.chat.id, "data_updated!")

    #taking ScreenShot
    browser.ss()
    photo = open('success.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()

    browser.close()
    bot.send_message(message.chat.id, "Thank You!Done!Come tommorow.")


#start bot...
print("Bot is started...")
bot.polling()
