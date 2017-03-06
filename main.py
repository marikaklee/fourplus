from flask import Flask
from flask import render_template
import fbchat

client = fbchat.Client("marikalee15@gmail.com", "C!Nta8ku123!")

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('main.html')

@app.route("/button")
def messageMarika():
	friends = client.getUsers("Marika Lee")
	friends = client.getUsers("Marika Lee")  # return a list of names
	friend = friends[0]
	sent = client.send(friend.uid, "hello :)")

	if sent:
	    print("Message sent successfully!")
  	return 'Message sent to Marika.'

if __name__ == "__main__":
    app.run()
