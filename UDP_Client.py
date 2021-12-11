import pyaudio
import socket
import sys
import time
import wave


RECORD_SECONDS = 10
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 10240
WAVE_OUTPUT_FILENAME = "out1.wav"

p = pyaudio.PyAudio()
counter = 0
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

host = "127.0.0.1"
port = ""
size = 2048
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
frames = []
state = True


def connect(port):
    global state
    while state:
        data = stream.read(CHUNK)
        s.sendto(data, (host, int(port)))
        s.recvfrom(size)


def rec(port):

    print("* recording")
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        s.sendto(data, (host, int(port)))
        frames.append(data)
    print("* done recording")
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def ex():
    sys.exit(0)


counter = 0
