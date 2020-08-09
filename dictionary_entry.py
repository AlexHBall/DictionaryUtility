from lxml import etree
import os
import unicodedata

class Dictonary_Entry:
    def __init__(self, word):
        root = self.load_dict(word)
        element = self.search_word(word, root)
        if not element:
            raise Exception("Word not found")
        self.defitions = self.get_body_variants(element)   

    def load_dict(self,word):
        def strip_accents(text):
            try:
                text = unicode(text, 'utf-8')
            except NameError: # unicode is a default on python 3 
                pass

            text = unicodedata.normalize('NFD', text)\
                .encode('ascii', 'ignore')\
                .decode("utf-8")

            return str(text)

        first_character = strip_accents(word[0].lower())
        script_dir = os.path.dirname(__file__)
        relative_path = "data/{}.xml".format(first_character)
        abs_file_path = os.path.join(script_dir, relative_path)

        with open(abs_file_path) as f:
            root = etree.parse(f)

        return root


    def search_word(self,word, root):
        try:
            element = root.xpath("//entree[@terme='{}']".format(word.upper()))[0]
        except IndexError:
            return None
        return element


    def get_body_variants(self,element):
        variants = element.findall(".//corps/variante")
        texts = []
        for variant in variants:
            text = variant.text
            if text is not None:
                #TODO: Handle unicode properly
                text = text.replace("\n","")
                text = text.replace("\xa0"," ")
                texts.append(text.strip())
        return tuple(texts)