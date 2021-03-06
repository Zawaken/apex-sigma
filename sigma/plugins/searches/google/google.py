import requests
from config import GoogleAPIKey
from config import GoogleCSECX


async def google(cmd, message, args):
    if not args:
        await cmd.reply(cmd.help())
        return
    else:
        search = ' '.join(args)
        results = requests.get(
            'https://www.googleapis.com/customsearch/v1?q=' + search + '&cx=' + GoogleCSECX + '&key=' + GoogleAPIKey).json()
        try:
            title = results['items'][0]['title']
            url = results['items'][0]['link']
            out = '`' + title + '`: \n<' + url + '>'
            await cmd.reply(out)
        except Exception as e:
            cmd.log.error(e)
            await cmd.reply(str(e))
