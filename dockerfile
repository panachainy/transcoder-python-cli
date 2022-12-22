FROM python:3.10.6-slim

RUN apt-get -y update
RUN apt-get install -y ffmpeg

# Copy the code file to the image
COPY convert.py /app/convert.py
COPY requirements.txt /app/requirements.txt

# Install ffmpeg and requests libraries
RUN pip install -r /app/requirements.txt

# Set the working directory to the app directory
WORKDIR /app

# Run the script when the container starts
CMD ["python", "convert.py"]
