# import os 
# from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
# from moviepy.editor import * # ImageClip



# from PIL import Image
# from moviepy.video.fx.all import crop

# source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")

# GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")
# os.makedirs (GIF_DIR, exist_ok=True)
# output_path1 = os.path.join(GIF_DIR, "sample1.gif")
# output_path2 = os.path.join(GIF_DIR, "sample2.gif")

# clip = VideoFileClip(source_path)
# fps = clip.reader.fps
# subclip = clip.subclip (10, 20) # name it subclip, it is a video clip object that contains the frames from 10 to 20 sec of the original clip
# subclip = subclip.resize(width=320)
# subclip.write_gif(output_path1, fps=20, program = "ffmpeg")

# w, h = clip.size
# subclip2 = clip.subclip(10, 20)
# square_cropped_clip = crop(subclip2, width=320, height=320, x_center=w/2, y_center=h/2)
# square_cropped_clip.write_gif(output_path2, fps=fps, program='ffmpeg')


import os 
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy import VideoFileClip
from moviepy.video.fx import Crop
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")

GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")
os.makedirs(GIF_DIR, exist_ok=True)
output_path1 = os.path.join(GIF_DIR, "sample1.gif")
output_path2 = os.path.join(GIF_DIR, "sample2.gif")

clip = VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclipped(10, 20)
subclip = subclip.resized(width=320)
subclip.write_gif(output_path1, fps=20)  # Removed program parameter

w, h = clip.size
subclip2 = clip.subclipped(10, 20)

# Fix: Apply Crop as a method, not as a callable class
square_cropped_clip = subclip2.with_effects([Crop(x_center=w/2, y_center=h/2, width=320, height=320)])
square_cropped_clip.write_gif(output_path2, fps=fps)