import speech_recognition as sr

def record_text(recognizer, microphone):
    while True:
        try:
            with microphone as source:
                print("Please speak something...")  # Prompt the user to speak
                
                # Adjust for ambient noise with a shorter duration
                recognizer.adjust_for_ambient_noise(source, duration=0.1)
                
               # Use a smaller chunk size for potentially faster processing
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                print("Recording complete. Recognizing...")

            return recognizer.recognize_google(audio)  # Recognize speech using Google's API

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            print("Please check your network connection and try again.")  # Network error message
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")  # Recognition error message
        except KeyboardInterrupt:
            print("Recording stopped.")  # Handle user interruption
            break

def output_text(text, filename="output.txt"):
    with open(filename, "a") as file:
        file.write(text + "\n")  # Append recognized text to the output file


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        try:
            text = record_text(recognizer, microphone)  # Record and recognize speech
            if text:
                output_text(text)  # Save recognized text to the output file
                print("Wrote text to output.txt")
                

        except KeyboardInterrupt:
            print("Program terminated.")  # Handle user termination
            break

if __name__ == "__main__":
    main()
