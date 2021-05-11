# from collections.abc import Iterable
import this
from fuzzywuzzy import fuzz, process


class LOM:

    def __init__(self, general=None, life_cycle=None, meta_metadata=None, technical=None, educational=None, rights=None,
                 relation=None, annotation=None, classification=None):
        self.general = general
        self.life_cycle = life_cycle
        self.meta_metadata = meta_metadata
        self.technical = technical
        self.educational = educational
        self.rights = rights
        self.relation = relation
        self.annotation = annotation
        self.classification = classification

    class General:
        identifier = None
        title = None
        language = None
        description = None
        keyword = None
        coverage = None
        structure = None
        aggregation_level = None

        def __init__(self, identifier=None, title='', language='', description='', keyword='', coverage='',
                     structure='', aggregation_level=''):
            self.identifier = identifier
            self.title = title
            self.language = language
            self.description = description
            self.keyword = keyword
            self.coverage = coverage
            self.structure = structure
            self.aggregation_level = aggregation_level

        class Identifier:
            catalog = None
            entry = None

            def __init__(self, catalog='', entry=''):
                self.catalog = catalog
                self.entry = entry

            def __dict__(self):
                return {'Catalog': self.catalog, 'Entry': self.entry}

        def __dict__(self):
            return {'Identifier': self.identifier.__dict__() if self.identifier is not None else None,
                    'Title': self.title, 'Language': self.language,
                    'Description': self.description, 'Keyword': self.keyword, 'Coverage': self.coverage,
                    'Structure': self.structure, 'Aggregation Level': self.aggregation_level}

    class LifeCycle:
        version = None
        status = None
        contribute = None

        def __init__(self, version='', status='', contribute=None):
            self.version = version
            self.status = status
            self.contribute = contribute

        class Contribute:
            role = None
            entity = None
            date = None

            def __init__(self, role='', entity='', date=''):
                self.role = role
                self.entity = entity
                self.date = date

            def __dict__(self):
                return {'Role': self.role, 'Entity': self.entity, 'Date': self.date}

        def __dict__(self):
            return {'Version': self.version, 'Status': self.status,
                    'Contribute': self.contribute.__dict__() if self.contribute is not None else None}

    class MetaMetadata:
        identifier = None
        contribute = None
        metadata_schema = None
        language = None

        def __init__(self, identifier=None, contribute=None, metadata_schema='', language=''):
            self.identifier = identifier
            self.contribute = contribute
            self.metadata_schema = metadata_schema
            self.language = language

        class Identifier:
            catalog = None
            schema = None

            def __init__(self, catalog='', schema=''):
                self.catalog = catalog
                self.schema = schema

            def __dict__(self):
                return {'Catalog': self.catalog, 'Schema': self.schema}

        class Contribute:
            role = None
            entity = None
            date = None

            def __init__(self, role='', entity='', date=''):
                self.role = role
                self.entity = entity
                self.date = date

            def __dict__(self):
                return {'Role': self.role, 'Entity': self.entity, 'Date': self.date}

        def __dict__(self):
            return {'Identifier': self.identifier.__dict__() if self.identifier is not None else None,
                    'Contribute': self.contribute.__dict__() if self.contribute is not None else None,
                    'Metadata Schema': self.metadata_schema, 'Language': self.language}

    class Technical:
        format = None
        size = None,
        location = None
        requirement = None
        installation_remarks = None
        other_platform_requirements = None
        duration = None

        def __init__(self, technical_format='', size='', location='', requirement=None, installation_remarks='',
                     other_platform_requirements='',
                     duration=''):
            self.format = technical_format
            self.size = size,
            self.location = location
            self.requirement = requirement
            self.installation_remarks = installation_remarks
            self.other_platform_requirements = other_platform_requirements
            self.duration = duration

        class Requirement:
            or_composite = None

            def __init__(self, or_composite=None):
                self.or_composite = or_composite

            class OrComposite:
                composite_type = None
                name = None
                minimum_version = None
                maximum_version = None

                def __init__(self, composite_type='', name='', minimum_version='', maximum_version=''):
                    self.composite_type = composite_type
                    self.name = name
                    self.minimum_version = minimum_version
                    self.maximum_version = maximum_version

                def __dict__(self):
                    return {'Type': self.composite_type, 'Name': self.name, 'Minimum Version': self.minimum_version,
                            'Maximum Version': self.maximum_version}

            def __dict__(self):
                return {'OrComposite': self.or_composite.__dict__() if self.or_composite is not None else None}

        def __dict__(self):
            return {'Format': self.format, 'Size': self.size, 'Location': self.location,
                    'Requirement': self.requirement, 'Installation Remarks': self.installation_remarks,
                    'Other Platform Requirements': self.other_platform_requirements, 'Duration': self.duration}

    class Educational:
        interactivity_type = None
        learning_resource_type = None
        interactivity_level = None
        semantic_density = None
        intended_end_user_role = None
        context = None
        typical_age_range = None
        difficulty = None
        typical_learning_time = None
        description = None
        language = None

        def __init__(self, interactivity_type='', learning_resource_type='', interactivity_level='',
                     semantic_density='', intended_end_user_role='', context='', typical_age_range='', difficulty='',
                     typical_learning_time='', description='', language=''):
            self.interactivity_type = interactivity_type
            self.learning_resource_type = learning_resource_type
            self.interactivity_level = interactivity_level
            self.semantic_density = semantic_density
            self.intended_end_user_role = intended_end_user_role
            self.context = context
            self.typical_age_range = typical_age_range
            self.difficulty = difficulty
            self.typical_learning_time = typical_learning_time
            self.description = description
            self.language = language

        def __dict__(self):
            return {'Interactivity Type': self.interactivity_type,
                    'Learning Resource Type': self.learning_resource_type,
                    'Interactivity Level': self.interactivity_level, 'Semantic Density': self.semantic_density,
                    'Intended End User Roles': self.intended_end_user_role, 'Context': self.context,
                    'Typical Age Range': self.typical_age_range, 'Difficulty': self.difficulty,
                    'Typical Learning Time': self.typical_learning_time, 'Description': self.description, 'Language':
                        self.language}

    class Rights:
        cost = None
        copyright = None
        description = None

        def __init__(self, cost='', copyright_and_other_restrictions='', description=''):
            self.cost = cost
            self.copyright = copyright_and_other_restrictions
            self.description = description

        def __dict__(self):
            return {'Cost': self.cost, 'Copyright and Other Restrictions': self.copyright,
                    'Description': self.description}

    class Relation:
        kind = None
        resource = None

        def __init__(self, kind='', resource=None):
            self.kind = kind
            self.resource = resource

        class Resource:
            description = None
            identifier = None

            def __init__(self, identifier=None, description=''):
                self.description = description
                self.identifier = identifier

            class Identifier:
                catalog = None
                entry = None

                def __init__(self, catalog='', entry=''):
                    self.catalog = catalog
                    self.entry = entry

                def __dict__(self):
                    return {'Catalog': self.catalog, 'Entry': self.entry}

            def __dict__(self):
                return {'Identifier': self.identifier.__dict__() if self.identifier is not None else None,
                        'Description': self.description}

        def __dict__(self):
            return {'Kind': self.kind, 'Resource': self.resource.__dict__() if self.resource is not None else None}

    class Annotation:
        entity = None
        date = None
        description = None

        def __init__(self, entity='', date='', description=''):
            self.entity = entity
            self.date = date
            self.description = description

        def __dict__(self):
            return {'Entity': self.entity, 'Date': self.date, 'Description': self.description}

    class Classification:
        purpose = None  # purpose
        taxon_path = None  # taxon_path
        description = None  # description
        keyword = None  # keyword

        def __init__(self, purpose='', taxon_path=None, description='', keyword=''):
            self.purpose = purpose
            self.taxon_path = taxon_path
            self.description = description
            self.keyword = keyword

        class TaxonPath:
            source = None
            taxon = None

            def __init__(self, source='', taxon=None):
                self.source = source
                self.taxon = taxon

            class Taxon:
                taxon_id = None
                entry = None
                
                def __init__(self, taxon_id='', entry=''):
                    self.taxon_id = taxon_id
                    self.entry = entry

                def __dict__(self):
                    return {'Id': self.taxon_id, 'Entry': self.entry}

            def __dict__(self):
                return {'Source': self.source, 'Taxon': self.taxon.__dict__() if self.taxon is not None else None}

        def __dict__(self):
            return {'Purpose': self.purpose, 'Taxon Path': self.taxon_path.__dict__() if self.taxon_path is not None
                else None, 'Description': self.description, 'Keyword': self.keyword}

    def __dict__(self):
        return {'General': self.general.__dict__() if self.general is not None else None,
                'Life Cycle': self.life_cycle.__dict__() if self.life_cycle is not None else None,
                'Meta-Metadata': self.meta_metadata.__dict__() if self.meta_metadata is not None else None,
                'Technical': self.technical.__dict__() if self.technical is not None else None,
                'Educational': self.educational.__dict__() if self.educational is not None else None,
                'Rights': self.rights.__dict__() if self.rights is not None else None,
                'Relation': self.relation.__dict__() if self.relation is not None else None,
                'Annotation': self.annotation.__dict__() if self.annotation is not None else None,
                'Classification': self.classification.__dict__() if self.classification is not None else None}


