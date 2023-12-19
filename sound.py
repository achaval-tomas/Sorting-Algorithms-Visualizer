import pygame as py
from array import array
from pygame.mixer import Sound, get_init

class Note(Sound):

    def __init__(self, frequency, volume=.1):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

def playPitch(pitch, duration):
    py.mixer.pre_init(44100, -16, 1, 1024)
    note = Note(pitch)
    note.play(-1)
    py.time.delay(duration)
    note.stop()
