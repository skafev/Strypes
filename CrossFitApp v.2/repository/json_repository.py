import json

from repository.repository import Repository


class JsonRepository(Repository):
    def __init__(self, idGenerator, db_filename, entity_class):
        super().__init__(idGenerator)
        self.db_filename = db_filename
        self.entity_class = entity_class

    def save(self):
        with open(self.db_filename, 'wt', encoding='utf8') as f:
            json.dump(list(self.find_all()), f, indent=4, default=dumper)

    def load(self):
        with open(self.db_filename, "rt", encoding="utf-8") as f:
            users = json.load(f, object_hook=object_hook(self.entity_class)) # IIFE
            for user in users:
                self.create(user)


def dumper(obj):
    try:
        return obj.to_json()
    except AttributeError:
        return obj.__dict__


entity_class = None


def object_hook(entity_class):
    def obj_hook(jsdict):
        obj = entity_class()
        obj.__dict__ = jsdict
        return obj

    return obj_hook
