from diary.modules.resume.entities import (
    BaseDedicationEntity,
    DedicationEntity
)


class DedicationSerializer(object):

    @staticmethod
    def orm_to_dataclass(query):

        values = []
        list_types = list(query.values_list('type__name', flat=True))
        types = dict((el, []) for el in list_types)

        for d in query:
            entity = DedicationEntity(
                d.cycle,
                d.time,
                [
                    {
                        'slug': t.slug,
                        'name': t.name
                    }
                    for t in d.tags.all()
                ]
            )

            types[d.type.name].append(entity)

        for k in types.keys():
            base = BaseDedicationEntity(k, types[k])
            values.append(base)

        return values

    @staticmethod
    def dataclass_to_dict(base):

        data = []

        for b in base:
            obj = {
                'name': b.type_name,
                'total': len(b.dedications)
            }

            obj['dedications'] = []
            for d in b.dedications:
                dedic = {
                    'cycle': d.cycle,
                    'time': d.time,
                    'total_minutes': d.total_minutes,
                    'total_time': d.total_time,
                    'tags': d.tags
                }
                obj['dedications'].append(dedic)

            data.append(obj)

        return data
