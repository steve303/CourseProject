import emoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
nltk.download('punkt')
import string
import re
def preprocess_text(input_data):
    data = input_data 

    # Removing tags
    #data = tf.strings.regex_replace(input_data, "@USER", " ")
    #data = tf.strings.regex_replace(data, "<URL>", " ")

    # Process emojis
    #data = emoji.demojize(data, delimiters=(" ", " "))

    # Remove stopwords/emojis
    stop_words = set(stopwords.words("english"))
    emojis = set(emoji.UNICODE_EMOJI_ALIAS)
    word_tokens = word_tokenize(data) 
    data = []
    for w in word_tokens:
        # Modify below for stopwords and/or emojis
        if w not in emojis:
            data.append(w)
    data = (" ").join(data)

    # Remove non alpha-numeric characters (not sure if a good idea)
    #data = re.sub(r'[^\w'+' .'+']', '', data)
   
    return data