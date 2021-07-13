from collections import OrderedDict

leo = OrderedDict([('@uniqueElementName', 'date'), ('dateTime', OrderedDict([('@uniqueElementName', 'dateTime'),
    ('#text', '2021-05-17T15:40:32.00-05:00')])), ('description', OrderedDict([('string',
    OrderedDict([('@language', 'es'), ('#text', 'Ninguna fecha')]))]))])

print(type(leo))

print(leo['dateTime']['#text'])