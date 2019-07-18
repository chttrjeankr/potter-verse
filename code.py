import telebot
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
HP_TOKEN = os.getenv('HP_TOKEN')
# print(HP_TOKEN)

bot = telebot.TeleBot(HP_TOKEN) #balderdashBot
df = pd.DataFrame(map(lambda X: map(str.strip,X.split('-')),open('spells.txt')),columns = ['Spells','Reactions'])
print('Ready')

def get_anim(spell):
    file_name = '_'.join(spell.lower().split())+'.gif'
    user = "chttrjeankr"
    repository = "potter-verse"
    branch = "master"
    file_path = "gifs"
    link = f"https://raw.githubusercontent.com/{user}/{repository}/{branch}/{file_path}/{file_name}"
    return link

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	name = message.from_user.first_name
	bot.reply_to(message, "Welcome To Hogwarts, {}\n(not the real one though)".format(name))

@bot.message_handler(func=lambda message: True, content_types=['voice','video_note','document','photo','location','contact'])
def default_handler(message):
	# print(message.json)
	# print()
	bot.reply_to(message,"Can you please type it out? That'd be great.")

@bot.message_handler(func=lambda message: True)
def react(message):
	# print(message)
	# print()
	try:
		spell = df[df['Spells'].str.contains(message.text,case=False)]
		reply = spell['Reactions'].to_list()[0]
		try:
			# anim = df[df['Spells'].str.contains(message.text,case=False)]['GIFs'].to_list()[0]
			spell = spell['Spells'].to_list()[0]
			anim = get_anim(spell)
			print(anim)
			msg = bot.send_document(message.from_user.id, anim)
			print(msg)
		except Exception as e:
			print(e)
			bot.send_message(message.from_user.id,"Let's assume there's something interesting in this message")
	except:
		reply = "I haven't learned that spell yet"
	bot.reply_to(message, reply)


bot.polling()
