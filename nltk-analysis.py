import nltk
from nltk.corpus import stopwords
from nltk.corpus import brown


smartapptemplate='''
definition(
    name: "$name",
    namespace: "smartthings",
    author: "SmartThings",
    description: "$description",
    category: "Convenience",
    iconUrl: "https://s3.amazonaws.com/smartapp-icons/Meta/light_presence-outlet.png",
    iconX2Url: "https://s3.amazonaws.com/smartapp-icons/Meta/light_presence-outlet@2x.png"
)

preferences {
	section("condition..."){
		input "condition_sensor", "capability.$capability_condition", multiple: true
	}
	section("action..."){
		input "action_sensor", "capability.$capability_action", multiple: true
	}
}

def installed()
{
	subscribe(condition_sensor, "$subscribe", presenceHandler)
}

def updated()
{
	unsubscribe()
	subscribe(condition_sensor, "$subscribe", presenceHandler)
}

def presenceHandler(evt)
{
	action_sensor.$method()
}

'''
file = open('ifttt-smartthings-when.txt')
for line in file:
    text = line
    text_list = nltk.word_tokenize(text)
    #去标点
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    text_list = [word for word in text_list if word not in english_punctuations]
    #去停止词
    # stops = set(stopwords.words("english"))
    # text_list = [word for word in text_list if word not in stops]
    cixing = nltk.pos_tag(text_list,tagset='universal')
    print(cixing)
    for each in cixing:
        print(each[0])
    
    break