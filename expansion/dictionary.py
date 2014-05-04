import tempfile
import lingotranslator.translator as lingo_translator

class EnglishDictionary:
    def __init__(self):
        f = open("../res/freeling.src", "r")
        self.words = [l.split()[0].lower() for l in f.readlines()]
        f.close()

    def exists(self, word):
        return word.lower() in self.words

class GenericDictionary:
    def __init__(self, filename):
        f = open(filename, "r")
        self.dictionary = dict(l.strip("\n").split("\t") for l in f.readlines())
        f.close()

    def translate(self, word):
        try:
            return self.dictionary[word.lower()]
        except:
            return word

class LingoDictionary:
    def __init__(self):
        self.mode = "YYN"
        lingo_translator.init(self.mode)

    def translate(self, line):
        return lingo_translator.translate(line)
