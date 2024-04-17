# Process all the slots called from the inference function here

import config.functions as func
from config.functions import make_request
from system.gtts import play_audio_response


def infer1(inference):
    # Store the slots for the passed inference
    slots = inference.slots

    # TODO: Process response
    out = make_request()

    print(out)

    # Play the responses generated based on the slots
    play_audio_response(response)


def infer2(inference):
    # Store the slots for the passed inference
    slots = inference.slots

    # TODO: Process response
    out = make_request()

    print(out)

    # Play the responses generated based on the slots
    play_audio_response(response)
    