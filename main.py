from moviepy.editor import VideoFileClip
import azure.cognitiveservices.speech as speechsdk
import time
import pickle
import json
import sys

# Azure Speech Service subscription key
subscription_key = sys.argv[2]

# Azure Speech Service region
speech_region = "australiaeast"

# Get the audio out of the input video e.g. "input.mp4"
video_name = sys.argv[1]
video = VideoFileClip(video_name)
audio = video.audio
audio.write_audiofile("input.wav")

# Set up the file as the audio source
speech_config = speechsdk.SpeechConfig(subscription_key, speech_region)
audio_config = speechsdk.AudioConfig(filename="input.wav")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config, audio_config)

# Flag to end transcription
done = False

# List of transcribed lines
results = list()

def stop_cb(evt):
    """callback that stops continuous recognition upon receiving an event `evt`"""
    print(f"CLOSING on {evt}")
    speech_recognizer.stop_continuous_recognition()

    # Let the function modify the flag defined outside this function
    global done
    done = True
    print(f"CLOSED on {evt}")

def recognised(evt):
    """Callback to process a single transcription"""
    recognised_text = evt.result.text

    # Simply append the new transcription to the running list
    results.append(recognised_text)
    print(f"Audio transcription: '{recognised_text}'")

# Define behaviour for each recognition/transcription
speech_recognizer.recognized.connect(recognised)

# Define behaviour for end of session
speech_recognizer.session_stopped.connect(stop_cb)

# And for canceled sessions
speech_recognizer.canceled.connect(stop_cb)

# Create a synchronous continuous recognition, the transcription itself if you will
speech_recognizer.start_continuous_recognition()

# Set a brief pause between API calls
while not done:
    time.sleep(0.5)

# Dump the whole transcription to a pickle file
with open("output.pickle", "wb") as f:
    pickle.dump(results, f)
    print("Transcription dumped to pickle")

# Dump the processed text to JSON
with open("output.json", "a") as f:
    json.dump(results, f, indent=2)
    print("Transcription dumped to JSON")
