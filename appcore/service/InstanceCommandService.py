__author__ = 'Sabbir'
from sqlalchemy import or_
from wtforms import Form, validators, StringField, SelectField, TextAreaField
from appcore.helpers.Service import Service
from appcore.models import InstanceCommand, InstanceBatch


class InstanceCommandForm(Form):
    #  from appcore.models.InstanceBatch import InstanceBatch

    instance_batch_id = SelectField("Instance Batch", [validators.DataRequired()],
                                    choices=[
                                        (row.id, row.name)
                                        for row in InstanceBatch.InstanceBatch().combo()
                                        ], coerce=int)

    command = TextAreaField('Command', [validators.length(min=2, max=1600)])
    name = StringField("Name", [validators.length(max=50)])


class InstanceCommandService(Service):

    def get_paginated_list(self, search_str, batch_id, page_no):
        model = InstanceCommand.InstanceCommand
        instance_batch_model = InstanceBatch.InstanceBatch
        filter_opt = model().query. \
            join(instance_batch_model, aliased=True)

        if search_str:
            filter_opt = filter_opt.filter(model.instance_batch_id == instance_batch_model.id,
                                           or_(model.command.like("%" + search_str + "%"),
                                               instance_batch_model.name.like("%" + search_str + "%"),
                                               model.name.like("%" + search_str + "%"),
                                               model.create_date.like("%" + search_str + "%"),
                                               model.update_date.like("%" + search_str + "%")))

        if batch_id > 0:
            filter_opt = filter_opt.filter(model.instance_batch_id == batch_id)
        #  count = filter_opt.count()
        #  result = filter_opt.limit(self.per_page).all()
        #  self.per_page = 5
        return self.page_generator(filter_opt, page_no)