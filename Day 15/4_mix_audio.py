# import os
# from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
# from moviepy.editor import *  # Direct import, no .editor needed
# from PIL import Image
# from moviepy.audio.fx.all import volumex

# source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")
# source_audio_path = os.path.join(SAMPLE_INPUTS, "sample.mp3")
# mix_audio_dir = os.path.join(SAMPLE_OUTPUTS,"mixed-audio")
# os. makedirs(mix_audio_dir, exist_ok=True)

# og_audio_path = os.path.join(mix_audio_dir, 'og.mp3')
# final_audio_path = os.path.join(mix_audio_dir, 'final-audio.mp3')
# final_video_path = os.path.join(mix_audio_dir, 'final-video.mp4')

# video_clip = VideoFileClip(source_path)
# original_audio = video_clip.audio
# original_audio.write_audiofile(og_audio_path)

# background_audio_clip = AudioFileClip(source_audio_path)
# bg_music = background_audio_clip.subclip(0, video_clip.duration)

# bg_music = bg_music.volumex (0.10)
# # bg_music = bg_music.fx(volumex, 0.10)
# # bg_music.write_audiofile()

# final_audio = CompositeAudioClip([original_audio, bg_music])
# final_audio.write_audiofile(final_audio_path, fps=original_audio.fps)

# final_clip = video_clip.set_audio(final_audio)
# final_clip.write_videofile(final_video_path, codec='libx264', audio_codec="aac")



import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, "sample.mp4")
source_audio_path = os.path.join(SAMPLE_INPUTS, "sample.mp3")
mix_audio_dir = os.path.join(SAMPLE_OUTPUTS, "mixed-audio")
os.makedirs(mix_audio_dir, exist_ok=True)

og_audio_path = os.path.join(mix_audio_dir, 'og.mp3')
final_audio_path = os.path.join(mix_audio_dir, 'final-audio.mp3')
final_video_path = os.path.join(mix_audio_dir, 'final-video.mp4')

video_clip = VideoFileClip(source_path)
original_audio = video_clip.audio
original_audio.write_audiofile(og_audio_path)

background_audio_clip = AudioFileClip(source_audio_path)

# Fix: Make sure we don't try to subclip beyond the audio's duration
audio_duration = background_audio_clip.duration
video_duration = video_clip.duration

if audio_duration >= video_duration:
    # Audio is longer than video - take just the first part
    bg_music = background_audio_clip.subclipped(0, video_duration)
else:
    # Audio is shorter than video - loop it or just use what we have
    print(f"Warning: Audio ({audio_duration:.2f}s) is shorter than video ({video_duration:.2f}s)")
    # Option 1: Just use the audio as is (will end early)
    bg_music = background_audio_clip
    # Option 2: Loop the audio (uncomment below if you want looping)
    # bg_music = background_audio_clip.loop(duration=video_duration)

bg_music = bg_music.with_volume_scaled(0.10)  # Reduce volume to 10%

# Create composite audio
final_audio = CompositeAudioClip([original_audio, bg_music])
final_audio.write_audiofile(final_audio_path, fps=original_audio.fps)

final_clip = video_clip.with_audio(final_audio)
final_clip.write_videofile(final_video_path, codec='libx264', audio_codec="aac")

# Clean up
video_clip.close()
background_audio_clip.close()
final_clip.close()

print(f"Video with mixed audio saved to {final_video_path}")