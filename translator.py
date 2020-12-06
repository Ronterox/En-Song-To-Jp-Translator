def contains_word(sentence, word, separator):
    sentence = sentence.split(separator)
    for w in sentence:
        if w == word:
            return True
    return False


def getTranslation(word):
    with open('data.txt', 'r+') as data:
        if word != '\n' and word != ' ':
            translated = False
            word = word.lower().strip()
            data.seek(0)
            data_read = data.readline().lower()
            while len(data_read) > 0:  # has read something
                if contains_word(data_read, word, ':'):  # Has translation in data.txt line
                    data_read = data_read.split(':')
                    if len(data_read) > 1:
                        word = data_read[1]
                    translated = True
                    break
                data_read = data.readline()
            word = word.strip()
            if not translated:
                data.read()  # put it at the end
                data.write(word + ': ' + word + '\n')
        return word


def transLateLyrics(lyricsFile, resultFile):
    with open(lyricsFile, 'r') as lyrics, open(f'translated-{resultFile}.txt', 'a') as resultFile:
        resultFile.truncate(0)  # reduces the size of the file to 0
        for line in lyrics:
            if len(line) > 0:
                line = line.split(' ')
                for counter, word in enumerate(line, 1):  # positions it in song form
                    if counter == len(line):
                        resultFile.write(getTranslation(word) + '\n')
                    else:
                        resultFile.write(getTranslation(word) + ' ')


transLateLyrics('lyrics.txt', 'helloWorld')
