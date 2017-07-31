'''
This is a tool to help fiction writers generate ideas for
unique characters. The user inputs the first and last name, gender and
an archetype and a unique character is written to a text file.
'''

import traits
from classes import Character
import archetypes as arch


def characterize(
        first='Jane', last='Doe', gender='Female', archetype=arch.standard):
    '''Generate a fictional character based on user arguments.'''

    my_char = Character(first, last, gender, archetype)  # Create a character.
    my_char.sample_traits(archetype)   # Sample some personality traits.
    my_char.export_markdown()    # Serialize character sheet in Markdown.


characterize('Mysterious', 'Stranger', 'Female', archetype=arch.antagonist)
