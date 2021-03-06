from sigma.core.permission import check_man_msg
from sigma.core.permission import check_man_roles
from sigma.core.permission import check_write
import asyncio


async def unmute(cmd, message, args):
    channel = message.channel
    server = message.server
    if not message.mentions:
        await cmd.reply(cmd.help())
        return
    user_q = message.mentions[0]
    if message.author is not user_q:
        if check_man_msg(message.author, channel) and check_man_roles(message.author, channel):
            try:
                for chan in server.channels:
                    if str(chan.type).lower() == 'text':
                        if not check_write(user_q, chan):
                            await cmd.bot.delete_channel_permissions(chan, user_q)
                await cmd.reply('Execution Successful.\nUser **' + user_q.name + '** was unmuted')
            except Exception as e:
                cmd.log.error(e)
                await cmd.reply(str(e))
        else:
            response = await cmd.reply('Only a user with the **Manage Messages and Manage Roles** privilege can use this command. :x:')
            await asyncio.sleep(10)
            await cmd.bot.delete_message(response)
