# Discord Bot using Python, Discord API, and Gemini API

This project is a Discord bot that allows server members to communicate with the bot, which generates responses using the Gemini API.

## Features

- **User Interaction**: After joining the server, members can communicate with the bot.
- **Response Generation**: The bot utilizes the Gemini API to generate dynamic responses based on user input.
  
## Technologies Used

- **Python**: For building the bot logic.
- **Discord API**: To interact with Discord servers and users.
- **Gemini API**: For generating responses based on user interactions.

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AkshatJain-Programming/Discord_BOT.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    - **Discord Bot Token**: Your bot's token from the Discord Developer Portal.
    - **Gemini API Key**: Your Gemini API key.

    Create a `.env` file in the root directory of your project:
    ```plaintext
    DISCORD_TOKEN=your_discord_token
    GEMINI_API_KEY=your_gemini_api_key
    ```

4. Run the bot:
    ```bash
    python main.py
    ```

## Usage

- After adding the bot to your Discord server, members can interact with it by sending messages.
- The bot will respond to user messages using the Gemini API for intelligent responses.

## Contributing

Feel free to fork this repository and submit pull requests for any features or improvements.


