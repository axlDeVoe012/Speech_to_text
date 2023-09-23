import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

def record_text():
    # Loop in case of errors
    while True:
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # Prepare recognizer for input
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")
        
        return

def output_text(text):
    if text:  # Check if text is not None before writing to the file
        f = open("output.txt", "a")
        f.write(text)
        f.write("\n")
        f.close()
    return

while True:
    text = record_text()
    output_text(text)
    print("Wrote text")
