from lxml import etree
import os

# Les données balisées sont toutes placées sous licence Creative Commons Paternité - Partage des conditions initiales à l'identique 3.0, alias CC-BY-SA 3.0. Vous ne pouvez donc les utiliser qu'en indiquent leur source « littre.org » ou en faisant référence à l'auteur du XML « François Gannaz, francois.gannaz@littre.org ».


def load_dict(word):
    # TODO: What happens when the word starts with an accent e.g. être
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    relative_path = "data/{}.xml".format(word[0].lower())
    abs_file_path = os.path.join(script_dir, relative_path)

    with open(abs_file_path) as f:
        root = etree.parse(f)

    return root


def search_word(word, root):
    try:
        return root.xpath("//entree[@terme='{}']".format(word.upper()))[0]
    except IndexError:
        print("Word not found")


def create_readable_string(element):
    # TODO: print useful info
    #
    # <entete>
    #     <prononciation>è-m'</prononciation>
    #     <nature>s. f.</nature>
    # </entete>
    # and
    # coprs or variante
    return(etree.tostring(element, pretty_print=True))


word = input("Type word to look up: ")
root = load_dict(word)
element = search_word(word, root)
readable_string = create_readable_string(element)
print(readable_string)
