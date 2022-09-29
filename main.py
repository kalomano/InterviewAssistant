# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import whisper


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def getReady():
    print("preparing initial data, don't talk yet.")

    #Get the whisper model we want to use (Affects perfomance)
    model_ready = whisper.load_model("tiny")



    return model_ready


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    model = getReady()
    result = model.transcribe("shortAudio.mp3")
    print(result["text"])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
