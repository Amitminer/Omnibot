# Omnibot

Omnibot is a Discord bot created as my first Python project, marking the beginning of my programming journey. Please keep in mind that this project was developed when I was learning Python, so there might be bugs and limited readability.

## Project Status

This project won't be further enhanced or updated. It serves as a foundational learning experience, showcasing my early efforts in Python programming. While it may have its limitations, it stands as a testament to my progress as a developer.

**If you want to use the latest Discord custom bot, check out: [BhaluBot](https://github.com/Amitminer/Bhalu) coded in PHP.**

## Features

- **Easy Installation:** Omnibot can be set up quickly with just a few simple steps.
- **Customizable Configuration:** Tailor Omnibot's behavior according to your preferences, including setting custom prefixes and owner commands.
- **Rich Command Set:** Enjoy a wide range of commands for moderation, entertainment, utilities, and more.
- **Interactive User Experience:** Omnibot provides interactive and engaging features to keep your server members entertained.

## Installation Guide

### Prerequisites

- **Python:** Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **Discord Bot Token:** Obtain your Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

### Getting Started

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Amitminer888/Omnibot
   cd Omnibot
   ```

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   This command installs all the necessary packages for Omnibot.

3. **Set Up Bot Configuration:**
   Create a `.env` file in the root directory if not exists and add your Discord bot token:
   ```sh
   echo "BOT_TOKEN=YOUR_BOT_TOKEN" > .env
   ```
   Replace `YOUR_BOT_TOKEN` with your actual bot token.

4. **Configure Bot Settings (Optional):**
   Customize Omnibot's behavior by editing the `config.py` file. Set the bot's prefix and owner ID to control access to owner commands.

5. **Make the Start Script Executable:**
   ```sh
   chmod +x start.sh
   ```

6. **Start Omnibot:**
   ```sh
   bash start.sh
   ```
   Launch Omnibot and ensure it is invited to your Discord server with the necessary permissions.

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug reports, please open an issue or create a pull request.

## Issues or Questions

Encountered a problem or have a question? We're here to help!

* **Report Issues:** If you find any bugs or have specific issues, please create a new [GitHub issue](https://github.com/Amitminer888/Omnibot/issues/new). We appreciate detailed bug reports that help us understand and fix the problem efficiently.

* **Contact Me on Discord:** Feel free to reach out to me directly on Discord.
  * **Username:** [Amit_xD](https://discord.com/users/814660125511778315)

**To-Do List**

Help us make Omnibot even better! You can:
* [ ] **Suggest New Commands:** Have a cool idea for a new command? Share it with us by creating a new [GitHub issue](https://github.com/Amitminer888/Omnibot/issues/new). Your suggestions are valuable and contribute to enhancing Omnibot's functionality.


## License

This project is licensed under the [MIT License](LICENSE).

---