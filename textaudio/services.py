from config.settings import ELEVEN_LABS_API_KEY

from elevenlabs.client import ElevenLabs
from .models import Voice


# Creates an ElevenLabs API client using the API key stored in Django settings
client = ElevenLabs(
    api_key=ELEVEN_LABS_API_KEY
)

###### FUNCTION TO GET VOICES FROM ELEVENLABS #########
def get_voices():
    response = client.voices.get_all() # FETCH ALL AVAILABLE VOICES FROM ELEVEN LABS
    return response.voices # RETURN ONLY VOICES




##### FUNCTION TO MAKE EXTRACT VOICES AND SEPARATING THEM BASED ON GENDER #########
def extract_voices():
    #fetch voices and store in variable "voices"
    voices = get_voices()
    
    # Loop over voices to see gender
    
    for voice in voices:
        # IF GENDER IS MALE STORE THIS VOICE IN "MALE_VOICES" LIST
        male_voices = [
            voice for voice in voices
            if voice.labels.get("gender") == "male"
        ]

    # IF GENDER IS FEMALE STORE THIS VOICE IN "FEMALE_VOICES" LIST
        female_voices = [
            voice for voice in voices
            if voice.labels.get("gender") == "female"
        ]
        
    # ADD THE FIRST 5 MALE AND FIRST 5 FEMALE VOICES AND STORE THEM IN VARIABLE SELECTED_VOICES 
        selected_voices = male_voices[:5] + female_voices[:5]
        return selected_voices
        
        
        
#### FUNCTION TO SAVE VOICES TO DATABASE VOICE TABLE ########
def save_to_db():
    selected_voices= extract_voices()
    
    for voice in selected_voices:
    
    #LOOP OVER VOICES IF THE VOICE WITH ITS VOICE_ID ALREADY EXISTS GET IT IF NOT THEN CREATE IT
        Voice.objects.get_or_create(
            voice_id = voice.voice_id,
            defaults = {
                "name":voice.name,
                "gender":voice.labels.get("gender"),
            }
        )
        
        
### FUNCTION TO SEND "TEXT AND VOICE ID" TO ELEVEN LABS TO GENERATE AUDIO #####
def generate_audio(text, voice_id):
    
    # Send text and voice ID to ElevenLabs
    audio = client._text_to_speech.convert(
        voice_id = voice_id,
        text = text
    )
    # Return generated audio
    return audio