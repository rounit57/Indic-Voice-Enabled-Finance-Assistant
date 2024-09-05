
"""Our server API functions"""
import requests
import json
import base64
import os
from pydub import AudioSegment


def transcribe_audio(asr_url, asr_payload, asr_file_path, file_name):
    with open(asr_file_path, 'rb') as audio_file:
        files = [('file', (file_name, audio_file, 'application/octet-stream'))]
        try:
            response = requests.post(asr_url, headers={}, data=asr_payload, files=files)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code}, {response.text}")
                return None
        except Exception as e:
            print(f"Exception occurred during transcription: {str(e)}")
            return None
 
def ASR_call(source_language, audio_base64):
    # Decode base64-encoded 3GP data and save as a .3gp file
    decoded_3gp_data = base64.b64decode(audio_base64)
    with open("output.3gp", "wb") as f:
        f.write(decoded_3gp_data)
 
    # Convert the .3gp file to .wav format
    audio = AudioSegment.from_file("output.3gp", format="3gp")
    file_name = "output.wav"
    audio.export(file_name, format="wav")
    
    # Check if the file was created
    if not os.path.exists(file_name):
        print("Error: WAV file was not created.")
        return None
    
    # Check if the WAV file is non-empty
    if os.path.getsize(file_name) == 0:
        print("Error: WAV file is empty.")
        return None
 
    # Play the file and check manually (for debugging)
    # print(f"File {file_name} created successfully, size: {os.path.getsize(file_name)} bytes.")
    
    asr_url = "http://121.242.232.220:5000/decode"
    # asr_url = api_asr
 
    asr_payload = {
        'vtt': 'true',
        'language': source_language
    }
 
    asr_result = transcribe_audio(asr_url, asr_payload, file_name, file_name)
 
    if asr_result:
        if asr_result.get("status") == "success":
            text_from_audio = asr_result.get("transcript", "")
            return text_from_audio
        else:
            print(f"ASR failed with message: {asr_result.get('message', 'No message')}")
    else:
        print(f"Failed to transcribe {file_name}")
    
    return None
 
def MT_call(source_language, target_language, text_from_audio):
    mt_url = "http://121.242.232.220:5002/mt"
    # mt_url = api_mt
 
    payload = {
        'src_language':source_language,
        'tgt_language':target_language,
        'transcript': text_from_audio
        }
    
    response = requests.post(mt_url,data = payload,verify=False)
    translated_text = response.json()['mt_out']
 
    return translated_text
 
def TTS_call(target_language, translated_text):
    tts_url = "http://121.242.232.220:5010/tts"
    # tts_url = api_tts
    gender = 'male' 
   
    payload = json.dumps({
            "input": translated_text,
            "gender": gender,
            "lang": target_language,
            "alpha": 1,
            "segmentwise":"True"
             })
    headers = {
    'Content-Type': 'application/json'
    }
 
    response = requests.request("POST", tts_url, headers=headers, data=payload)
 
    text_to_audio = response.json()['audio']
 
    return text_to_audio
