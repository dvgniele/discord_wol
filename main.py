import Consts as keys
import discord
from wol import send_magik_packet

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('$turnon') or msg.content.startswith('$poweron'):
        await msg.channel.send(send_magik_packet(keys.MAC, keys.IP, keys.PORT))

    if msg.content.startswith('$bl') or msg.content.startswith('$blbl'):
        await msg.channel.send("sovvivo!")


def main():
    client.run(keys.TOKEN)


if __name__ == "__main__":
    main()
