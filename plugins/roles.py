# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  roles.py importado.{/cyan}'))

changeds = {
    'Chogath': 'ChoGath',
    'FiddleSticks': 'Fiddlesticks',
    'Leblanc': 'LeBlanc',
    'Khazix': 'KhaZix',
    'MonkeyKing': 'Wukong'
}

@bot.message_handler( func=lambda message: message.text=="CAMPEONES" or message.text=="CHAMPIONS" )
@bot.message_handler(commands=['champs'])
def command_champs(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['champs'][lang(cid)]
        for (k, v) in sorted(data[lang(cid)].items(), key=lambda x: x[1]['name']):
            if k in changeds:
                txt += '\n/' + changeds[k] + ' ' + v['title']
            else:
                txt += '\n/' + k + ' ' + v['title']
        bot.send_message( cid, txt)
    else:
        bot.send_message( cid, responses['not_user'])

@bot.message_handler( func=lambda message: message.text=="POSICIONES" or message.text=="ROLES" )
@bot.message_handler(commands=['roles'])
def command_roles(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['roles_1'][lang(cid)]
        for rol in responses['roles_2'][lang(cid)]:
            txt += '\n/' + rol + ': ' + responses['roles_2'][lang(cid)][rol]
        bot.send_message( cid, txt, parse_mode="Markdown")
    else:
        bot.send_message( cid, responses['not_user'])


@bot.message_handler( func=lambda message: message.text=="ASESINOS" or message.text=="ASSASSINS" )
@bot.message_handler(commands=['assassins'])
def command_assassins(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['champs'][lang(cid)]
        for (k, v) in sorted(data[lang(cid)].items(), key=lambda x: x[1]['name']):
            if 'Assassin' in v['tags']:
                if k in changeds:
                    txt += '\n/' + changeds[k] + ' ' + v['title']
                else:
                    txt += '\n/' + k + ' ' + v['title']
        bot.send_message( cid, txt)
    else:
        bot.send_message( cid, responses['not_user'])

@bot.message_handler( func=lambda message: message.text=="LUCHADORES" or message.text=="FIGHTERS" )
@bot.message_handler(commands=['fighters'])
def command_fighters(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['champs'][lang(cid)]
        for (k, v) in sorted(data[lang(cid)].items(), key=lambda x: x[1]['name']):
            if 'Fighter' in v['tags']:
                if k in changeds:
                    txt += '\n/' + changeds[k] + ' ' + v['title']
                else:
                    txt += '\n/' + k + ' ' + v['title']
        bot.send_message( cid, txt)
    else:
        bot.send_message( cid, responses['not_user'])

@bot.message_handler( func=lambda message: message.text=="MAGOS" or message.text=="MAGES" )
@bot.message_handler(commands=['mages'])
def command_mages(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['champs'][lang(cid)]
        for (k, v) in sorted(data[lang(cid)].items(), key=lambda x: x[1]['name']):
            if 'Mage' in v['tags']:
                if k in changeds:
                    txt += '\n/' + changeds[k] + ' ' + v['title']
                else:
                    txt += '\n/' + k + ' ' + v['title']
        bot.send_message( cid, txt)
    else:
        bot.send_message( cid, responses['not_user'])

@bot.message_handler( func=lambda message: message.text=="APOYOS" or message.text=="SUPPORTS" )
@bot.message_handler(commands=['supports'])
def command_supports(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['champs'][lang(cid)]
        for (k, v) in sorted(data[lang(cid)].items(), key=lambda x: x[1]['name']):
            if 'Support' in v['tags']:
                if k in changeds:
                    txt += '\n/' + changeds[k] + ' ' + v['title']
                else:
                    txt += '\n/' + k + ' ' + v['title']
        bot.send_message( cid, txt)
    else:
        bot.send_message( cid, responses['not_user'])

@bot.message_handler( func=lambda message: message.text=="TANQUES" or message.text=="TANKS" )
@bot.message_handler(commands=['tanks'])
def command_tanks(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['champs'][lang(cid)]
        for (k, v) in sorted(data[lang(cid)].items(), key=lambda x: x[1]['name']):
            if 'Tank' in v['tags']:
                if k in changeds:
                    txt += '\n/' + changeds[k] + ' ' + v['title']
                else:
                    txt += '\n/' + k + ' ' + v['title']
        bot.send_message( cid, txt)
    else:
        bot.send_message( cid, responses['not_user'])

@bot.message_handler( func=lambda message: message.text=="TIRADORES" or message.text=="ADCS" )
@bot.message_handler(commands=['adcs'])
def command_adcs(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['champs'][lang(cid)]
        for (k, v) in sorted(data[lang(cid)].items(), key=lambda x: x[1]['name']):
            if 'Marksman' in v['tags']:
                if k in changeds:
                    txt += '\n/' + changeds[k] + ' ' + v['title']
                else:
                    txt += '\n/' + k + ' ' + v['title']
        bot.send_message( cid, txt)
    else:
        bot.send_message( cid, responses['not_user'])