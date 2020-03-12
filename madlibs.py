class MadLibs:

    def __init__(self):
        self.noun = ''
        self.verb = ''
        self.adjective = ''
        self.adverb = ''

    def get_inputs(self):
        print()
        self.noun = input("Type in a NOUN: ")
        self.verb = input("Type in a VERB: ")
        self.adjective = input("Type in an ADJECTIVE: ")
        self.adverb = input("Type in an ADVERB: ")

    def get_mad_libs(self, name):
        with open(f'madlibsfiles/{name}', 'r') as file:
            ml = file.read()
        ml = ml.replace("noun",  self.noun)
        ml = ml.replace("adverb",  self.adverb)
        ml = ml.replace("verb",  self.verb)
        ml = ml.replace("adjective",  self.adjective)
        print()
        print(ml)        