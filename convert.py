import argparse
import ffmpeg

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument for the input URL
parser.add_argument('input_url', help='URL of the input M3U8 file')

# Parse the command line arguments
args = parser.parse_args()

# Set the input URL and output file path
input_url = args.input_url
output_file = 'results/output.mp4'

# Use ffmpeg-python to convert the M3U8 file to an MP4 file
(
    ffmpeg
    .input(input_url)
    .output(output_file, c='copy')
    .run()
)
