# Process all your intents here. Based on the initial understanding,
# the appropriate function is called to process the slots

from config.slots import infer2
from config.slots import infer1
from system.gtts import play_audio_response


def process_inference(inference):
    if inference.is_understood:
        if inference.intent == "infer1":
            infer1(inference)
        elif inference.intent == "infer2":
            infer2(inference)
        else:
            raise NotImplementedError()
    else:
        play_audio_response("I'm afraid I don't understand")
