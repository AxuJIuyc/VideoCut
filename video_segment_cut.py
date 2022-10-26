from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("input_file", time_start_sec, time_end_sec, targetname="output_file")
