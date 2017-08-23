"""ce fichier contient les données utilisées par l'application"""

#liste des phrases si la personne est reconnue (format ssml) 
phrases_copain=[
"<speak> Hello {0}, it's nice to see you <break time='150ms'/> </speak>",
"<speak> Hi {0}. How are you today? <break time='2s'/> You realize you're talking to a machine, right? <break time='150ms'/> </speak>",
"<speak> Hello {0}, you look <emphasis> splendid </emphasis> today <break time='150ms'/> </speak>",
"<speak> Welcome {0}, long time no see <break time='150ms'/> </speak>",
"<speak> Hey {0}, try not to spill any beer this time, ok? <break time='150ms'/> </speak>",
"<speak> Hi {0}, it's me! Polly! Remember me? <break time='150ms'/> </speak>",
"<speak> Oh, it's {0} again. <break time='150ms'/> Do you really have to come here that often? <break time='150ms'/> </speak>",
"<speak> My dear {0}, you looked better the last time I saw you <break time='150ms'/> </speak>"]

#liste des phrases si la personne n'est pas reconnue (format ssml)
phrases_inconnu=[
"<speak>Hi, my name is Polly. What's your name?<break time='1500ms'/> Well, I don't really care. I can't even hear you anyway. <break time='150ms'/> </speak>",
"<speak>Hi stranger, pleasure meeting you. You look <emphasis level='strong'> really </emphasis> hot <break time='150ms'/> </speak>",
"<speak>Oh. God. <break strength='x-strong' /> You are not a beautiful person, are you? <break time='150ms'/> </speak>"]

#liste des phrases si émotion détectée (format ssml)
phrases_emotion=[
"<speak> Hello {0}. You look {1} today <break time='150ms'/> </speak>",
"<speak> Hi {0}. You seem {1}, grab a beer and get one for me please <break time='150ms'/> </speak>",
"<speak> My sensors show that you are {1}, but I do not really give a damn about your feelings. Goodbye {0} <break time='150ms'/> </speak>",
"<speak> Your level of pheromones indicates that you are {1}, <break time='700ms'/> you should have sex {0} <break time='500ms'/> really <break time='150ms'/> </speak>"
"<speak> My lovely {0} <break time='300ms' /> You are <emphasis level='strong'> horrible </emphasis> when you look {1}, but I guess nobody told you <break time='150ms' /> </speak>"]

#liste des ExternalId
prenoms_copains={
	"ExternalId":'Momo',
	"ExternalId":'Flo',
	"ExternalId":'Mathieu',
	"ExternalId":'Aurelie',
	"ExternalId":'Hugo',
	"ExternalId":'Camille',
	"ExternalId":'The guy with a shitty name',
	"ExternalId":'Pauline',
	"ExternalId":'my Master',
	"ExternalId":'Segolene',
	"ExternalId":'Aleen',
	"ExternalId":'Jack',
	"ExternalId":'Adrian',
	"ExternalId":'Asmaa',
	"ExternalId":'Sleeman',
	"ExternalId":'Teebale'
}