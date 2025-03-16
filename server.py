""" Capstone project """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """ Displays the index page """
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """ Detects emotion using WatsonX API """
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return emotion_detector(text_to_analyze)

if __name__ == "__main__":
    app.run(debug=True)
