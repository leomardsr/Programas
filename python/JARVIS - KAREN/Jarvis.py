import pyttsx3 #Python Text to Speach 3
import datetime #Libreria de fecha y hora
import speech_recognition as sr 

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voices',voice[1])
engine.setProperty('rate', 190)
engine.say("Hi, I'm Karen, buenas noches")
engine.runAndWait()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def time():
	ftime = "It is the"
	Time = datetime.datetime.now().strftime("%I:%M:%S") 
	Ttime = ftime + Time
	speak(Ttime)

def date():
	day = int(datetime.datetime.now().day)
	month = int(datetime.datetime.now().month)
	year = int(datetime.datetime.now().year)
	speak(day)
	speak(month)
	speak(year)

def wishme():
	hour = int(datetime.datetime.now().hour)
	if hour >= 5 and hour <= 12:
		hour = "Good Morning Sir"
	elif hour >=12 and hour <=18:
		hour = "Good Afternoon Sir"
	elif hour >= 16 and hour<=22:
		hour = "Good Evening Sir"
	else:
		hour = "Good Night Sir"

	engine.say(hour)
	date()
	time()

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print ("Listening...")
		r.pause_threshold = 1
		audio = r.listen (source)

		try:
			print("Reconociendo")
			query = r.recognize_google(audio, "en=IN")
			print (query)

		except Exception as e:
			print (e)
			speak ("Say it again, please...")
 
			return "None"
		return query
#wishme()
takeCommand()

#print(sr.Microphone.list_microphone_names())