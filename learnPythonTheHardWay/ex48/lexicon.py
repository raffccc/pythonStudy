from string import lower

lexicon = { 'direction': [ 'north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back' ],
            'verb': [ 'go', 'stop', 'kill', 'eat' ],
            'stop': [ 'the', 'in', 'of', 'from', 'at', 'it' ],
            'noun': [ 'door', 'bear', 'princess', 'cabinet' ]
          }

def scan(text):
    words = get_lower_split_string(text)
    if words:
        wordsClassifications = []
        
        for word in words:
            wordsClassifications.append(get_word_classification(word))
            
        return wordsClassifications
    
    return None

def get_lower_split_string(text):
    if text:
        return text.split()
    return None

def get_word_classification(word):
    if word:
        wordToLower = lower(word)
        for item in lexicon.items():
            if wordToLower in item[1]:
                return (item[0], word)
        
        try:
            return ('number', int(word))
        except ValueError:
            return ('error', word)
        
    return ('error', None)