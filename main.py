from openbot import Openbot
from loguru import logger as log


while True:
    log.debug('Start Openbot')

    try:
        Openbot().run()
    except Exception as err:
        log.error(err)
    finally:
        log.debug('Stop bot')