function_dict = None


def determine_lopad_leaf(dictionary: dict, key):
    metodo = dispatch[key]
    metodo(dictionary)
    ...


def map_attributes(data: dict, object_instance):
    if data is not None:
        attributes = object_instance.__dir__()
        for key, value in data.items():
            attribute_matched = process.extractOne(key.replace('lomes:', ''), attributes, scorer=fuzz.partial_ratio)[0]
            if type(object_instance.__getattribute__(attribute_matched)) is str:
                object_instance.__setattr__(attribute_matched, value)
    return object_instance


def general_leaf(data: dict):
    general_object = map_attributes(data, LOM.General())
    general_object.identifier = map_attributes(data.get('lomes:identifier')[0], LOM.General.Identifier())
    print(general_object.__dict__())


def life_cycle_leaf(data: dict):
    life_cycle_object = map_attributes(data, LOM.LifeCycle())
    life_cycle_object.contribute = map_attributes(data.get('lomes:contribute')[0], LOM.LifeCycle.Contribute())
    print(life_cycle_object.__dict__())


def meta_metadata_leaf(data: dict):
    meta_metadata_object = map_attributes(data, LOM.MetaMetadata())
    meta_metadata_object.identifier = map_attributes(data.get('lomes:identifier'), LOM.MetaMetadata.Identifier())
    meta_metadata_object.contribute = map_attributes(data.get('lomes:contribute'), LOM.MetaMetadata.Contribute())
    print(meta_metadata_object.__dict__())


