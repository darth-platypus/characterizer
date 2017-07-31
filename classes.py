class Character:
    def __init__(self, first, last, gender, archetype):
        '''Randomize and store all the details of a fictional character.'''

        self.first = first
        self.last = last
        self.gender = gender
        self.archetype = archetype
        self.traits = {
            'Physical': {},
            'Personality': {},
            'Past': {},
            'Occupation': {},
            'Beliefs': {},
            'Conflict': {},
            'Health': {},
        }
        self.fullname = self.first + ' ' + self.last

    def __repr__(self):
        return '{} {} is a {} with these personality traits:\n{}'.format(
            self.first, self.last, self.gender, self.traits)

    def sample_traits(self, archetype):
        '''Sample trait data according to pattern in archetype template.'''
        import random
        for category, trait_dict, count in archetype:
            # Pick x count of random traits from trait_dict.
            selected_traits = random.sample(trait_dict.items(), count)
            # Copy trait key, values to my character.
            self.traits[category].update(selected_traits)

    def format_traits(self, trait_dict):
        '''Format trait keys, values as human-readable strings.'''
        for trait, description in trait_dict.items():
            x = ('{}: {}'.format(trait, description))
            print(x)

    def export_markdown(self):

        def list_traits(x):
            for k, v in self.traits[x].items():
                print('+ ' + '**{}**: {}'.format(k, v))

        # Serialize character sheet output.
        print('# My Character Sheet')
        print('\n' + '## Name')
        print('\n' + '*' + self.fullname + '*')
        print('\n' + '## Gender')
        print('\n' + '*' + self.gender + '*')
        print('\n' + '## Physical Appearance')
        list_traits('Physical')
        print('\n' + '## Personality Traits')
        list_traits('Personality')
        print('\n' + '## Beliefs')
        list_traits('Beliefs')
        print('\n' + '## Past')
        list_traits('Past')
        print('\n' + '## Occupation')
        list_traits('Occupation')
        print('\n' + '## Conflict')
        list_traits('Conflict')
        print('\n' + '## Health')
        list_traits('Health')
