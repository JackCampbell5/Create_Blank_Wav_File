# Import the necessary modules
import os
import wave
import numpy as np
from left_channel import get_left_channel
from right_channel import get_right_channel


# Set the directory containing the wav files
directory = r"C:\Users\jackp\Documents\Game Design\SoundProject\Audio\Python Code\TestFiles"

# Get the wave data from left and right channels
left_channel = get_left_channel()
right_channel = get_right_channel()

# Need to be created in a 2*2 formation3
wave_data_blank = np.array([left_channel, right_channel])
wave_data_blank = np.reshape(wave_data_blank, len(left_channel) * 2, order='F')
wave_data_blank = np.reshape(wave_data_blank, (len(left_channel), 2))

# Make the paths for writing files
path_blank = os.path.join(directory, "blank.wav")

# Create file for left
outwav_blank = wave.open(path_blank, 'w')

# Set stereo vs mono
outwav_blank.setnchannels(2)
outwav_blank.setsampwidth(2)
outwav_blank.setframerate(48000)
outwav_blank.setnframes(57600000)
outwav_blank.setcomptype('NONE', 'not compressed')


# Writes the output file
outwav_blank.writeframes(wave_data_blank.tobytes())

# Done and close it
outwav_blank.close()
