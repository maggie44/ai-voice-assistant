<div align="center">
   <img width="150" alt="Logo" src="https://github.com/mesh-of-things/api/assets/64841595/8fdf66f2-8b31-42d9-8ff7-98dd6d9bb984">
   <br>
   <h3 align="center">AI voice assistant running on a Raspberry Pi</h3>
</div>
<div align="center">
  <img src="https://github.com/maggie44/ai-voice-assistant/actions/workflows/deploy.yml/badge.svg"
      alt="Deploy">
</div>
<br>

# **WIP!**

An AI voice assistant running on a Raspberry Pi 4. This project brings together [previous modular projects](#how-it-is-built) I have worked on to create an AI voice assistant. It draws on [Picovoice](https://picovoice.ai) for voice recognition at the edge, and uses Cloudflare GPUs, both with very generous free allowances for everyday operation. It allows use of a number of different AI LLMs including Llama2, Gemma and others.

## Usage

- Flash an image from the Releases section. The `dev` image allows SSH access on port `22222`, whereas `prod` has the ssh port closed.
- Boot the Raspberry Pi. A WiFi hotspot will become available to your devices called `AI Voice Assistant`. Connect and a captive portal will appear with a user interface allowing you to connect the Pi to your WiFi network, and configure the environment variables required:

```
AI_CLOUDFLARE_TOKEN=xyz
AI_PICO_ACCESS_KEY=xyz
```

- Get started by saying `hey millie`. Your Raspberry Pi will reply `yes` and wait for your instruction. The instruction is passed to an AI LLM for processing. A response to your question is streamed back to your device and read out loud to you.

## Hardware

This project is built for the Raspberry Pi 4. On top of the Raspberry Pi 4 goes the [ReSpeaker 2-Mics Pi Hat](https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT.html) which provides the microphones and speaker output for Picovoice. I then used a [3w Mono Enclosed Speaker](https://thepihut.com/products/mono-enclosed-speaker-3w-4-ohm) plugged in to the HAT for sound output.

All of this hardware is push fit, with no soldering required.

## How it is built

1. A GitHub Action in this repository uses `Dockerfile.ai-assistant` to build out-of-tree kernel modules for the ReSpeaker 2-Mics Pi Hat.
2. `seeed-2mic-voicecard.dtbo` is inserted into the overlays for the Pi in the downloaded OS images and the Pi's `config.txt` is updated to specify the required device tree overlays and device tree parameters.
3. `Dockerfile.ai-assistant` copies the required code and sets up the environment.
4. Some of my [earlier work](https://github.com/balena-os/kernel-module-build/commit/135178ba554150d59d302d7752341c395db30693) on the kernel builder loads the other kernel modules on first boot of the Pi.
5. Some of my other earlier projects provides an API to interact with the Raspberry Pi WiFi configuration, and a web interface for configuring WiFi hotspots and setting required environment variables (`Dockerfile.ai-assistant`). The starter interface is customisable using the `config.yml` file to provide the features required for different projects. See the docs of each for more info:

- [balena Starter Interface](https://github.com/balena-io-experimental/starter-interface), a customisable modular interface for edge devices.
- [Python WiFi Connect](https://github.com/balena-labs-research/python-wifi-connect), an API for interacting with the WiFi on embedded Linux devices.
- [Picovoice balena CLI Demo](https://github.com/balena-io-experimental/picovoice-balena-cli), a Python voice assistant and GoLang CLI for identifying devices on local networks.

6. Picovoice provides the wake word functionality.
7. Cloudflare GPUs process the voice requests and also the speech-to-text.
8. Google Text to Speech API is also utilised for returning responses.

## TODO:

This is not a high priority project, however other features that I may get around to adding in the future (contributions welcome):

- Allow voice commands to allow sending the output to different sources
- Allow AI to call functions that allow interaction with the hardware and peripheries
- Perform more at the edge
- Replace OS with an OS with better UX and atomic updates
