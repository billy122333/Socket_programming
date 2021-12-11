import pyaudio
import socket
import sys
import time
import wave
import tkinter

# 待解決 掛斷通話....
# 若用無窮迴圈 就入後就出不來了...
# 目前想法 : non-block 讓輸入端不會停止，在terminal輸入 0 結束通話
# 非阻塞式若想避免錯誤 使用try catch 解決
host = "127.0.0.1"
port = ""
size = 1024
RECORD_SECONDS = 10
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 10240
WAVE_OUTPUT_FILENAME = "out1.wav"


frames = []
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)


size = 1024


frames = []
state = True


def connect(port):
    global state
    Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Sock.connect((host, int(port)))
    while state:  # bool
        data = stream.read(size)
        if(data):
            Sock.send(data)
            Sock.recv(size)
    if(not state):
        Sock.close()


def rec(port):
    Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Sock.connect((host, int(port)))
    print("* recording")
    for i in range(0, int((RATE / CHUNK) * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        Sock.send(data)
        Sock.recv(size)
        frames.append(data)
    print("* done recording")
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def ex():
    sys.exit(0)


def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

    # input