def technical_leaf(data: dict):
    # technical_object = map_attributes(data, LOM.Technical())
    # or_composite = map_attributes(data[''])
    # print('Hello from technical: ', data)
    ...


def educational_leaf(data: dict):
    educational_object = map_attributes(data, LOM.Educational())
    print('Educational: ', educational_object.__dict__())
    # print('Hello from educational: ', data)
    ...


def rights_leaf(data: dict):
    rights_object = map_attributes(data, LOM.Rights())
    print('Rights:', rights_object.__dict__())
    # print('Hello from rights: ', data)
    ...


def relation_leaf(data: dict):
    relation_object = map_attributes(data, LOM.Relation())
    resource_object = map_attributes(data.get('lomes:resource'), LOM.Relation.Resource())
    identifier_object = map_attributes(data.get('lomes:resource').get('lomes:identifier'),
                                       LOM.Relation.Resource.Identifier())
    relation_object.identifier = identifier_object
    relation_object = resource_object
    print('Relation: ', relation_object.__dict__())
    # print('Hello from relation: ', data)
    ...


def annotation_leaf(data: dict):
    # print('Hello from annotation: ', data)
    ...


def classification_leaf(data: dict):
    # print('Hello from classification: ', data)
    ...


dispatch = {
    'lomes:general': general_leaf, 'lomes:lifeCycle': life_cycle_leaf, 'lomes:metaMetadata': meta_metadata_leaf,
    'lomes:technical': technical_leaf, 'lomes:educational': educational_leaf,
    'lomes:rights': rights_leaf, 'lomes:relation': relation_leaf, 'lomes:annotation': annotation_leaf,
    'lomes:classification': classification_leaf
}