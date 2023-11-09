# Creating Your Bot on Telegram
1. Create a New Bot with BotFather
To create a new Telegram bot, you'll need to interact with BotFather, Telegram's own bot for creating and managing bots.

Start a chat with BotFather: Search for @BotFather in your Telegram app and start a chat.
Create a new bot: Send the /newbot command to BotFather.
Follow the prompts: BotFather will ask for a name for your bot and then a username. The username must end in bot (e.g., minaProtocolBot).
Save your bot token: After the bot is created, BotFather will provide a token. Save this token securely, as you'll need it for your bot configuration.
2. Set Up Bot Commands
You can define commands that users can easily access through the Telegram interface.

Open a chat with BotFather: If you've closed your chat with BotFather, reopen it.

Send the /setcommands command: Choose your bot and send a list of commands and descriptions in this format:

```
start - Starts interaction with the bot
addvalidator - Adds a new validator to monitor
validatorinfo - Retrieves information about the added validators
removevalidator - Removes a validator from the monitoring list
checkbalance - Checks the balance of an account
Replace these with any other commands relevant to your bot.
```
# Configuring the Bot
1. Update config.py in Your Bot Project
In your bot's codebase, locate the config.py file and replace the placeholder for TELEGRAM_TOKEN with the token you received from BotFather.

python
Copy code
TELEGRAM_TOKEN = 'your_telegram_bot_token_here'
# Other configuration settings...
2. Database and API Configuration
Ensure that your database is set up correctly and the connection string is updated in config.py. If you are using external APIs, make sure their endpoints are correctly configured.

Running the Bot
After the configuration, you can run your bot:

Navigate to your bot's project directory.

Run the bot using Python:

```
python main.py
```
Your bot should now be live on Telegram and respond to the configured commands.

Interacting with Your Bot
Search for Your Bot: In Telegram, search for the username you assigned to your bot.
Start a Chat: Start a conversation with your bot and try out the commands you've set up.