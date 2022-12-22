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
    .overwrite_output()
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
        f'{api_endpoint}/video/v1/uploads',
        auth=(api_key, api_secret),
        json={"new_asset_settings":{"playback_policy":["public"]},"cors_origin":"*"}
    )
    response.raise_for_status()
    # asset_id = response.json()['data']['id']

    # print('asset_id',asset_id)
    asset_url = response.json()['data']['url']

    # Open the MP4 file
    with open(output_file, 'rb') as file:
        # Send an HTTP PUT request to the Google Cloud Storage API endpoint
        gcpRes = requests.put(
            asset_url,
            # params=params,
            data=file
        )

    # Print the response from the Google Cloud Storage API
    print('GCP storage status',gcpRes)
    print('Try to check on mux asset waiting Upload from GCP to Mux automatic.')