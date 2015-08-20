import time
import logging

crontable = []
outputs = []

LOGGER = logging.getLogger(__name__)

def process_message(data):
    text = data['text'].lower()
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

