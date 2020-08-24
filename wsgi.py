from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Sup Benny the man!"

if __name__ == "__main__":
    application.run()
