# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  sales.py importado.{/cyan}'))

@bot.message_handler( func=lambda message: message.text=="OFERTA" or message.text=="SALE" )
@bot.message_handler(commands=['sale'])
def command_sale(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['sale'][lang(cid)] + '\n'
        with open('extra_data/sale.txt', 'rt') as f:
            txt += f.read()
        bot.send_photo( cid, open('extra_data/sale.jpg','rb'))
        bot.send_message( cid, txt)
    else:
        bot.send_message( cid, responses['not_user'])

@bot.message_handler(commands=['update_sale_text'])
def command_update_sale(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_admin(uid):
        bot.send_message( cid, responses['update_sale_text_1'])
        userStep[cid] = 'update_sale_text'

@bot.message_handler(commands=['update_sale_pic'])
def command_update_pic(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_admin(uid):
        bot.send_message( cid, responses['update_sale_pic_1'])
        userStep[cid] = 'update_sale_pic'