import numpy as np
from pippi import dsp
from pippi import tune

class Soundify():
    def __init__(self, instrument='guitar', octave_offset=-0):
        """
        Initialize class
        :param instrument:
        :param octave_offset:
        """
        self.instrument = instrument
        self.octave_offset = octave_offset

        if self.instrument == 'guitar':
            self.base_tone = dsp.read('/home/nik/Projects/pippi/tests/sounds/guitar1s.wav') #Tone A
            self.original_freq = tune.ntf('A{}'.format(4-octave_offset))
            print("Frequency of base tone: {} Hz ".format(self.original_freq))


        self.keys = {'A0': 0,
                     'Bb': 1,
                     'B': 2,
                     'C': 3,
                     'Db': 4,
                     'D': 5,
                     'Eb': 6,
                     'E': 7,
                     'F': 8,
                     'Gb': 9,
                     'G': 10,
                     'Ab': 11,
                     'A': 12}

        self.keys_inverted = {value: key for key, value in self.keys.items()}

    def get_frequency(self, key, octave):
        """
        Returns frequency based on key and octave.
        Tuned such that key='A' and octave=1 returns 880Hz
        :param key: String with key
        :param octave: positive integer with octave.
        :return: frequency
        """
        frequency = 2 ** (self.keys[key] * octave / 12) * 440
        return frequency

    def make_melody(self, sequence, name):
        out = dsp.buffer()

        pos = 0
        beat = 0.05
        pause = 0.5

        for keys in sequence:

            notes = self.keys_to_notes(keys=keys)
            print("Playing the following notes: {}".format(notes))

            frequencies = [self.get_frequency(key=tone[:-1], octave=int(tone[-1])) for tone in notes]
            print("Corresponding to the frequencies: {}".format(frequencies))

            speeds = self.get_speeds(frequencies)

            for speed in speeds:
                # Create a pitch-shifted copy of the original guitar
                tone = self.base_tone.speed(speed)

                # Dub it into the output buffer at the current position in seconds
                out.dub(tone, pos)

                # Now move the write position forward <beat> seconds
                pos += beat
            pos += pause

        # Save this output buffer
        out.write('../output/harmonic/renders/melody_{}.wav'.format(name))
        pass

    def keys_to_notes(self, keys, start='Bb'):
        """
        From a list of numbers representing pressed keyboard keys, gets the corresponding notes.
        :param keys: list of strings, which should be either '1' or '0' (for pressed or not pressed)
        :param start: note representing the first key
        :return:
        """
        notes = []
        i = 0
        for key in keys:
            if key == '1':
                octave = i//12
                number = i%12 + 1
                note = self.keys_inverted[number] + str(octave+1)
                notes.append(note)
            elif key == '0':
                pass
            else:
                print("No valid key. Abort.")
                exit()
            i += 1
        return notes

    def get_speeds(self, line):
        speeds = [new_freq / self.original_freq for new_freq in line]
        return speeds


if __name__ == '__main__':
    # sequence =  Bb   B    C    Db   D    Eb   E    F    Gb   G    Ab   A    Bb   B  ...

    sequence = [['0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0'],
                ['0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0'],
                ['0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1'],
                ['0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0'],
                ['0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0']]

    sequence = [['0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0'],
                ['0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0']
                ]


    Sound = Soundify()

    Sound.make_melody(sequence)

    # print(chord)
    # print(speeds)