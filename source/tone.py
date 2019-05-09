from scipy.io.wavfile import write
import numpy as np


def note(freq, length, amp=1, rate=5):
    t = np.linspace(0, length, length * rate)
    data = np.sin(2*np.pi*freq*t)*amp
    return data.astype(np.int16)  # two byte integers


def get_frequency(key, octave):
    """
    Returns frequency based on key and octave.
    Tuned such that key='A' and octave=0 returns 440Hz
    :param key: String with key
    :param octave: integer with
    :return: frequency
    """

    keys = {'A0': 0,
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
    frequency = 2 ** (keys[key] * octave / 12) * 440
    return frequency


print(get_frequency(key='A', octave=-1))

duration = 5000
tone1 = note(440,duration,amp=10000)
tone2 = note(140,duration,amp=10000)
tone3 = np.concatenate([tone2, tone1])
tone3 = tone2 + tone1

print(tone1)
print(tone2)
print(tone3)


write('../output/harmonic/renders/440hzAtone.wav', 44100, tone1)
write('../output/harmonic/renders/140hzAtone.wav', 44100, tone2)
write('../output/harmonic/renders/440p140hzAtone.wav', 44100, tone3)

#output:
# [ 0 -9 -3  8  6 -6 -8  3  9  0]
# [ 0  6  9  8  3 -3 -8 -9 -6  0]
# [ 0  6  9  8  3 -3 -8 -9 -6  0  0 -9 -3  8  6 -6 -8  3  9  0]