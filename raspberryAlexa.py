from flask import Flask 
from flask ask import Ask, statement
import Adafruit_DHT
from time import sleep

sensor = Adafruit_DHT. DHT22
pin = 3

app = Flask (__name__)
ask = Ask(app, '/')

@app.route('/')

def index():
        return 'Hello World'

@ask.launch
def start_skill():
        welcome_message = "Hi! jiyeon!"
        return statement(welcome_message)

@ask.intent('hellointent')
def hi():
        text = "Hi! nice to meet you"
        return statement(text)

def my():
        text = "hello my name is jiyeon you"
        return statement(text)
    
@ask.intent('dhtintent')
def temp()
        humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
        sleep(1)
        text = "temperature is {0:0.1f}".format(temperature)
        return statement(text)
@ask.intent('dhtintent')
def hum()
        humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
        sleep(1)
        text = "humidity is {0:0.1f}".format(temperature)
        return statement(text)

if __name__=='__main__':
        app.run(debug=True, host='0.0.0.0')