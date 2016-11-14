__author__ = 'Sabbir'
from wtforms import validators, Form, StringField, SelectField


class InstanceIdentifierForm(Form):
    #  from appcore.models.InstanceBatch import InstanceBatch
    key_name = StringField('Key Name', [validators.length(min=1, max=30)])
    host = StringField('Host', [validators.length(min=1, max=30)])
    username = StringField('Server User', [validators.length(min=1, max=30)])
    name = StringField('Name', [validators.length(max=50)])
    # for row in InstanceBatch().combo():
    #     print (row.id, row.name)
    #  from appcore.models.InstanceBatch import InstanceBatch

    instance_batch_id = SelectField('Instance Batch',  [validators.InputRequired()],
                                    coerce=int)
