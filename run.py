import argparse
import time
from pathlib import Path

import soundfile
import speech_recognition as sr

parser = argparse.ArgumentParser(description="Transcribes audio into Cantonese")
parser.add_argument("in_audio", type=Path, help="path to the input audio")
parser.add_argument("out_text", type=Path, help="path to the output text file")
args = parser.parse_args()
in_audio = args.in_audio.resolve()
out_text = args.out_text


def stt_Cantonese(audio_file):

    # Write the audio data back to the same file, using the original sample rate and a 16-bit PCM encoding to avoid the ValueError: Audio file could not be read as PCM WAV, AIFF/AIFF-C, or Native FLAC; check if file is corrupted or in another format
    data, samplerate = soundfile.read(audio_file)
    soundfile.write(audio_file, data, samplerate, subtype="PCM_16")

    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio, language="yue-HK")  # yue-HK = Cantonese
        return text

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )
        return None


start_time = time.time()

print(f"Transcribing {in_audio.name}")
transcript = stt_Cantonese(str(in_audio))
with open(out_text, "w") as f:
    f.write(transcript)
end_time = time.time()
elapsed_time = round(end_time - start_time, 2)
print(f"Transcript exported to {out_text.name}")
print(f"Elapsed time: {elapsed_time} second(s)")
