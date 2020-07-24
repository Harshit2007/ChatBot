from nltk.chat.util import Chat, reflections
print("Hi, I'm QWERTY and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is QWERTY, I'm a chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing very well", "I am great!"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*)created(.*)",
        ["Harshit created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Delhi, India',]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Chess",]
    ],
    [
        r"who (.*) (moviestar|actor|actress)?",
        ["Those who create good movies are my favourite"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['I did not understand please try again']
    ],
]

reflections = {
    "i": "you",
    "i am": "you are",
    "i was": "you were",
    "i'd": "you would",
    "i'll": "you will",
    "i'm": "you are",
    "i've": "you have",
    "me": "you",
    "my": "your",
    "you": "me",
    "you are": "i am",
    "you were": "i was",
    "you'll": "i will",
    "you've": "i have",
    "your": "my",
    "yours": "mine"
    }
chat = Chat(pairs, reflections)
chat.converse()
