from collections import OrderedDict

leo = OrderedDict([('@uniqueElementName', 'technical'), ('format', 'NA'), ('size', OrderedDict([('@uniqueElementName',
                                                                                                 'size'),
                                                                                                ('#text', '100mb')])),
                   ('location', 'NA'), ('requirement', OrderedDict([('orComposite',
                                                                     OrderedDict([('type', OrderedDict(
                                                                         [('@uniqueElementName', 'type'), ('source',
                                                                                                           OrderedDict([
                                                                                                                           (
                                                                                                                           '@uniqueElementName',
                                                                                                                           'source'),
                                                                                                                           (
                                                                                                                           '#text',
                                                                                                                           'LOMv1.0')])),
                                                                          ('value', OrderedDict(
                                                                              [('@uniqueElementName', 'value'),
                                                                               ('#text', 'operating system')]))])), (
                                                                                  'name', OrderedDict(
                                                                                      [('@uniqueElementName', 'name'), (
                                                                                      'source', OrderedDict([(
                                                                                                             '@uniqueElementName',
                                                                                                             'source'),
                                                                                                             ('#text',
                                                                                                              'LOMv1.0')])),
                                                                                       ('value', OrderedDict([(
                                                                                                              '@uniqueElementName',
                                                                                                              'value'),
                                                                                                              ('#text',
                                                                                                               'unix')]))])),
                                                                                  ('minimumVersion', OrderedDict([(
                                                                                                                  '@uniqueElementName',
                                                                                                                  'minimumVersion'),
                                                                                                                  (
                                                                                                                  '#text',
                                                                                                                  '1.0')])),
                                                                                  ('maximumVersion', OrderedDict([(
                                                                                                                  '@uniqueElementName',
                                                                                                                  'maximumVersion'),
                                                                                                                  (
                                                                                                                  '#text',
                                                                                                                  '15.0')]))]))])),
                   ('installationRemarks', OrderedDict([('@uniqueElementName', 'installationRemarks'), (
                   'string', OrderedDict([('@language', 'es'), ('#text', 'Cuidado con el perro.')]))])), (
                   'otherPlatformRequirements', OrderedDict([('string', OrderedDict(
                       [('@language', 'es'), ('#text', 'Debe tener al menos 256mb de ram.')]))])), ('duration',
                                                                                                    OrderedDict([(
                                                                                                                 '@uniqueElementName',
                                                                                                                 'duration'),
                                                                                                                 (
                                                                                                                 'duration',
                                                                                                                 OrderedDict(
                                                                                                                     [(
                                                                                                                      '@uniqueElementName',
                                                                                                                      'duration'),
                                                                                                                      (
                                                                                                                      '#text',
                                                                                                                      'P0Y0M0DT1H0M0S')])),
                                                                                                                 (
                                                                                                                 'description',
                                                                                                                 OrderedDict(
                                                                                                                     [(
                                                                                                                      'string',
                                                                                                                      OrderedDict(
                                                                                                                          [
                                                                                                                              (
                                                                                                                              '@language',
                                                                                                                              'es'),
                                                                                                                              (
                                                                                                                              '#text',
                                                                                                                              'No debe tomar mas de una hora.')]))]))]))])



print(leo.get('requirement').get('orComposite').keys())
print('requirement' in leo.keys() and 'orComposite' in leo.get('requirement').keys())
