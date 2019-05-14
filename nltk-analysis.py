import nltk
from nltk.corpus import stopwords
from nltk.corpus import brown


codeTemplate='''
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

def findMaxSimilarity(word, filename):
    capFile = open(filename,'r')
    #获取全部到capability字典
    capDict = {}
    for line in capFile:
        print(line)
        capArray = line.strip('\n').split(',')
        if len(capArray) < 3:
            continue
        capDict[capArray[0]] = capArray[2:][0].split(' ')
    # a = capDict['capability.garageDoorControl'][0]
    # print(capDict)

    

file = open('ifttt-smartthings-when.txt')
for line in file:
    text = line
    text_list = nltk.word_tokenize(text)
    # 去标点
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    text_list = [word for word in text_list if word not in english_punctuations]
    # 去停止词
    # stops = set(stopwords.words("english"))
    # text_list = [word for word in text_list if word not in stops]
    cixing = nltk.pos_tag(text_list,tagset='universal')
    print(cixing)
    # 处理when和whenever的位置
    try:
        indexOfWhen = text_list.index('when')
    except ValueError:
        indexOfWhen = text_list.index('whenever')
    print(indexOfWhen)
    beforeWhenArr = text_list[0 : indexOfWhen]
    afterWhenArr = text_list[indexOfWhen+1 : len(cixing)]
    cixingBefore = nltk.pos_tag(beforeWhenArr,tagset='universal')
    cixingAfter = nltk.pos_tag(afterWhenArr,tagset='universal')
    lenOfCixingBefore = len(beforeWhenArr)
    lenOfCixingAfter = len(afterWhenArr)
    index = 0
    for word, wordcixing in cixingBefore:
        if(index != lenOfCixingBefore and wordcixing == 'VERB' or wordcixing == 'PRT'):
            codeTemplate.replace('$name', text)
            codeTemplate.replace('$description', text)
            codeTemplate.replace('$capability_action', word)
            # codeTemplate.replace('$')

        print(word, wordcixing)

