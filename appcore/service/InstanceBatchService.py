__author__ = 'Sabbir'
from wtforms import Form, StringField, validators


class InstanceBatchForm(Form):
    name = StringField('Name', [validators.length(min=1, max=80)])
