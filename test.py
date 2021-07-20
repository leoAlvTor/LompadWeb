from collections import OrderedDict

leo = OrderedDict([('identifier', OrderedDict([('catalog', 'Catalogo1'), ('entry', 'Entrada 1')])), ('title',
    OrderedDict([('string', OrderedDict([('@language', 'es'), ('#text', 'Titutlo del general')]))])), ('language','es'),
    ('description', OrderedDict([('string', OrderedDict([('@language', 'es'), ('#text', 'Descripcion del general.')]))])),
    ('keyword', OrderedDict([('string', [OrderedDict([('@language', 'es'), ('#text', 'Key1')]),
                                         OrderedDict([('@language', 'es'), ('#text', 'Key2')])])])),
                   ('coverage', OrderedDict([('string', OrderedDict([('@language', 'es'), ('#text', 'AmbitoGeneral')]))])),
                   ('structure', OrderedDict([('source', 'LOMv1.0'), ('value', 'atomic')])),
                   ('aggregationLevel', OrderedDict([('source', 'LOMv1.0'), ('value', '2')]))])


print(type(leo['keyword']['string']))
