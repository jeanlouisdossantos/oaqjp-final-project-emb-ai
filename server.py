import flask
from EmotionDetection import emotion_detector

app = flask.Flask(__name__)
@app.route("/")
def hello():
    return  flask.render_template('index.html')


@app.route("/emotionDetector")
def emotionDetector():
    text = flask.request.args.get('textToAnalyze')
    res = emotion_detector(text)
    print (res)
    return res