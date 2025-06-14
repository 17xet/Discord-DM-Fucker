import discord
import asyncio
import json
import os
from pystyle import Colors, Colorate, Center, Write

os.system('title https://github.com/17xet ~~~ https://youtube.com/@17xet ~~~ https://discord.gg/mx9raXzU9S')

banner = """


┌┬┐┌┬┐  ┌─┐┬ ┬┌─┐┬┌─┌─┐┬─┐
 │││││  ├┤ │ ││  ├┴┐├┤ ├┬┘
─┴┘┴ ┴  └  └─┘└─┘┴ ┴└─┘┴└─
   ( Made by 17xet <3 ) 



"""

print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(banner)))

def load_tokens(file_name):
    try:
        with open(file_name, 'r') as f:
            tokens = json.load(f)
        return tokens
    except Exception as e:
        Write.Print(f"Error loading bot tokens: {e}\n", Colors.red, interval=0.01)
        return []

async def send_message(bot_token, user_id, message, repeat_count):
    intents = discord.Intents.default()
    intents.dm_messages = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        try:
            user = await client.fetch_user(user_id)
            for _ in range(repeat_count):
                await user.send(message)
            Write.Print(f"{client.user.name} successfully sent messages.\n", Colors.green, interval=0.01)
        except Exception as e:
            Write.Print(f"Failed to send message from {client.user.name}: {e}\n", Colors.red, interval=0.01)
        finally:
            await client.close()

    try:
        await client.start(bot_token)
    except Exception as e:
        Write.Print(f"Error starting bot: {e}\n", Colors.red, interval=0.01)

async def main():
    user_id = int(Write.Input("Enter the user ID to message: ", Colors.blue_to_purple, interval=0.01))
    token_file = Write.Input("Enter the bot token file name (e.g., tokens.json): ", Colors.blue_to_purple, interval=0.01)
    message = Write.Input("Enter the message to send: ", Colors.blue_to_purple, interval=0.01)
    repeat_count = int(Write.Input("Enter how many times to send the message: ", Colors.blue_to_purple, interval=0.01))

    bot_tokens = load_tokens(token_file)

    if not bot_tokens:
        Write.Print("No valid bot tokens found.\n", Colors.red, interval=0.01)
        return

    tasks = [send_message(token, user_id, message, repeat_count) for token in bot_tokens]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
