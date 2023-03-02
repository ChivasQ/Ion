import stt
import pyperclip, keyboard, time
import webbrowser

def paste(text: str):
    buffer = pyperclip.paste()
    pyperclip.copy(text)
    keyboard.press_and_release('ctrl + v')
    pyperclip.copy(buffer)


def type(text: str, interval=0.0):
    if interval == 0.0:
        paste(text)
        return

    buffer = pyperclip.paste()
    for char in text:
        pyperclip.copy(char)
        keyboard.press_and_release('ctrl + v')
        time.sleep(interval)
    pyperclip.copy(buffer)

def command(commd):
    if commd == "очистити":
        keyboard.press_and_release('ctrl + a')
        keyboard.press_and_release('delete')
    else:
        type(f'{commd}', 0.01)
    print(commd)



def respond(voice):
    if len(voice) > 0:
        print("Вы: ", voice.capitalize() + ".")
        command(voice)
webbrowser.open("https://translate.google.com/?hl=ru&sl=uk&tl=en&op=translate")
stt.listen(respond)
