import json
import google.generativeai as genai
import discord

GEN_KEY = "YOUR-GEMINI-API-KEY"
genai.configure(api_key=GEN_KEY)

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 50,
    "max_output_tokens": 692,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config)

# discord set up
APP_ID = "YOUR-ID"
PUBLIC_KEY = "YOUR_PUBLIC_KEY"
TOKEN = "YOUR_DISCORD_TOKEN"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# create history file to store history of chats
with open("history.txt", 'w') as file:
  init_chat = [{"role": "user",
                "parts": ["<@1219650758312595616> give answers in less than 200 words only in any condition"]},
               {"role": "model",
                "parts": ["No problem! Keeping it concise. \ud83d\udc4d \n"]}]
  json.dump(init_chat, file)

@client.event
async def on_message(msg):

    # msg sent by bot
    if msg.author == client.user:
        return

    # if anyone mentions the bot
    if client.user in msg.mentions:
        # loads history
        with open("history.txt") as file:
            chat = json.loads(file.read())
            chat_history = chat

        convo = model.start_chat(history=chat_history)

        author_chat = {
            "role": "user",
            "parts": [msg.content]
        }
        # append msg sent by anyone
        chat_history.append(author_chat)
        # push request
        convo.send_message(msg.content)

        response = convo.last.text
        # save response by AI
        model_chat = {
            "role": "model",
            "parts": [response]
        }
        chat_history.append(model_chat)

        # saves history
        with open("history.txt", 'w', encoding="utf-8") as file:
            json.dump(chat_history, file)

        # response sent
        await msg.channel.send(response)


# run discord bot
client.run(TOKEN)
