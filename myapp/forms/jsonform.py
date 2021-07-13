import wtforms_json
from flask import request
from wtforms import Form


class JsonForm(Form):
    @classmethod
    def init_and_validate(cls):
        wtforms_json.init()
        form = cls.from_json(request.get_json())
        # valid = form.validate()
        # if not valid:
        #     raise Exception(form.errors)
        return form
