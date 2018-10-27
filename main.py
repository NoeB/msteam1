from microsoftbotframework import MsBot
from tasks import *

CONFIG_LOCATION="/home/user/noe/msteam/config.yaml"

bot = MsBot(verify_jwt_signature=False)
bot.add_process(echo_response)
bot.add_process(echo_test)

if __name__ == '__main__':
    bot.run()
