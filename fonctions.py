"""Ce fichier contient les fonctions de l'application"""

import boto3
import os
import sys
import subprocess
from picamera import PiCamera
from random import choice
from time import sleep
from donnees import *
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
from tempfile import gettempdir

#Démarrage de la caméra et prise de la photo
camera=PiCamera()

camera.start_preview()
sleep(2)
camera.capture(photo_prise)
camera.stop_preview()


#on enregistre la photo prise sur le bucket S3
def upload_photo(photo_prise):
	s3=boto3.resource('s3')
	s3.Bucket(bucket).upload_file(photo, photo_aws)


#La photo est analysée pour voir si elle correspond à un visage existant dans la collection
detection=boto3.client('rekognition')

visage=detection.search_faces_by_image(
	CollectionId= collection_visages,
	Image={
	'S3Object':{'Bucket': bucket, 'Name':photo_aws
	}
	},
	MaxFaces=2,
	FaceMatchThreshold=50)
#On va chercher le prénom du visage qui est stocké dans le l'ExternalImageId. 
#Cet Id est dans un ditionnaire imbriqué au sein de la réponse renvoyée par aws
a= response['FaceMatches']
prenom= response['FaceMatches'][0]['Face']['ExternalImageId']


#On choisit une phrase à transmettre à polly avec le prénom lié au visage détecté

def choix_phrase():
	if not a:
		phrase=choice(phrase_copains).format(prenom)
	else:
		phrase=choice(phrase_inconnu)

#Synthétisation de la voix avec Polly
def retour_vocal():
	voix= boto3.client("polly")

	try:
    	# Request speech synthesis
    	response = voix.synthesize_speech(Text="<speak>Hi </speak>".format(prenom), TextType='ssml', OutputFormat="mp3",
                                        VoiceId="Emma")
	except (BotoCoreError, ClientError) as error:
    	# The service returned an error, exit gracefully
    	print(error)
    	sys.exit(-1)

	# Access the audio stream from the response
	if "AudioStream" in response:
    	# Note: Closing the stream is important as the service throttles on the
    	# number of parallel connections. Here we are using contextlib.closing to
    	# ensure the close method of the stream object will be called automatically
    	# at the end of the with statement's scope.
    	with closing(response["AudioStream"]) as stream:
        	output = os.path.join(gettempdir(), "speech.mp3")

        	try:
            	# Open a file for writing the output as a binary stream
            	with open(output, "wb") as file:
                	file.write(stream.read())
        	except IOError as error:
            	# Could not write to file, exit gracefully
            	print(error)
            	sys.exit(-1)

	else:
    # The response didn't contain audio data, exit gracefully
    sys.exit(-1)

	# Play the audio using the platform's default player
	if sys.platform == "win32":
    	os.startfile(output)
	else:
    	# the following works on Mac and Linux. (Darwin = mac, xdg-open = linux).
    	opener = "open" if sys.platform == "darwin" else "xdg-open"
	subprocess.call([opener, output])