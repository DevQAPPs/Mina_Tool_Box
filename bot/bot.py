from telegram.ext import Updater, CommandHandler
import handlers
from config import TELEGRAM_TOKEN

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Registering command handlers
    dp.add_handler(CommandHandler("start", handlers.start))
    dp.add_handler(CommandHandler("addvalidator", handlers.add_validator))
    dp.add_handler(CommandHandler("validatorinfo", handlers.validator_info))
    dp.add_handler(CommandHandler("removevalidator", handlers.remove_validator))
    dp.add_handler(CommandHandler("checkbalance", handlers.check_balance))

    # Starting the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
