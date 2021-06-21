from flask import Flask

apps=Flask(__name__)

@apps.route('/',methods=['GET','POST'])
def index():
    return "<h1> this is a flask application </h1>"


if __name__=="__main__":
    apps.run()