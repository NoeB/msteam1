
from microsoftbotframework import ReplyToActivity

def echo_response(message):
    if message["type"] == "message":
        ReplyToActivity(fill=message,text=message["text"]).send()


def echo_test(message):
	if message["text"] =="Hallo":
        	ReplyToActivity(fill=message,text='Hallo Noé').send()
