# Dev Discord Bot
Dev Discord Bot is a Python bot built for interacting with users on Discord. It comes with a set of useful features to enhance your Discord server experience. This bot is a bit different from the others because it uses different APIs from webpages and allow users to get data from them.

## Features

- **!miau ping**: It checks the latency.
- **!miau cat**: Retrieves a photo or gif of a cat.
- **!miau horoscopo**: Provides astrological indications (joke).
- **!miau help**: Displays the list of available commands.
- **!miau malda**: Retrieves information from the Cinema Malda API.
- **!miau ping**: Checks the latency of the bot.
- **!miau stalk**: Stalks Instagram profiles.
- **!miau notify**: Allows users to submit ideas or report some bugs.
- **!miau animeflv**: Retrieves information from the animeflv webpage (uses selenium), under development. 

To learn how to use each command, you can use `!miau [command] help`. For example, `!miau cat help` will provide information on how to use the `!miau cat command`. You can also use `!miau help` for general information.

Feel free to explore and experiment with the bot's features!

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/my-awesome-discord-bot.git
   
2. Install the required dependencies
   ```shell
   pip install -r requirements.txt

3. Configure the bot token:
   Create a new bot on the Discord Developer Portal (https://discord.com/developers/applications)
   Copy the bot token
   Find the file "src/TOKEN.json" and paste your token there.
   If the file doesn't exist try to run the index.py once. It will create it.

4. Start the bot
   Run the index.py file.

## License
This project is licensed under the <ins>MIT License</ins>.

Feel free to customize the README further based on your specific Discord bot project's needs.
