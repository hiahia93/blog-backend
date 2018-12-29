from abc import ABC
import time
from apps.default_handler import DefaultHandler, get_json, auth
from apps.label.model import Label


class LabelHandler(DefaultHandler, ABC):

    @auth
    @get_json('label')
    async def post(self, *args, **kwargs):
        label = self.body.get('label')
        la = Label()
        await la.connect()
        one = await la.insert_label(label)
        del label
        if one is None:
            self.set_status(400)
            return
        self.set_status(201)

    @auth
    @get_json()
    async def put(self, *args, **kwargs):
        await self.put_one(Label(), *args, **kwargs)

    @auth
    async def delete(self, *args, **kwargs):
        await self.delete_one(Label(), *args, **kwargs)


class LabelsHandler(DefaultHandler, ABC):
    async def get(self, *args, **kwargs):
        la = Label()
        await la.connect()
        many = await la.select_labels()
        del la
        if many is None:
            self.set_status(404)
            return
        labels = []
        for m in many:
            labels.append({
                'label': m[0],
                'created_at': time.mktime(m[1].timetuple()),
            })
        self.finish({'items': labels})
