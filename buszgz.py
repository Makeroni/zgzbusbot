#!/usr/bin/env python
# coding=utf-8

# buszgz.py

import telebot
import suds
import urllib2
import json
from BeautifulSoup import BeautifulSoup
bot = telebot.TeleBot("287844347:AAHlT-xf3HQxP4mnhTh745bqkqM2ePksH2Y")

#http://www.dndzgz.com/web/api.html
# http://www.dndzgz.com/fetch?service=###servicio###
# http://www.dndzgz.com/fetch?service=bus
# http://www.dndzgz.com/point?service=###servicio###&id=###id###
# http://www.dndzgz.com/point?service=bus&id=888

# # url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
url = 'http://www.dndzgz.com/point?service=bus&id=888'
response = urllib2.urlopen(url)
html = response.read()
html = json.loads(html)
html = html['items']
html = json.dumps(html)
html = html.replace('\u00f3', 'ó')
html = html.replace(']]', '')
html = html.replace('[[', '')
html = html.replace('"], ["', '\n')
html = html.replace('", "', '; ')
html = html.replace('"', '')
html = html.replace('None min', '0 min')
html = html.replace('[', '')
html = html.replace(']', ':')
# html = BeautifulSoup(response.read().decode('utf-8'))
print html

# \u00e1 -> á
# \u00e9 -> é
# \u00ed -> í
# \u00f3 -> ó
# \u00fa -> ú
# \u00c1 -> Á
# \u00c9 -> É
# \u00cd -> Í
# \u00d3 -> Ó
# \u00da -> Ú
# \u00f1 -> ñ
# \u00d1 -> Ñ

# request = urllib2.Request(url)
# request.add_header('Accept-Encoding', 'ISO-8859-1')
# response = urllib2.urlopen(request)
# # html = response.read()
# html = BeautifulSoup(response.read().decode('ISO-8859-1'))
# print html

# from suds.client import Client
# client = Client(url)
# print client

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Escribe el numero de parada sobre el que te quieres informar")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	html="Creo que se ha producido un error"
	try:
		url = 'http://www.dndzgz.com/point?service=bus&id='+message.text
		response = urllib2.urlopen(url)
		html = response.read()
		html = json.loads(html)
		html = html['items']
		html = json.dumps(html)
		html = html.replace('\u00f3', 'ó')
		html = html.replace(']]', '')
		html = html.replace('[[', '')
		html = html.replace('"], ["', '\n')
		html = html.replace('", "', '; ')
		html = html.replace('"', '')
		html = html.replace('None min', '0 min')
		html = html.replace('[', '')
		html = html.replace(']', ':')
	except urllib2.HTTPError, e:
		print('HTTPError = ' + str(e.code))
	except urllib2.URLError, e:
		print('URLError = ' + str(e.reason))
	except httplib.HTTPException, e:
		print('HTTPException')
	bot.reply_to(message, html)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

# @bot.message_handler(commands=['convert']) 
# def command_convert(message):
# 	cid = message.chat.id
# 	html="Creo que se ha producido un error"
# 	try:
# 		url = 'http://www.dndzgz.com/point?service=bus&id='+message.text
# 		response = urllib2.urlopen(url)
# 		html = response.read()
# 		html = json.loads(html)
# 		html = html['items']
# 		html = json.dumps(html)
# 		html = html.replace('\u00f3', 'ó')
# 		html = html.replace(']]', '')
# 		html = html.replace('[[', '')
# 		html = html.replace('"], ["', '\n')
# 		html = html.replace('", "', '; ')
# 		html = html.replace('"', '')
# 		html = html.replace('None min', '0 min')
# 		html = html.replace('[', '')
# 		html = html.replace(']', ':')
# 	except urllib2.HTTPError, e:
# 		print('HTTPError = ' + str(e.code))
# 	except urllib2.URLError, e:
# 		print('URLError = ' + str(e.reason))
# 	except httplib.HTTPException, e:
# 		print('HTTPException')
# 	bot.send_message(cid, html)

# bot.polling()
bot.polling(none_stop=True, interval=0)

