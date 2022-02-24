from django.template.loader import get_template

def get_message(item, action):
    template = get_template('app/message.txt')
    context = {
        "item": item,
        "action": action,
    }
    message = template.render(context)
    return message

def send_notification(item, action):
    message = get_message(item, action)
    # send_slack_message.delay(message)
    # send_email.delay(message)