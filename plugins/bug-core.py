import time
crontable = []
outputs = []

#def process_message(data):
#    if data['channel'].startswith("D"):
#        outputs.append([data['channel'], "from repeat1 \"{}\" in channel {}".format(data['text'], data['channel']) ])

def process_message(data):
    text = data['text'].lower()
    if text.startswith('pets') and 'bug' in text:
        outputs.append([ data['channel'], '_wags tail_'])
    elif text.startswith('pushes') and 'bug to' in text:
        user = text.split()[3]
        if user:
            outputs.append([ data['channel'], '_wanders over to {}_'.format(user) ])
    elif text.startswith('bug:'):
        outputs.append([ data['channel'], 'Woof!' ])
    print data
