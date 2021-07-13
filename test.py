from collections import OrderedDict

leo = OrderedDict([('@uniqueElementName', 'typicalLearningTime'), ('duration', OrderedDict([('@uniqueElementName', 'duration'), ('#text', 'P0Y0M0DT1H0M0S')])), ('description', OrderedDict([('string', OrderedDict([('@language', 'es'), ('#text', 'No toma mas de una hora.')]))]))])
print(leo['description']['string']['#text'])

print('description' in leo.keys() and 'string' in leo['description'].keys() and '#text' in leo['description']['string'])
