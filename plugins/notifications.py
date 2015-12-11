# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  notifications.py importado.{/cyan}'))

@bot.message_handler( func=lambda message: message.text=="NOTIFICACIONES" or message.text=="NOTIFICATIONS" )
@bot.message_handler(commands=['notify'])
def command_notify(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        if users[str(cid)]['notify']:
            bot.send_message( cid, responses['notifications_1'][lang(cid)], parse_mode="Markdown")
            users[str(cid)]['notify'] = False
        else:
            bot.send_message( cid, responses['notifications_2'][lang(cid)], parse_mode="Markdown")
            users[str(cid)]['notify'] = True
        with open('usuarios.json', 'w') as f:
            json.dump( users, f)
    else:
        bot.send_message( cid, responses['not_user'])