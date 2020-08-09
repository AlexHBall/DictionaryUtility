from lxml import etree
import os

class Dictonary_Entry:
    def __init__(self, word):
        root = self.load_dict(word)
        element = self.search_word(word, root)
        self.defitions = self.get_body_variants(element)   

    def load_dict(self,word):
    # TODO: What happens when the word starts with an accent e.g. tre
        script_dir = os.path.dirname(__file__)
        relative_path = "data/{}.xml".format(word[0].lower())
        abs_file_path = os.path.join(script_dir, relative_path)

        with open(abs_file_path) as f:
            root = etree.parse(f)

        return root


    def search_word(self,word, root):
        try:
            return root.xpath("//entree[@terme='{}']".format(word.upper()))[0]
        except IndexError:
            #TODO: How to handle erros
            return ""


    def get_body_variants(self,element):
        variants = element.findall(".//corps/variante")
        texts = []
        for variant in variants:
            text = variant.text
            if text is not None:
                text = text.replace("\n","")
                text = text.replace("\xa0"," ")
                texts.append(text.strip())
        return tuple(texts)