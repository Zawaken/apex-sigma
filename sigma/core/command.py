import os
from importlib import import_module

from .permission import check_channel_nsfw
from sigma.core.formatting import code, codeblock


class CommandNotEnabled(RuntimeError):
    pass


class Command(object):
    def __init__(self, plugin, info):
        self.enabled = False
        self.glob = False
        self.sfw = True
        self.usage = "{pfx:s}{cmd:s}"
        self.desc = 'No description available.'

        self.db = plugin.db
        self.log = plugin.log
        self.bot = plugin.bot
        self.plugin = plugin
        self.prefix = self.bot.prefix

        try:
            self.load_info(info)
        except CommandNotEnabled:
            return

    def load_info(self, info):
        if 'enabled' not in info or not info['enabled']:
            raise CommandNotEnabled
        else:
            self.enabled = True

        self.name = info['name']
        self.path = self.plugin.path

        if 'global' in info and info['global']:
            self.glob = True

        if 'usage' in info:
            self.usage = info['usage']

        if 'description' in info:
            self.desc = info['description']

        self.sfw = info['sfw']

        module_path = os.path.join(self.path, self.name)
        self.modpath = module_path.replace('/', '.').replace('\\', '.')
        self.module = import_module(self.modpath)

    def help(self):
        usage = self.usage.format(pfx=self.prefix, cmd=self.name)
        return 'Usage: {:s}\n{:s}'.format(
                code(usage), codeblock(self.desc))

    def resource(self, path):
        return os.path.join(self.path, 'res', path)

    async def call(self, message, *args):
        channel = message.channel

        # some convenience methods
        async def typing():
            await self.bot.send_typing(channel)

        async def reply(text):
            await typing()
            return await self.bot.send_message(channel, text)

        async def reply_file(filename):
            return await self.bot.send_file(channel, filename)

        async def delete_call_message():
            return await self.bot.delete_message(message)

        self.typing = typing
        self.reply = reply
        self.reply_file = reply_file
        self.delete_call_message = delete_call_message

        # check channel nsfw permission
        if not self.sfw and not check_channel_nsfw(self.db, channel.id):
            msg = 'Channel does not have NSFW permissions set, sorry.'
            await self.reply(msg)
            return

        await typing()
        await getattr(self.module, self.name)(self, message, *args)
