import numpy
import pyaudio
import analyse
import time
from playsound import playsound

pyaud = pyaudio.PyAudio()

stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 2, 
    rate = 44100,
    input_device_index = 0,
    input = True,
    frames_per_buffer = 1024)

def commandSound():
  print "bark"
  playsound('Desktop/shhh.m4a')
  time.sleep(5)
  listenBarks()
  pass

def listenBarks():
  end = 0
  while end == 0:

    # Read raw microphone data
    rawsamps = stream.read(1024, exception_on_overflow=False)
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    # Show the volume
    volume = analyse.loudness(samps)

    print(volume)

    if volume>-10:
      end = 1
      commandSound()
      pass

  pass

listenBarks()
