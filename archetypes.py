'''
Templates for archetypes. Feel free to create your own! Use the example
archetype below to help get you started.
'''

import traits


standard = [    # Average Joe/Jane
    ['Physical', traits.matrix['Physical']['Body'], 1],
    ['Personality', traits.matrix['Personality']['Humor']['Playful'], 1],
    ['Personality', traits.matrix['Personality']['Flaws']['Common'], 2],
    ['Personality', traits.matrix['Personality']['Quirks'], 2],
    ['Personality', traits.matrix['Personality']['Fears']['Common'], 2],
    ['Beliefs', traits.matrix['Beliefs']['Faith'], 1],
    ['Past', traits.matrix['Past']['Wounds']['Fresh'], 1],
    ['Past', traits.matrix['Past']['Wounds']['Old'], 2],
    ['Past', traits.matrix['Past']['Secrets']['Common'], 1],
    ['Past', traits.matrix['Past']['Secrets']['Dark'], 1],
    ['Past', traits.matrix['Past']['Education'], 1],
    ['Past', traits.matrix['Past']['Relationships']['Standard'], 1],
    ['Past', traits.matrix['Past']['Child Status'], 1],
    ['Occupation', traits.matrix['Occupation']['Skilled'], 1],
    ['Conflict', traits.matrix['Conflict']['Recent Troubles'], 1],
    ['Health', traits.matrix['Health']['Mental']['Common'], 1]
]

antagonist = [    # Average Joe/Jane
    ['Physical', traits.matrix['Physical']['Body'], 1],
    ['Personality', traits.matrix['Personality']['Humor']['Offbeat'], 1],
    ['Personality', traits.matrix['Personality']['Flaws']['Common'], 2],
    ['Personality', traits.matrix['Personality']['Flaws']['Self-destructive'], 1],
    ['Personality', traits.matrix['Personality']['Flaws']['Unlikable'], 1],
    ['Personality', traits.matrix['Personality']['Quirks'], 2],
    ['Personality', traits.matrix['Personality']['Fears']['Common'], 2],
    ['Personality', traits.matrix['Personality']['Fears']['Phobias'], 1],
    ['Beliefs', traits.matrix['Beliefs']['Faith'], 1],
    ['Past', traits.matrix['Past']['Wounds']['Fresh'], 1],
    ['Past', traits.matrix['Past']['Wounds']['Old'], 4],
    ['Past', traits.matrix['Past']['Secrets']['Common'], 2],
    ['Past', traits.matrix['Past']['Secrets']['Dark'], 2],
    ['Past', traits.matrix['Past']['Education'], 1],
    ['Past', traits.matrix['Past']['Relationships']['Dysfunctional'], 1],
    ['Past', traits.matrix['Past']['Child Status'], 1],
    ['Occupation', traits.matrix['Occupation']['Uncommon'], 1],
    ['Conflict', traits.matrix['Conflict']['Recent Troubles'], 2],
    ['Health', traits.matrix['Health']['Mental']['Common'], 1],
    ['Health', traits.matrix['Health']['Mental']['Serious'], 1]
]
