# transcoder-python-cli

## development

### setup

```sh
python3 -m venv env
```

### prerequisite

```sh
brew install ffmpeg
# check
ffmpeg -version
```

### activate env (do every time before dev)

```sh
source env/bin/activate
```

## Commands

You can read in `Makefile`

## Use

```sh
# _ _ public-url-of-s3-file.m3u8 output.mp4 --upload
python convert.py https://storage.googleapis.com/bucket-name/xxxxxxxxx.m3u8 --output_file=xxxxx.mp4 --upload

# help
python convert.py -h
```
