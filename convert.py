import argparse
import ffmpeg
import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments for the input URL, output file name, and upload flag
parser.add_argument('input_url', help='URL of the input M3U8 file')
parser.add_argument('--output_file', default='default_output.mp4', help='Name of the output MP4 file %(prog)s (default: %(default)s)')
parser.add_argument('--upload', action='store_true', help='Upload the output MP4 file to a Mux asset')

# Parse the command line arguments
args = parser.parse_args()

# Set the input URL and output file path
input_url = args.input_url
output_file = args.output_file

# Use ffmpeg-python to convert the M3U8 file to an MP4 file
(
    ffmpeg
    .input(input_url)
    .output(output_file, c='copy')
    .run()
)

# Check if the user wants to upload the output file to a Mux asset
if args.upload:
    # Set your Mux API keys from environment variables
    api_key = os.environ['MUX_API_KEY']
    api_secret = os.environ['MUX_API_SECRET']

    # Set the Mux API endpoint
    api_endpoint = 'https://api.mux.com'

    # Create a Mux asset
    response = requests.post(
        f'{api_endpoint}/videos',
        auth=(api_key, api_secret),
        json={'new_asset_settings': {'playback_policy': 'public'}}
    )
    response.raise_for_status()
    asset_id = response.json()['data']['id']

    # Upload the output file to the Mux asset
    with open(output_file, 'rb') as file:
        requests.put(
            f'{api_endpoint}/assets/{asset_id}/source',
            auth=(api_key, api_secret),
            headers={'Content-Type': 'video/mp4'},
            data=file
        ).raise_for_status()
