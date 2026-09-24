from django.shortcuts import render
from rest_framework.views import APIView
from .services import save_to_db, generate_audio
from .serializers import VoiceSerializer
from better_profanity import profanity
from rest_framework.response import Response
from .models import Voice
from django.http import StreamingHttpResponse

# Create your views here.

class SaveVoicesView(APIView):
    def post(self, request):
        save_to_db()
        return Response({
            "message":"succesfully saved voices to database"
        })



class VoicesListView(APIView):
    def get(self,request):
        
        #GET GENDER IF USER SPECIFIED IN URL 
        gender = request.query_params.get("gender")
        
        # GET ALL VOICES 
        voices = Voice.objects.all()
        
        # IF USER REQUESTED SPECIFIC USER APPLY THE FILTER FOR THAT GENDER 
        if gender:
            voices = Voice.objects.filter(gender=gender)
            
        
        serializer = VoiceSerializer(voices, many=True)
        
        return Response({
            "Voices": serializer.data
        })
        
        
        
##### View Cretaed to call generated auid from services ########
class GenerateAudioView(APIView):
    def post(self, request):
        
        # Get text from user he want to convert to audio
        text = request.data.get("text")
        
        # Get voice ID the user want to use audio
        voice_id = request.data.get("voice_id")
        
        
        if profanity.contains_profanity(text):
            return Response(
                {"error": "Inappropriate words detected"},
                status=400)
        
        audio = generate_audio(text, voice_id)
        
        return StreamingHttpResponse(
            audio,
            content_type="audio/mpeg"
        )
        
        