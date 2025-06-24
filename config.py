from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "2360d53e98bf778a286d8c054333d470")
      API_ID = int(getenv("API_ID", "23830854"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8076097548:AAGz7ilnlkZzjGfCOqFX81RHv4VjotXSdMw")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002541110361:-1002541451452").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
