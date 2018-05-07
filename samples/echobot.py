import time

def respond(message):
	return "you said : {}".format(message)


def send_message(message):
	time.sleep(2)
	print(respond(message))



k = input("Hey User Say something? \n")

send_message(k)