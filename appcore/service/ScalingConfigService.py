__author__ = 'Sabbir'
from wtforms import Form, validators, IntegerField, SelectField, StringField


class ScalingConfigValidators(Form):
    from appcore.models.InstanceBatch import InstanceBatch

    instance_batch_id = SelectField("Instance Batch",
                                    [validators.DataRequired()],
                                    choices=[
                                        (row.id, row.name)
                                        for row in InstanceBatch().combo()], coerce=int)
    name = StringField("Config Name", [validators.DataRequired()])
    cpu_max = IntegerField("Max. CPU", [validators.DataRequired()])
    cpu_min = IntegerField("Min. CPU", [validators.DataRequired()])
    ram_max = IntegerField("Max. RAM", [validators.DataRequired()])
    ram_min = IntegerField("Min. RAM", [validators.DataRequired()])
    storage_max = IntegerField("Max. Storage", [validators.DataRequired()])
    storage_min = IntegerField("Min. Storage", [validators.DataRequired()])
    min_instance = IntegerField("Min. Instance", [validators.DataRequired()])
    max_instance = IntegerField("Max. Instance", [validators.DataRequired()])
    exceed_action = IntegerField("Exceed Action", [validators.DataRequired()])
