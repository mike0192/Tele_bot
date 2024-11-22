from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = ''
USERNAME: Final = '@func_work_bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello My Son i am your Dad now')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello i am Dad! Just type something so i can respond to you Son!')

# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there Son!'
    
    if 'how are you' in processed:
        return 'I am alright son, what about you?'
    
    if 'i am good' in processed:
        return 'You have grown so much since i have left you my son'
    
    if 'i love you dad' in processed:
        return 'I love you too my dear Son'
    
    if 'why did you left me' in processed:
        return 'I am very sorry son it is complicated'
    
    return 'I do not understand what you wrote my Son...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id})cin {message_type}: "{text}"')

    if message_type == 'group':
        if USERNAME in text:
            new: str = text.replace(USERNAME, '').strip()
            response: str = handle_response(new)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling....')
    app.run_polling(poll_interval=3)
    
