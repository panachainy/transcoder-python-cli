import ffmpeg

# Set the input URL and output file path
input_url = 'https://storage.googleapis.com/bucket-name/path-to-file/xxxxxxxxxx.m3u8'
output_file = 'results/output.mp4'

# Use ffmpeg-python to convert the M3U8 file to an MP4 file
(
    ffmpeg
    .input(input_url)
    .output(output_file, c='copy')
    .run()
)
