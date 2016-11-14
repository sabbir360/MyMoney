"""

__author__ = 'Sabbir'
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from flask import redirect, request, abort, Response, session
#  from project.sweetcore.c_system import c_render, redirect_helper, set_message
#  from project.sweetcore.appdb import db_session
from appcore import db
from appcore.helpers.Controller import Controller
from appcore.models.InstanceBatch import InstanceBatch
from appcore.service.InstanceBatchService import InstanceBatchForm


class InstanceBatchController(Controller):

    def instance_batch_index(self):
        self.set_title("Instance Batch List")
        unauthenticated = self.redirect_helper()
        if unauthenticated:
            return redirect(unauthenticated)
        elif session.get("role") and eval(session.get("role")) != "Super":
            return abort(401, "Unsatisfied Role")

        search_str = request.values.get("query") or ''
        model = InstanceBatch
        filter_opt = model().query
        if search_str:
            filter_opt = filter_opt.filter(or_(
                model.name.like("%"+search_str+"%"),
                model.create_date.like("%"+search_str+"%"),
                model.update_date.like("%"+search_str+"%"),
            ))

        result = filter_opt.all()

        return self.render("instance/batch/index",
                           form=InstanceBatchForm(request.form), search_str=search_str,
                           result=result)

    def instance_batch_add(self):
        unauthenticated = self.redirect_helper()
        self.set_title("Add New Instance Batch")
        if unauthenticated:
            return redirect(unauthenticated)
        elif session.get("role") and eval(session.get("role")) != "Super":
            return abort(401, "Unsatisfied Role")

        form = InstanceBatchForm(request.form)
        if request.method == 'POST' and form.validate():
            model = InstanceBatch(form.name.data)
            try:
                db.session.add(model)
                db.session.commit()
                self.set_message("Batch added successfully", "info")
                return redirect("/instance/batch")
            except IntegrityError as ex:
                self.set_message(str(ex))
        return self.render("instance/batch/add", form=form)

    def instance_batch_edit(self):
        self.set_title("Edit Instance Batch")
        unauthenticated = self.redirect_helper()
        if unauthenticated:
            return redirect(unauthenticated)
        elif session.get("role") and eval(session.get("role")) != "Super":
            return abort(401, "Unsatisfied Role")

        form_id = request.values.get("id")
        if form_id:
            model_data = InstanceBatch().query.get(form_id)
            if not model_data:
                return abort(404)
            form = InstanceBatchForm(request.form, obj=model_data)
            if request.method == 'POST' and form.validate():
                try:
                    model_data.name = form.name.data
                    db.session.commit()
                    self.set_message("Batch added successfully", "info")
                    return redirect("/instance/batch")
                except IntegrityError as ex:
                    self.set_message(str(ex))
        else:
            return abort(400)
        return self.render("instance/batch/add", form=form, form_id=form_id)

    def instance_batch_delete(self):
        if request.method == 'POST':
            unauthenticated = self.redirect_helper()
            if unauthenticated:
                return abort(401)
            elif session.get("role") and eval(session.get("role")) != "Super":
                return abort(401, "Unsatisfied Role")

            form_id = request.form.get("id")

            if form_id:
                model_data = InstanceBatch().query.get(form_id)
                if not model_data:
                    abort(404)
                db.session.delete(model_data)
                db.session.commit()
                self.set_message("Batch("+model_data.name+") deleted successfully")
                return self.response("Success")
        return abort(400)

instance_batch_controller = InstanceBatchController()
"""
