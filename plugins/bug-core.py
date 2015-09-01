import time
import logging

crontable = []
outputs = []
parent = None

LOGGER = logging.getLogger(__name__)

def process_message(data):
    if 'text' in data:
        text = data['text'].lower()
    else:
        text = None

    LOGGER.debug(data)
    if 'subtype' in data and (data['subtype'] == 'bot_message' or data['user'] == 'U02NTS39B'):
        LOGGER.info('I hate bots!')
        outputs.append([ data['channel'], '_growls_'])
    if text.startswith('pets') and 'bug' in text:
        LOGGER.info('Command received: %s', text)
        outputs.append([ data['channel'], '_wags tail_'])
    elif text.startswith('pushes') and 'bug to' in text:
        LOGGER.info('Command received: %s', text)
        user = text.split()[3]
        if user:
            outputs.append([ data['channel'], '_wanders over to {}_'.format(user) ])
    elif text.startswith('bug:'):
        LOGGER.info('Command received: %s', text)
        outputs.append([ data['channel'], 'Woof!' ])

def setup(self):
    LOGGER.info("BugBot Core Loaded!")


def user_is_bot(uid):
    LOGGER.debug(uid)
    if uid == 'U02NTS39B':
        return True
    reply = parent.slack_client.api_call('users.info', user=user)
    user_data = json.loads(reply)
    user = None
    if user_data['ok']:
        user = user_data['user']
        return user['is_bot']
    else:
        return False

