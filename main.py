# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import whisper
import wave
import pyaudio
import time
import threading
import concurrent.futures


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def getReady():
    print("preparing initial data, don't talk yet.")

    #Get the whisper model we want to use (Affects perfomance)
    model_ready = whisper.load_model("tiny")



    return model_ready


def waitSeconds(nSeconds):
    time.sleep(nSeconds)


def startRecord(recordX,time):
    print("recording "+ recordX)
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []

    #Creating a thread to take the audio while it is running (used only to take aduio for Xseconds)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(waitSeconds,time)
        while f1.running():
            data = stream.read(1024)
            frames.append(data)

    print("Audio grabado")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open((recordX+".mp3"), "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()


def transcribe(modelUsed,name):
    result = model.transcribe(name+".mp3")
    return result["text"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #GET READY
    model = getReady()
    voiceSeconds = []
    voiceSecondsIndex = 0
    secondsWait = 2

    #APP CICLE CODE (each secondsWait seconds)
    while True:
        print("Siguiente 'segundos'")

        #Record the secondsWait duration audio
        threadRecorder = threading.Thread(target=startRecord, args=(("input"+str(voiceSecondsIndex)),secondsWait))
        threadRecorder.start()
        threadRecorder.join()

        #is it nonsound?
        prevAudioTxt = transcribe(model,"input"+ str(voiceSecondsIndex))
        print (prevAudioTxt)
        if(prevAudioTxt != ""):
            print(" ALGO HAY")
            # Next "seconds"
            voiceSecondsIndex += 1
        else:
            print("NADA HAY")
            # Return to 0 "seconds"
            voiceSecondsIndex = 0








