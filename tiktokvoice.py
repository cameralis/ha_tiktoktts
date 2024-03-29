# author: GiorDior aka Giorgio
# date: 12.06.2023
# topic: TikTok-Voice-TTS
# version: 1.0
# credits: https://github.com/oscie57/tiktok-voice

import threading, requests, base64
from .const import SUPPORT_LANGUAGES

ENDPOINTS = ['https://tiktok-tts.weilnet.workers.dev/api/generation', "https://tiktoktts.com/api/tiktok-tts"]
current_endpoint = 0
# in one conversion, the text can have a maximum length of 300 characters
TEXT_BYTE_LIMIT = 300

# create a list by splitting a string, every element has n chars
def split_string(string: str, chunk_size: int) -> list[str]:
    words = string.split()
    result = []
    current_chunk = ''
    for word in words:
        if len(current_chunk) + len(word) + 1 <= chunk_size:  # Check if adding the word exceeds the chunk size
            current_chunk += ' ' + word
        else:
            if current_chunk:  # Append the current chunk if not empty
                result.append(current_chunk.strip())
            current_chunk = word
    if current_chunk:  # Append the last chunk if not empty
        result.append(current_chunk.strip())
    return result

# checking if the website that provides the service is available
def get_api_response() -> requests.Response:
    url = f'{ENDPOINTS[current_endpoint].split("/a")[0]}'
    response = requests.get(url)
    return response

# saving the audio file
def save_audio_file(base64_data: str, filename: str = "output.mp3") -> None:
    audio_bytes = base64.b64decode(base64_data)
    with open(filename, "wb") as file:
        file.write(audio_bytes)

# send POST request to get the audio data
def generate_audio(text: str, voice: str) -> bytes:
    url = f'{ENDPOINTS[current_endpoint]}'
    headers = {'Content-Type': 'application/json'}
    data = {'text': text, 'voice': voice}
    response = requests.post(url, headers=headers, json=data)
    return response.content

# creates an text to speech audio file
def tts(text: str, voice: str = "none") -> (bytes, str):
    # checking if the website is available
    global current_endpoint

    if get_api_response().status_code != 200:
        current_endpoint = (current_endpoint + 1) % 2
        if get_api_response().status_code == 200:
            return (bytes(), "Service available!")
        else:
            return (bytes(), f"Service not available and probably temporarily rate limited, try again later...")
    
    # checking if arguments are valid
    if voice == "none":
        return (bytes(), "No voice has been selected")
    
    if not voice in SUPPORT_LANGUAGES:
        return (bytes(), "Voice does not exist")

    if len(text) == 0:
        return (bytes(), "Insert a valid text")

    # creating the audio file
    try:
        if len(text) < TEXT_BYTE_LIMIT:
            audio = generate_audio((text), voice)
            if current_endpoint == 0:
                audio_base64_data = str(audio).split('"')[5]
            else:
                audio_base64_data = str(audio).split('"')[3].split(",")[1]
            
            if audio_base64_data == "error":
                return (bytes(), "This voice is unavailable right now")
                
        else:
            # Split longer text into smaller parts
            text_parts = split_string(text, 299)
            audio_base64_data = [None] * len(text_parts)
            
            # Define a thread function to generate audio for each text part
            def generate_audio_thread(text_part, index):
                audio = generate_audio(text_part, voice)
                if current_endpoint == 0:
                    base64_data = str(audio).split('"')[5]
                else:
                    base64_data = str(audio).split('"')[3].split(",")[1]

                if audio_base64_data == "error":
                    return (bytes(), "This voice is unavailable right now")
            
                audio_base64_data[index] = base64_data

            threads = []
            for index, text_part in enumerate(text_parts):
                # Create and start a new thread for each text part
                thread = threading.Thread(target=generate_audio_thread, args=(text_part, index))
                thread.start()
                threads.append(thread)

            # Wait for all threads to complete
            for thread in threads:
                thread.join()

            # Concatenate the base64 data in the correct order
            audio_base64_data = "".join(audio_base64_data)
            
        return (base64.b64decode(audio_base64_data), "")

    except Exception as e:
        return (bytes(), "Error occurred while generating audio:", str(e))
