"""
Flask server for emotion detection.
"""

import flask
from EmotionDetection import emotion_detector

app = flask.Flask(__name__)
@app.route("/")
def hello():
    """Render the index page."""
    return flask.render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions in the provided text and return formatted response."""

    text = flask.request.args.get('textToAnalyze')
    res = emotion_detector(text)
    print (res)
    # Format the response
    dominant_emotion = res['dominant_emotion']
    if dominant_emotion is None:
        formatted_response = "Invalid text! Please try again!"
    else:
        formatted_response = (
            f"For the given statement, the system response is 'anger': {res['anger']}, "
            f"'disgust': {res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']} "
            f"and 'sadness': {res['sadness']}. The dominant emotion is {dominant_emotion}."
        )
    return formatted_response
