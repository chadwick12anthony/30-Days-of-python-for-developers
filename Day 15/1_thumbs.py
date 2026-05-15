# import os
# from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
# from moviepy.video.io.VideoFileClip import VideoFileClip  # Direct import
# from PIL import Image

import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *  # Direct import, no .editor needed
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
os. makedirs(thumbnail_dir, exist_ok=True)

clip = VideoFileClip(source_path)

print(clip.reader.fps) # Frames per sec 
print(clip.reader.nframes) # nbr of frames 
print(clip.duration) # Video duration in sec 

duration = clip.reader.duration
max_duration = int(duration) + 1

for i in range (0, max_duration):
    print(f"Here is an image at {i} sec !")
    frame = clip.get_frame(i) # numpy array of shape (height, width, 3) with RGB values
    new_img_filepath = os. path. join(thumbnail_dir, f"{i}.jpg")
    #print(frame)
    new_image = Image.fromarray(frame)
    new_image.save(new_img_filepath)