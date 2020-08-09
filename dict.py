from lxml import etree
import os
from dictionary_entry import Dictonary_Entry
# Les données balisées sont toutes placées sous licence Creative Commons Paternité - Partage des conditions initiales à l'identique 3.0, alias CC-BY-SA 3.0. Vous ne pouvez donc les utiliser qu'en indiquent leur source « littre.org » ou en faisant référence à l'auteur du XML « François Gannaz, francois.gannaz@littre.org ».

word = input("Type word to look up: ")
entry = Dictonary_Entry(word)
print(entry.defitions)