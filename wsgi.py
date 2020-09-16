from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/bo")
def bo():
    return "Thanks Boeing for allowing us to work with you!!"


@application.route("/rh")
def rh:():
    return "Red Hat loves linux"

if __name__ == "__main__":
    application.run()
