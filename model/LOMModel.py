import logging
import traceback
from collections import OrderedDict
from pprint import pprint
from fuzzywuzzy import fuzz, process


class LOM:

    def __init__(self, general=None, life_cycle=None, meta_metadata=None, technical=None, educational=None, rights=None,
                 relation=None, annotation=None, classification=None, accessibility=None):
        logging.basicConfig(filename='logger.log')
        self.general = general
        self.lifeCycle = life_cycle
        self.metaMetadata = meta_metadata
        self.technical = technical
        self.educational = educational
        self.rights = rights
        self.relation = relation
        self.annotation = annotation
        self.classification = classification
        self.accesibility = accessibility

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

            def to_xml(self):
                return f"""<identifier>
                <catalog>{self.catalog}</catalog>
                <entry>{self.entry}</entry>
                </identifier>"""

            def __dict__(self):
                return {'Catalog': self.catalog, 'Entry': self.entry}

        def get_keyword(self):
            if type(self.keyword) is list:
                elements = []
                for element in self.keyword:
                    elements.append(f'{element},')
                return elements
            else:
                return self.keyword

        def get_xml_keywords(self):
            if type(self.keyword) is list:
                content = ""
                for key in self.keyword:
                    content += f"""<string language="en">{key}</string>\n"""
                return content
            else:
                return self.keyword

        def to_xml(self):
            return f"""<general>
                {self.identifier.to_xml() if self.identifier is not None else ''}
                <title>
                <string language="{self.language}">{self.title}</string>
                </title>
                <language>{self.language}</language>
                <description>
                <string language="{self.language}">{self.description}</string>
                </description>
                <keyword>
                {self.get_xml_keywords()}
                </keyword>
                <coverage>
                <string language="{self.language}">{self.coverage}</string>
                </coverage>
                <structure>
                <source>LOMv1.0</source>
                <value>{self.structure}</value>
                </structure>
                <aggregationLevel>
                <source>LOMv1.0</source>
                <value>{self.aggregation_level}</value>
                </aggregationLevel>
            </general>"""

        def __dict__(self):
            return {'Identifier': self.identifier.__dict__() if self.identifier is not None else '',
                    'Title': self.title, 'Language': self.language,
                    'Description': self.description, 'Keyword': self.get_keyword(), 'Coverage': self.coverage,
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

            def to_xml(self):
                return f"""<contribute>
                <role>
                <source>LOMv1.0</source>
                <value>{self.role}</value>
                </role>
                <entity><![CDATA[{self.entity}]]></entity>
                <date>
                <dateTime>{self.date}</dateTime>
                <description>
                <string language="en">EMPTY</string>
                </description>
                </date>
                </contribute>"""

        def __dict__(self):
            return {'Version': self.version, 'Status': self.status,
                    'Contribute': self.contribute.__dict__() if self.contribute is not None else self.Contribute().__dict__()}

        def to_xml(self):
            return f"""<lifeCycle>
                <version><string language="en">{self.version}</string></version>
                <status>
                <source>LOMv1.0</source>
                <value>{self.status}</value>
                </status>
                {self.contribute.to_xml() if self.contribute is not None else ''}
            </lifeCycle>"""

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
            entry = None

            def __init__(self, catalog='', entry=''):
                self.catalog = catalog
                self.entry = entry

            def to_xml(self):
                return f"""<identifier>
                <catalog>{self.catalog}</catalog>
                <entry>{self.entry}</entry>
                </identifier>"""

            def __dict__(self):
                return {'Catalog': self.catalog, 'Schema': self.entry}

        class Contribute:
            role = None
            entity = None
            date = None

            def __init__(self, role='', entity='', date=''):
                self.role = role
                self.entity = entity
                self.date = date

            def to_xml(self):
                return f"""<contribute>
                <role>
                <source>LOMv1.0</source>
                <value>{self.role}</value>
                </role>
                <entity>
                <![CDATA[{self.entity}]]>
                </entity>
                <date>
                <dateTime>{self.date}</dateTime>
                <description>
                <string language="en">EMPTY</string>
                </description>
                </date>
                </contribute>"""

            def __dict__(self):
                return {'Role': self.role, 'Entity': self.entity, 'Date': self.date}

        def to_xml(self):
            return f"""<metaMetadata>
            {self.identifier.to_xml() if self.identifier is not None else ''}
            {self.contribute.to_xml() if self.contribute is not None else ''}
            <metadataSchema>{self.metadata_schema}</metadataSchema>
            <language>{self.language}</language>
            </metaMetadata>"""

        def __dict__(self):
            return {
                'Identifier': self.identifier.__dict__() if self.identifier is not None else self.Identifier().__dict__(),
                'Contribute': self.contribute.__dict__() if self.contribute is not None else self.Contribute().__dict__(),
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
                     other_platform_requirements='', duration=''):
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

                def to_xml(self):
                    return f"""<orComposite>
                    <type>
                    <source>LOMv1.0</source>
                    <value>{self.composite_type}</value>
                    </type>
                    <name>
                    <source>LOMv1.0></source>
                    <value>{self.name}</value>
                    </name>
                    <minimumVersion>{self.minimum_version}</minimumVersion>
                    <maximumVersion>{self.maximum_version}</maximumVersion>
                    </orComposite>"""

                def __dict__(self):
                    return {'Type': self.composite_type, 'Name': self.name, 'Minimum Version': self.minimum_version,
                            'Maximum Version': self.maximum_version}

            def to_xml(self):
                return f"""<requirement>
                {self.or_composite.to_xml() if self.or_composite is not None else ''}
                </requirement>"""

            def __dict__(self):
                return {
                    'OrComposite': self.or_composite.__dict__() if self.or_composite is not None
                    else self.OrComposite().__dict__()}

        def to_xml(self):
            return f"""<technical>
            <format>{self.format}</format>
            <size>{self.size}</size>
            <location>{self.location}</location>
            {self.requirement.to_xml() if self.requirement is not None else ''}
            <installationRemarks>
            <string language="en">{self.installation_remarks}</string>
            </installationRemarks>
            <otherPlatformRequirements>
            <string language="en">{self.other_platform_requirements}</string>
            </otherPlatformRequirements>
            <duration>
                <duration>{self.duration}</duration>
                <description>
                    <string language="">EMPTY</string>
                </description>
            </duration>
            </technical>"""

        def __dict__(self):
            return {'Format': self.format, 'Size': self.size, 'Location': self.location,
                    'Requirement': self.requirement.__dict__() if self.requirement is not None else self.Requirement().__dict__(),
                    'Installation Remarks': self.installation_remarks,
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

        def to_xml(self):
            return f"""<educational>
            <interactivityType>
            <source>LOMv1.0</source>
            <value>{self.interactivity_type}</value>
            </interactivityType>
            <learningResourceType>
            <source>LOMv1.0</source>
            <value>{self.learning_resource_type}</value>
            </learningResourceType>
            <interactivityLevel>
            <source>LOMv1.0</source>
            <value>{self.interactivity_level}</value>
            </interactivityLevel>
            <semanticDensity>
            <source>LOMv1.0</source>
            <value>{self.semantic_density}</value>
            </semanticDensity>
            <intendedEndUserRole>
            <source>LOMv1.0</source>
            <value>{self.intended_end_user_role}</value>
            </intendedEndUserRole>
            <context>
            <source>LOMv1.0</source>
            <value>{self.context}</value>
            </context>
            <typicalAgeRange>
            <string language="en">{self.typical_age_range}</string>
            </typicalAgeRange>
            <difficulty>
            <source>LOMv1.0</source>
            <value>{self.difficulty}</value>
            </difficulty>
            <typicalLearningTime>
            <duration>{self.typical_learning_time}</duration>
            <description>
            <string language="en">{self.description}</string>
            </description>
            </typicalLearningTime>
            <description>
            <string language="en">{self.description}</string>
            </description>
            <language>{self.language}</language>
            </educational>"""

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

        def to_xml(self):
            return f"""<rights>
            <cost>
            <source>LOMv1.0</source>
            <value>{self.cost}</value>
            </cost>
            <copyrightAndOtherRestrictions>
            <source>LOMv1.0</source>
            <value>{self.copyright}</value>
            </copyrightAndOtherRestrictions>
            <description>
            <string language="en">{self.description}</string>
            </description>
            </rights>"""

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

                def to_xml(self):
                    return f"""<identifier>
                    <catalog>{self.catalog}</catalog>
                    <entry>{self.entry}</entry>
                    </identifier>"""

            def to_xml(self):
                return f"""<resource>
                {self.identifier.to_xml() if self.identifier is not None else ''}
                <description>
                <string language="en">{self.description}</string>
                </description>
                </resource>"""

            def __dict__(self):
                return {'Identifier': self.identifier.__dict__() if self.identifier is not None
                else self.Identifier().__dict__(),
                        'Description': self.description}

        def to_xml(self):
            return f"""<relation>
            <kind>
            <source>LOMv1.0</source>
            <value>{self.kind}</value>
            </kind>
            {self.resource.to_xml() if self.resource is not None else ''}
            </relation>"""

        def __dict__(self):
            return {'Kind': self.kind, 'Resource': self.resource.__dict__() if self.resource is not None
            else self.Resource().__dict__()}

    class Annotation:
        entity = None
        date = None
        description = None
        mode_access = None
        mode_access_sufficient = None
        rol = None

        def __init__(self, entity='', date='', description='', mode_access='', mode_access_sufficient='', rol=''):
            self.entity = entity
            self.date = date
            self.description = description
            self.mode_access = mode_access
            self.mode_access_sufficient = mode_access_sufficient
            self.rol = rol

        def to_xml(self):
            return f"""<annotation>
            <entity>
            <![CDATA[{self.entity}]]>
            </entity>
            <date>
            <dateTime>{self.date}</dateTime>
            <description>
            <string></string>
            </description>
            </date>
            <description>
            <string>{self.description}</string>
            </description>
            <modeaccess>
            <source>LOMv1.0</source>
            <value>{self.mode_access}</value>
            </modeaccess>
            <modeaccesssufficient>
            <source>LOMv1.0</source>
            <value>{self.mode_access_sufficient}</value>
            </modeaccesssufficient>
            <Rol>
            <source>LOMv1.0</source>
            <value>{self.rol}</value>
            </Rol>
            </annotation>"""

        def __dict__(self):
            return {'Entity': self.entity, 'Date': self.date, 'Description': self.description,
                    'Mode Access': self.mode_access, 'Mode Access Sufficient': self.mode_access_sufficient,
                    'Rol': self.rol}

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

                def to_xml(self):
                    return f"""<taxon>
                    <id>{self.taxon_id}</id>
                    <entry>
                    <string language="en">{self.entry}</string>
                    </entry>
                    </taxon>"""

            def to_xml(self):
                return f"""<taxonPath>
                <source>
                <string language="en">{self.source}</string>
                </source>
                {self.taxon.to_xml() if self.taxon is not None else ''}
                </taxonPath>"""

            def __dict__(self):
                return {'Source': self.source, 'Taxon': self.taxon.__dict__() if self.taxon is not None
                else self.Taxon().__dict__()}

        def to_xml(self):
            return f"""<classification>
            <purpose>
            <source>LOMv1.0</source>
            <value>{self.purpose}</value>
            </purpose>
            {self.taxon_path.to_xml() if self.taxon_path is not None else ''}
            <description>
            <string language="en">{self.description}</string>
            </description>
            <keyword>
            <string language="en">{self.keyword}</string>
            </keyword>
            </classification>"""

        def __dict__(self):
            return {'Purpose': self.purpose, 'Taxon Path': self.taxon_path.__dict__() if self.taxon_path is not None
            else self.TaxonPath().__dict__(), 'Description': self.description, 'Keyword': self.keyword}

    class Accessibility:

        description = None
        accessibility_features = None
        accessibility_hazard = None
        accessibility_control = None
        accessibility_api = None

        def __init__(self, description='', accesibility_features=None, accessibility_hazard=None,
                     accessibility_control=None, accessibility_api=None):
            self.description = description
            self.accessibility_features = accesibility_features
            self.accessibility_hazard = accessibility_hazard
            self.accessibility_control = accessibility_control
            self.accessibility_api = accessibility_api

        class AccessibilityFeatures:
            resource_content = None

            def __init__(self, resource_content=''):
                self.resource_content = resource_content

            def __dict__(self):
                return {'Resource Content': self.resource_content}

            def get_resource_content(self):
                content = ""
                if type(self.resource_content) is OrderedDict and type(self.resource_content.get('br')) is list:
                    for resource in self.resource_content.get('br'):
                        content += f"<br>{resource}</br>\n"
                    return content
                else:
                    return self.resource_content.get('br')

            def to_xml(self):
                return f"""<accessibilityfeatures>
                <resourcecontent>
                {self.get_resource_content()}
                </resourcecontent>
                </accessibilityfeatures>"""

        class AccessibilityHazard:
            properties = None

            def __init__(self, properties=''):
                self.properties = properties

            def __dict__(self):
                return {'Properties': self.properties}

            def get_properties(self):
                content = ""
                if type(self.properties) is OrderedDict and type(self.properties.get('br')) is list:
                    for resource in self.properties.get('br'):
                        content += f"<br>{resource}</br>\n"
                    return content
                else:
                    return self.properties.get('br')

            def to_xml(self):
                return f"""<accessibilityhazard>
                <properties>
                {self.get_properties()}
                </properties>
                </accessibilityhazard>"""

        class AccessibilityControl:
            methods = None

            def __init__(self, methods=''):
                self.methods = methods

            def __dict__(self):
                return {'Methods': self.methods}

            def get_methods(self):
                content = ""
                if type(self.methods) is OrderedDict and type(self.methods.get('br')) is list:
                    for resource in self.methods.get('br'):
                        content += f"<br>{resource}</br>\n"
                    return content
                else:
                    return self.methods.get('br')

            def to_xml(self):
                return f"""<accessibilitycontrol>
                <methods>
                {self.get_methods()}
                </methods>
                </accessibilitycontrol>"""

        class AccessibilityAPI:
            compatible_resource = None

            def __init__(self, compatible_resource=''):
                self.compatible_resource = compatible_resource

            def __dict__(self):
                return {'Compatible Resource': self.compatible_resource}

            def get_compatible_resources(self):
                content = ""
                if type(self.compatible_resource) is OrderedDict and type(self.compatible_resource.get('br')) is list:
                    for resource in self.compatible_resource.get('br'):
                        content += f"<br>{resource}</br>\n"
                    return content
                else:
                    return self.compatible_resource.get('br')

            def to_xml(self):
                return f"""<accessibilityAPI>
                <compatibleresource>
                {self.get_compatible_resources()}
                </compatibleresource>
                </accessibilityAPI>"""

        def to_xml(self):
            return f"""<accesibility>
            <description><string language="en">{self.description}</string></description>
            {self.accessibility_features.to_xml() if self.accessibility_features is not None else ''}
            {self.accessibility_hazard.to_xml() if self.accessibility_hazard is not None else ''}
            {self.accessibility_control.to_xml() if self.accessibility_control is not None else ''}
            {self.accessibility_api.to_xml() if self.accessibility_api is not None else ''}
            </accesibility>"""

        def __dict__(self):
            return {'Description': self.description, 'Accessibility Features': self.accessibility_features.__dict__()
                    if self.accessibility_features is not None else self.AccessibilityFeatures().__dict__(),
                    'Accessibility Hazard': self.accessibility_hazard.__dict__() if self.accessibility_hazard is not None
                    else self.AccessibilityHazard().__dict__(),
                    'Accessibility Control': self.accessibility_control.__dict__() if self.accessibility_control is not None
                    else self.AccessibilityControl().__dict__(),
                    'Accessibility API': self.accessibility_api.__dict__() if self.accessibility_api is not None
                    else self.AccessibilityAPI().__dict__()}

    def to_xml(self):
        return f"""
        <?xml version="1.0" encoding="UTF-8"?>
        <lom xmlns="http://ltsc.ieee.org/xsd/LOM" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://ltsc.ieee.org/xsd/LOM http://ltsc.ieee.org/xsd/lomv1.0/lom.xsd">
            {self.general.to_xml() if self.general is not None else ''}
            {self.lifeCycle.to_xml() if self.lifeCycle is not None else ''}
            {self.metaMetadata.to_xml() if self.metaMetadata is not None else ''}
            {self.technical.to_xml() if self.technical is not None else ''}
            {self.educational.to_xml() if self.educational is not None else ''}
            {self.rights.to_xml() if self.rights is not None else ''}
            {self.relation.to_xml() if self.relation is not None else ''}
            {self.annotation.to_xml() if self.annotation is not None else ''}
            {self.classification.to_xml() if self.classification is not None else ''}
            {self.accesibility.to_xml() if self.accesibility is not None else ''}
        </lom>
        """

    def __dict__(self):
        return {'General': self.general.__dict__() if self.general is not None else self.General().__dict__(),
                'Life Cycle': self.lifeCycle.__dict__() if self.lifeCycle is not None else self.LifeCycle().__dict__(),
                'Meta-Metadata': self.metaMetadata.__dict__() if self.metaMetadata is not None else self.MetaMetadata().__dict__(),
                'Technical': self.technical.__dict__() if self.technical is not None else self.Technical().__dict__(),
                'Educational': self.educational.__dict__() if self.educational is not None else self.Educational().__dict__(),
                'Rights': self.rights.__dict__() if self.rights is not None else self.Rights().__dict__(),
                'Relation': self.relation.__dict__() if self.relation is not None else self.Relation().__dict__(),
                'Annotation': self.annotation.__dict__() if self.annotation is not None else self.Annotation().__dict__(),
                'Classification': self.classification.__dict__() if self.classification is not None else self.Classification().__dict__(),
                'Accessibility': self.accesibility.__dict__() if self.accesibility is not None else self.Accessibility().__dict__()}


def determine_lompad_leaf(dictionary: dict, key: str, is_lompad_exported=False):
    """
    Determine which lompad leaf should be mapped.

    :param dictionary: A Dict instance in representation of data to being parsed.
    :param key: Represents the key of LOM standard.
    :param is_lompad_exported: Check if manifest comes from lompad application.

    :return: a dict representing the object mapped.
    :except If key was not found or couldn't invoke a function (by reflection) catch an exception and prints its
    traceback.
    """
    try:
        # Search the key inside dispatch dict.
        for key1 in dispatch.keys():
            if key in key1:
                metodo = dispatch[key1]
                return metodo(dictionary, is_lompad_exported)
    except KeyError as ke:
        logging.error(f' Unexpected key {key}, ignoring key, error {ke}')
    except Exception as ex:
        logging.error(f' Error: {ex}')
        print(traceback.format_exc())


def get_keywords(object_data: list):
    """
    Special case function.
    The can be many keywords inside general leaf, so this function get its value and stores it inside a list.

    :param object_data: List of OrderedDict.
    :return: extracted values.
    """
    values = []
    for value in object_data:
        if type(value) is OrderedDict and 'string' in value.keys() and '#text' in value['string'].keys():
            values.append(value['string']['#text'])
        elif type(value) is OrderedDict and '#text' in value.keys():
            values.append(value['#text'])
    return values


def map_attributes(data_original: dict, object_instance, is_lom):
    data = data_original.copy()

    for key in data_original.keys():
        data[str(key).replace('lom:', '')] = data.pop(key)

    """
    What a nice function, isn't it? (Just kidding).

    Extracts meaningful information from dict nodes and stores inside an object instance, inside nodes can be different
    types of information:
    - String
    - Date (as string)

    There are different ways that ExeLearning saves a string that's the why of too many ifs.

    :param data: An ordered dict which contains the information to be extracted.
    :param object_instance: An instance of Any LOM leaf class or its subclasses.
    :return: an object containing parsed information.
    """
    if data is not None and not isinstance(data, list):
        attributes = object_instance.__dir__()
        for key, value in data.items():
            # Special cases to extract data because FuzzyWuzzy can be wrong!
            if 'otherPlatformRequirements' == key:
                if type(value) is OrderedDict and 'string' in value.keys() and '#text' in value['string'].keys():
                    object_instance.__setattr__('other_platform_requirements', value['string']['#text'])
            elif 'modeaccess' == key:
                if type(value) is OrderedDict and 'value' in value.keys():
                    object_instance.__setattr__('mode_access', value['value'])
            elif 'modeaccesssufficient' == key:
                if type(value) is OrderedDict and 'value' in value.keys():
                    object_instance.__setattr__('mode_access_sufficient', value['value'])
            elif 'rol' == key:
                if type(value) is OrderedDict and 'value' in value.keys():
                    object_instance.__setattr__('rol', value['value'])
            elif 'size' == key and is_lom:
                object_instance.__setattr__('size', value)
            elif 'size' == key and not is_lom:
                object_instance.__setattr__('size', value['#text'])
            else:
                attribute_matched = process.extractOne(key.replace('lom:', ''), attributes, scorer=fuzz.partial_ratio)[0]

                if not is_lom:
                    if type(object_instance.__getattribute__(attribute_matched)) is str:
                        if type(value) is OrderedDict and '#text' in value.keys():
                            object_instance.__setattr__(attribute_matched, value['#text'])
                        elif type(value) is OrderedDict and 'string' in value.keys() and type(
                                value['string']) is not OrderedDict:
                            object_instance.__setattr__(attribute_matched, value['string'])
                        elif type(value) is OrderedDict and 'string' in value.keys() and '#text' in value['string'].keys():
                            object_instance.__setattr__(attribute_matched, value['string']['#text'])
                        elif type(value) is list:
                            object_instance.__setattr__(attribute_matched, get_keywords(value))
                        elif type(value) is OrderedDict and 'value' in value.keys() and '#text' in value['value'].keys():
                            object_instance.__setattr__(attribute_matched, value['value']['#text'])
                        elif type(value) is OrderedDict and 'dateTime' in value.keys() and '#text' in value[
                            'dateTime'].keys():
                            object_instance.__setattr__(attribute_matched, value['dateTime']['#text'])
                        elif type(value) is OrderedDict and 'description' in value.keys() and 'string' in \
                                value['description'].keys() and '#text' in value['description']['string']:
                            object_instance.__setattr__(attribute_matched, value['description']['string']['#text'])
                        else:
                            object_instance.__setattr__(attribute_matched, value)
                else:
                    if type(object_instance.__getattribute__(attribute_matched)) is str:
                        if type(value) is OrderedDict and 'string' in value.keys() and type(value['string']) is list:
                            object_instance.__setattr__(attribute_matched, get_keywords(value['string']))
                        elif type(value) is OrderedDict and 'string' in value.keys() and type(value['string']) \
                                is OrderedDict and '#text' in value['string'].keys():
                            object_instance.__setattr__(attribute_matched, value['string']['#text'])
                        elif type(value) is OrderedDict and 'value' in value.keys():
                            object_instance.__setattr__(attribute_matched, value['value'])
                        elif type(value) is OrderedDict and 'dateTime' in value.keys():
                            object_instance.__setattr__(attribute_matched, value['dateTime'])
                        elif type(value) is OrderedDict and 'duration' in value.keys():
                            object_instance.__setattr__(attribute_matched, value['duration'])
                        else:
                            object_instance.__setattr__(attribute_matched, value)
    return object_instance


def general_leaf(data: dict, is_lom):
    """
    Function to map General Leaf.

    :param data: data from manifest.
    :return: a General class instance.
    """
    general_object = map_attributes(data, LOM.General(), is_lom)
    if 'lom:identifier' in data.keys():
        general_object.identifier = map_attributes(data.get('lom:identifier'), LOM.General.Identifier(), is_lom)
    elif 'identifier' in data.keys():
        general_object.identifier = map_attributes(data.get('identifier'), LOM.General.Identifier(), is_lom)

    return general_object.__dict__(), general_object


def life_cycle_leaf(data: dict, is_lom):
    """
        Function to map Life Cycle Leaf.

        :param data: data from manifest.
        :return: a LifeCycle class instance.
        """
    life_cycle_object = map_attributes(data, LOM.LifeCycle(), is_lom)
    life_cycle_object.contribute = map_attributes(
        data.get('lom:contribute') if data.get('lom:contribute') is not None
        else data.get('contribute'),
        LOM.LifeCycle.Contribute(), is_lom)
    return life_cycle_object.__dict__(), life_cycle_object


def meta_metadata_leaf(data: dict, is_lom):
    """
        Function to map Meta MetaData Leaf.

        :param data: data from manifest.
        :return: a MetaMetaData class instance.
        """
    meta_metadata_object = map_attributes(data, LOM.MetaMetadata(), is_lom)
    meta_metadata_object.identifier = map_attributes(data.get('lom:identifier') if data.get('lom:identifier')
                                                     is not None else data.get('identifier'),
                                                     LOM.MetaMetadata.Identifier(), is_lom)
    meta_metadata_object.contribute = map_attributes(data.get('lom:contribute')
                                                     if data.get('lom:contribute') is not None
                                                     else data.get('contribute'), LOM.MetaMetadata.Contribute(), is_lom)

    return meta_metadata_object.__dict__(), meta_metadata_object


def technical_leaf(data: dict, is_lom):
    """
        Function to map Technical Leaf.

        :param data: data from manifest.
        :return: a Technical class instance.
        """
    technical_object = map_attributes(data, LOM.Technical(), is_lom)
    orComposite = None
    if 'lom:requirement' in data.keys() and 'lom:OrComposite' in data.get('lom:requirement').keys():
        orComposite = map_attributes(data.get('lom:requirement').get('lom:OrComposite'), LOM.Technical.Requirement
                                     .OrComposite(), is_lom)
    elif 'requirement' in data.keys():
        if data.get('requirement') is not None and 'orComposite' in data.get('requirement').keys():
            orComposite = map_attributes(data.get('requirement').get('orComposite'),
                                     LOM.Technical.Requirement.OrComposite(), is_lom)
        elif data.get('requirement') is not None and 'OrComposite' in data.get('requirement').keys():
            orComposite = map_attributes(data.get('requirement').get('OrComposite'),
                                     LOM.Technical.Requirement.OrComposite(), is_lom)
    technical_object.requirement = technical_object.Requirement(orComposite)

    return technical_object.__dict__(), technical_object


def educational_leaf(data: dict, is_lom):
    """
        Function to map Educational Leaf.

        :param data: data from manifest.
        :return: a Educational class instance.
        """
    educational_object = map_attributes(data, LOM.Educational(), is_lom)

    return educational_object.__dict__(), educational_object


def rights_leaf(data: dict, is_lom):
    """
        Function to map Rights Leaf.

        :param data: data from manifest.
        :return: a Rights class instance.
        """
    rights_object = map_attributes(data, LOM.Rights(), is_lom)

    return rights_object.__dict__(), rights_object


def relation_leaf(data: dict, is_lom):
    """
        Function to map Relation Leaf.

        :param data: data from manifest.
        :return: a Relation class instance.
        """
    relation_object = map_attributes(data, LOM.Relation(), is_lom)
    resource = map_attributes(data['resource'], LOM.Relation.Resource(), is_lom)

    if 'resource' in data.keys():
        if 'identifier' in data['resource'].keys():
            identifier = map_attributes(data['resource']['identifier'], LOM.Relation.Resource.Identifier(), is_lom)
        elif 'Identifier' in data['resource'].keys():
            identifier = map_attributes(data['resource']['Identifier'], LOM.Relation.Resource.Identifier(), is_lom)

    resource.identifier = identifier
    relation_object.resource = resource

    return relation_object.__dict__(), relation_object


def annotation_leaf(data: dict, is_lom):
    """
        Function to map Annotation Leaf.

        :param data: data from manifest.
        :return: a Annotation class instance.
        """
    annotation_object = map_attributes(data, LOM.Annotation(), is_lom)

    return annotation_object.__dict__(), annotation_object


def classification_leaf(data: dict, is_lom):
    """
        Function to map Classification Leaf.

        :param data: data from manifest.
        :return: a Classification class instance.
        """
    classification_object = map_attributes(data, LOM.Classification(), is_lom)

    taxon_path = map_attributes(data.get('lom:taxonPath') if data.get('lom:taxonPath') is not None else
                                data.get('taxonPath'), classification_object.TaxonPath(), is_lom)

    taxon = None
    if data.get('lom:taxonPath') is not None and data.get('lom:taxonPath').get('lom:taxon') is not None:
        taxon = map_attributes(data.get('lom:taxonPath').get('lom:taxon')[0]
                               if type(data.get('lom:taxonPath').get('lom:taxon')) is list else
                               data.get('lom:taxonPath').get('lom:taxon'), classification_object.TaxonPath.Taxon(),
                               is_lom)

    elif data.get('taxonPath') is not None and data.get('taxonPath').get('taxon') is not None:
        taxon = map_attributes(data.get('taxonPath').get('taxon')[0]
                               if type(data.get('taxonPath').get('taxon')) is list else
                               data.get('taxonPath').get('taxon'), classification_object.TaxonPath.Taxon(),
                               is_lom)

    classification_object.taxon_path = taxon_path
    classification_object.taxon_path.taxon = taxon

    return classification_object.__dict__(), classification_object


def accessibility_leaf(data: dict, is_lom):
    accessibility_object = map_attributes(data, LOM.Accessibility(), is_lom)
    api, features, hazard, control = None, None, None, None

    if data.get('accessibilityAPI') is not None:
        api = map_attributes(data.get('accessibilityAPI'), LOM.Accessibility.AccessibilityAPI(), is_lom)
    elif data.get('accessibilityApi') is not None:
        api = map_attributes(data.get('accessibilityApi'), LOM.Accessibility.AccessibilityAPI(), is_lom)

    if data.get('accessibilityfeatures') is not None:
        features = map_attributes(data.get('accessibilityfeatures'), LOM.Accessibility.AccessibilityFeatures(), is_lom)
    elif data.get('accessibilityFeatures') is not None:
        features = map_attributes(data.get('accessibilityFeatures'), LOM.Accessibility.AccessibilityFeatures(), is_lom)

    if data.get('accessibilityhazard') is not None:
        hazard = map_attributes(data.get('accessibilityhazard'), LOM.Accessibility.AccessibilityHazard(), is_lom)
    elif data.get('accessibilityHazard') is not None:
        hazard = map_attributes(data.get('accessibilityHazard'), LOM.Accessibility.AccessibilityHazard(), is_lom)

    if data.get('accessibilitycontrol') is not None:
        control = map_attributes(data.get('accessibilitycontrol'), LOM.Accessibility.AccessibilityControl(), is_lom)
    elif data.get('accessibilityControl') is not None:
        control = map_attributes(data.get('accessibilityControl'), LOM.Accessibility.AccessibilityControl(), is_lom)



    accessibility_object.accessibility_api = api
    accessibility_object.accessibility_features = features
    accessibility_object.accessibility_hazard = hazard
    accessibility_object.accessibility_control = control

    print(data)
    print('**********************************')
    print(accessibility_object.__dict__())

    return accessibility_object.__dict__(), accessibility_object


dispatch = {
    'lom:general': general_leaf, 'lom:lifeCycle': life_cycle_leaf, 'lom:metaMetadata': meta_metadata_leaf,
    'lom:technical': technical_leaf, 'lom:educational': educational_leaf,
    'lom:rights': rights_leaf, 'lom:relation': relation_leaf, 'lom:annotation': annotation_leaf,
    'lom:classification': classification_leaf, 'accesibility': accessibility_leaf
}

dispatch_update = {
    'general': general_leaf, 'lifeCycle': life_cycle_leaf, 'metaMetadata': meta_metadata_leaf,
    'technical': technical_leaf, 'educational': educational_leaf,
    'rights': rights_leaf, 'relation': relation_leaf, 'annotation': annotation_leaf,
    'classification': classification_leaf, 'accesibility': accessibility_leaf
}


def update_leaf(leaf, model, data):
    print('UPDATE')
    import json
    data_as_dict = json.loads(data)
    metodo = dispatch_update.get(leaf)
    data = data_as_dict.copy()

    for key in data_as_dict.keys():
        components = str(key).lower().split(' ')
        components = components[0] + ''.join(x.title() for x in components[1:])
        data[components] = data.pop(key)

    model.__setattr__(leaf, metodo(data, True)[1])

    return model
