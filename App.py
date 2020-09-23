from flask import Flask, render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__,template_folder="template")

BotMe = ChatBot('BotMe',storage_adapter="chatterbot.storage.SQLStorageAdapter")
# BotMe = ChatBot('BotMe',storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     # database = mongodb_name,
                    #  database_uri = mongodb_uri) this is for heroku database

trainer = ChatterBotCorpusTrainer(BotMe)
# trainer = ListTrainer(BotMe)

trainer.train("trainee/conversations.yml")
trainer.train("trainee/ai.yml")
trainer.train("trainee/botprofile.yml")
trainer.train("trainee/computers.yml")
trainer.train("trainee/emotion.yml")
trainer.train("trainee/food.yml")
trainer.train("trainee/gossip.yml")
trainer.train("trainee/greetings.yml")
trainer.train("trainee/health.yml")
trainer.train("trainee/history.yml")
trainer.train("trainee/humor.yml")
trainer.train("trainee/literature.yml")
trainer.train("trainee/movies.yml")
trainer.train("trainee/psychology.yml")
trainer.train("trainee/science.yml")
trainer.train("trainee/sports.yml")
trainer.train("trainee/trivia.yml")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    if (request.args.get('msg') == ''):
        return str("you wann ask something")
    else:
        return str(BotMe.get_response(userText))


if __name__ == "__main__":
    app.run(debug=False)