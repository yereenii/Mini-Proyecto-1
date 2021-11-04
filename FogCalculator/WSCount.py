import re
import sys
from FogCalculator.SyllableCounter import syllables
from FogCalculator.CompoundWord import split

class WSCount:
    globalCounting=-1
    globalWordCount=-1
    globalSentenceCount=-1

    def get_wscount(self, nombre_archivo):
        try:
            FileObject = open(nombre_archivo, "r")
        except FileNotFoundError:
            with open("FileNotFound.txt", "w+") as new_file:
                new_file.write("File does not exist, please try again by placing a valid file named 'TestDocument.txt' in "
                            "current directory")
            sys.exit(0)
        file_contents = FileObject.read()
        self.globalCounting=self._counting(file_contents)
        self.globalWordCount=self._wordcount(file_contents)
        self.globalSentenceCount=self._sentencecount(file_contents)
        FileObject.close()

    def _counting(self, file_contents):
        syllablecount = 0
        beg_each_Sentence = re.findall(r"\.\s*(\w+)", file_contents)
        capital_words = re.findall(r"\b[A-Z][a-z]+\b", file_contents)
        words = file_contents.split()
        for word in words:
            if word not in capital_words and len(word) >= 3: #all lower case words

                if syllables(word) >= 3 and len(split(word)) == 1:
                    syllablecount += 1

            if word in capital_words and word in beg_each_Sentence: #beginning of each sentence is uppercase

                if syllables(word) >= 3:
                    syllablecount += 1
        return syllablecount

    def _wordcount(self, file_contents):
        # Regex to match all words, hyphenated words count as a compound words
        return len(re.findall("[a-zA-Z-]+", file_contents))

    def _sentencecount(self, file_contents):
        #regex to count sentences, can end with a period, "?" or "!"
        return (len(re.split("[.!?]+", file_contents))-1)
