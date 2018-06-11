from diary.modules.resume.entities import (
    BaseNoteEntity,
    NoteEntity
)

import datetime


class NoteSerializer(object):

    @staticmethod
    def orm_to_dataclass(query):

        values = []
        list_types = list(query.values_list('role__name', flat=True))
        types = dict((el,[]) for el in list_types)

        for n in query:
            entity = NoteEntity(
                n.created_at,
                n.text,
                n.featured,
            )

            types[n.role.name].append(entity)

        for k in types.keys():
            base = BaseNoteEntity(k, types[k])
            values.append(base)

        return values

    @staticmethod
    def dataclass_to_dict(base):

        data = []

        for b in base:
            obj = {
                'name': b.role_name,
                'total': len(b.notes)
            }

            obj['notes'] = []
            
            for d in b.notes:
                notedic = {
                    'time': d.time,
                    'text': d.text,
                    'featured': d.featured
                }
                obj['notes'].append(notedic)
            
            data.append(obj)

        return data
