
from telethon import TelegramClient
from AI import *
from telethon import functions
from telethon import events

# Use your own values from my.telegram.org
api_id = 1234
api_hash = '213'



def minedOrNot(txt):  # -2 bomb      -1 not yet discovered

    if ord(txt) == 11036:
        return -1
    if ord(txt) - 48 > 0 and ord(txt) - 48 <= 8:
        return ord(txt) - 48
    if ord(txt) == 32:
        return 0
    return -2


def extract_info(reply_markup):
    table = [[0 for i in range(7)] for j in range(8)]
    for i in range(8):
        for j in range(7):
            table[i][j] = minedOrNot(reply_markup.rows[i].buttons[j].text[0])
    return table

address="@opponent_user"

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    @events.register(events.MessageEdited(chats=address))
    async def handler(event):
        print("I understand")
        if "Saber" in event.text:
            print("I understand Saber")
            minesTable = extract_info(event.reply_markup)
            decission = decide(minesTable)
            print("my :", decission)
            result = await client(functions.messages.GetBotCallbackAnswerRequest(
                peer=address,
                msg_id=event.id,
                data=event.reply_markup.rows[decission[0]].buttons[decission[1]].data
            ))



    client.add_event_handler(handler)

    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()

