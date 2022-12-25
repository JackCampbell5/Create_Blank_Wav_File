# Import the necessary modules
import os
import wave
import numpy as np
from left_channel import get_left_channel
from right_channel import get_right_channel

directory = r"C:\Users\Jack Campbell\Documents\Sound project Help Files\Python Code\TestFiles\More"

# Set the directory containing the wav files
# directory = r"C:\Users\Jack Campbell\Documents\Sound project Help Files\Python Code\TestFiles\More"
print(get_left_channel()[:10])
print(get_right_channel()[:10])

# Split the wave data into left and right channels
left_channel = get_left_channel()
right_channel = get_right_channel()


# Need to be created in a 2*2 formation3
wave_data_left = np.array([left_channel, right_channel])
wave_data_left = np.reshape(wave_data_left, len(left_channel) * 2, order='F')
wave_data_left = np.reshape(wave_data_left, (len(left_channel), 2))

# Make the paths for writing left and right
path_left = os.path.join(directory, "blank.wav")

# Create file for left
outwav_left = wave.open(path_left, 'w')

# Set stereo vs mono
outwav_left.setnchannels(2)
outwav_left.setsampwidth(2)
outwav_left.setframerate(48000)
outwav_left.setnframes(57600000)
outwav_left.setcomptype('NONE', 'not compressed')


# Writes the ou tput file
outwav_left.writeframes(wave_data_left.tobytes())

# We are done
outwav_left.close()
