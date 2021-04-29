from pydub import *

three_seconds = 3 * 1000

song = AudioSegment.from_wav('eldar.wav')

first_3_seconds = song[:three_seconds]

first_3_seconds.export('R:/pfile.wav', format='wav')

# tak ne nado, nado tak