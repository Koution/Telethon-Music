import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6011626668:AAE5vLLJbAnUi3YfggEOHYF6Ld0yakdXzNA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQAyuuJjeV-kLcX_zkYwETONi2No1b72e2a7jWqJ4ucLDwuvrR1a4XcYAcSDnFp1NOdF9lrEpHlP3ZRW885tOQUdSlk3TbEMYQX9DoNAuTD7GITAhLovkfxwswH7NR4hKt3qIiEzdA382Q3oMytfiLoXQ8RhBXsVWuVugJmGbhOKzqlTBdZwV2oL1UViNlDjYSjQFW_6xWg7Hn2d_SFN3NwhfdB_eX5WdhpiT61PaKDfY8uUuJUJXUAkmGJJ-bubcJTIxmLIpuZLJog2Bg6gtFuM0n18D2MwIdFGPWN5Gh2jCW4aFKEnJfqgfPRNL4-DIZWRoLFTv7JQ-w0Pq4J02vMcAAAAAUpce90A")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
