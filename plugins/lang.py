# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  lang.py importado.{/cyan}'))

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add('ESPAÑOL','ENGLISH')

@bot.message_handler(commands=['lang'])
def command_lang(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_message( cid, responses['lang_1'][lang(cid)], reply_markup=markup)
        userStep[cid] = 'lang'
    else:
        bot.send_message( cid, responses['not_user'])