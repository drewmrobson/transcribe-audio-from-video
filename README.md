# transcribe-audio-from-video
Get a text transcript of a video.

I built this dumb little app for myself and maybe you can find it useful too?

- [Overview](#overview)
- [Dependencies](#dependencies)
- [Usage](#usage)

## Overview

Get a text transcript for a provided video file (e.g. MP4). I use this for getting a text version of interesting YouTube videos. This is an implementation of this article https://medium.com/nerd-for-tech/transcribe-audio-from-video-with-azure-cognitive-services-a4589a12d74f.

## Dependencies

This project is implemented in Python and uses Azure Speech Services. An Azure Speech Services API Key is required.

## Usage

```bash
python main.py <video_name> <speech_subscription_key>
```
