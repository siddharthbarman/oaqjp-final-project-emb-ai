import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestJoy(unittest.TestCase):
    def test_correct_output(self):        
        self.assertEqual(emotion_detector('I am glad this happened')['dominant_emotion'], 'joy')

class TestAnger(unittest.TestCase):
    def test_correct_output(self):        
        self.assertEqual(emotion_detector('I am really mad about this')
        ['dominant_emotion'], 'anger')

class TestDisgust(unittest.TestCase):
    def test_correct_output(self):        
        self.assertEqual(emotion_detector('I feel disgusted just hearing about this')
        ['dominant_emotion'], 'disgust')

class TestSadness(unittest.TestCase):
    def test_correct_output(self):        
        self.assertEqual(emotion_detector('I amcl so sad about this')
        ['dominant_emotion'], 'sadness')

class TestFear(unittest.TestCase):
    def test_correct_output(self):        
        self.assertEqual(emotion_detector(
            'I am really afraid that this will happen')['dominant_emotion'], 'fear')

unittest.main()

