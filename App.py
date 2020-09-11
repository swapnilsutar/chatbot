from flask import Flask, render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__,template_folder="template")

BotMe = ChatBot('BotMe',storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer = ChatterBotCorpusTrainer(BotMe)
# trainer = ListTrainer(BotMe)

trainer.train("trainee/conversations.yml")

# trainer.train([
#     'how are you',
#     'I am good',
#     'what is your name',
#     'people call me BotMe',
#     'Have a great day',
# ])

@app.route("/")
def home():
    # while True:
    #     try:
    #         user = input("You: ")
    #         bot_response = BotMe.get_response(user)

    #         print(bot_response)
    #     except:
    #         break
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    if (request.args.get('msg') == ''):
        return str("you wann ask something")
    else:
        return str(BotMe.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)