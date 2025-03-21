import requests
import json

def emotion_detector(text_to_analyze):
    if text_to_analyze == None or text_to_analyze == '':
        return { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None }  
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    request_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = request_json, headers=headers)
    
    if response.status_code == 400:
        return { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None }
    
    j = json.loads(response.text)
    emotions = j['emotionPredictions'][0]['emotion']
    dominant_score = 0
    dominant_emotion = None
    for key, value in emotions.items():    
        if value > dominant_score:
            dominant_emotion = key
            dominant_score = value
    emotions['dominant_emotion'] = dominant_emotion
    return emotions

