import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *  
from PIL import Image


thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
output_video = os.path.join(SAMPLE_OUTPUTS, "thumbs.mp4")

this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir 
             if fname.endswith("jpg") ]

# clip = ImageSequenceClip(filepaths, fps=4)
# clip.write_videofile(output_video)

directory = {}

for root, dirs, files in os.walk(thumbnail_dir):
    for fname in files:        
        filepath = os.path.join(root, fname)
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key != None:
            directory[key] = filepath

new_filepath = []
for k in sorted(directory.keys()):
    print (k)
    new_filepath.append(directory[k])

# clip = ImageSequenceClip(new_filepath, fps=1)
# clip.write_videofile(output_video)

my_clips = []
for path in list (new_filepath):
    frame = ImageClip(path)
    my_clips.append (frame.img)
    print(frame.img) # numpy array my_clips. append (frame.img) 

clip = ImageSequenceClip(my_clips, fps=12)
clip.write_videofile(output_video)
