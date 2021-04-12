class LOM:
    class General:
        class Identifier:
            catalog = ''
            entity = ''

        title = ''
        language = ''
        description = ''
        keyword = ''
        coverage = ''
        structure = ''
        aggregation_level = ''

    class LifeCycle:
        version = ''
        status = ''

        class Contribute:
            role = ''
            entity = ''
            date = ''

    class MetaMetadata:
        class Identifier:
            catalog = ''
            schema = ''

        class Contribute:
            role = ''
            entity = ''
            date = ''

        metadata_schema = ''
        language = ''

    class technical:
        format = ''
        size = ''
        location = ''

        class Requirement:
            class OrComposite:
                type = ''
                name = ''
                minimum_version = ''
                maximum_version = ''

        installation_remarks = ''
        other_platform_requirements = ''
        duration = ''

    class Educational:
        interactivity_type = ''
        learning_resource_type = ''
        interactivity_level = ''
        semantic_density = ''
        intended_end_user_role = ''
        context = ''
        typical_age_range = ''
        difficulty = ''
        typical_learning_time = ''
        description = ''
        language = ''

    class Rights:
        cost = ''
        copyright_and_other_restrictions = ''
        description = ''

    class Relation:
        kind = ''

        class Resource:
            class Identifier:
                catalog = ''
                entry = ''

            description = ''

    class Annotation:
        entity = ''
        date = ''
        description = ''

    class Classification:
        purpose = ''

        class TaxonPath:
            source = ''

            class Taxon:
                id = ''
                entry = ''

                def to_dict(self):
                    return self.__dict__

            def to_dict(self):
                return self.__dict__

        description = ''
        keyword = ''

        def to_dict(self):
            return self.__dict__


class Leo:
    alvarado = 'ALVARADO'
    apellido = 'alv'

    class Trabajo:
        nombre: 'UPS'
        entorno: 'DIOS SABRA'
        lele = 912

        def dict_trabajo(self):
            return {'nombre': 'Attribute', 'entorno': 'Otro'}

    def dict(self, trabajo):
        return {'alvarado': self.alvarado, 'apellido': self.apellido, 'Trabajo': trabajo.dict_trabajo()}


leo = Leo()
trabajo = leo.Trabajo()
print(trabajo.lele)
print('LEO: ', leo.dict(trabajo))
