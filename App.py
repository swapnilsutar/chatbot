from flask import Flask, render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

app = Flask(__name__,template_folder="template")

BotMe = ChatBot('BotMe',storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer = ChatterBotCorpusTrainer(BotMe)
trainer = ListTrainer(BotMe)

trainer.train([
    'how are you',
    'I am good',
    'what is your name',
    'people call me BotMe',
    'Have a great day',
])

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


if __name__ == "__main__":
    app.run()