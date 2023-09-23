# Speech to text
This Python script allows you to convert spoken language into text using the speech_recognition library. It records audio from your microphone, recognizes the speech content, and saves it to a text file.

How to Use
1. Install Dependencies: Make sure you have the required libraries installed. You can install them using pip:  pip install SpeechRecognition

2. Run the Script: Execute the speech_to_text.py script using Python:  python speech_to_text.py

3. Recording: Once the script is running, it will prompt you to speak. Start speaking after the "Please speak something..." message.

4. Conversion: The script will adjust for ambient noise, record your speech, and then use Google's speech recognition to convert it to text.

5. Output: The recognized text will be saved to a file named output.txt. Each recognized phrase will be written on a new line in the file. You must use the tail fuction to see the sentences beign written in real time:  tail -f output.txt

6. Termination: To stop the script, press Ctrl+C.

This script is a basic speech-to-text converter and can be customized and extended to suit your specific needs. Make sure to handle exceptions and error cases as necessary for your use case.

