"""

__author__ = 'Sabbir'
from datetime import datetime

from appcore import db


class InstanceBatch(db.Model):
    from appcore.models import InstanceIdentifier, InstanceCommand,\
        ScalingConfig

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False, unique=True, index=True)

    instance_identifier = db.relationship(InstanceIdentifier.InstanceIdentifier,
                                          backref=db.backref("instance_batch"))
    instance_command = db.relationship(InstanceCommand.InstanceCommand,
                                       backref=db.backref("instance_command_batch"))
    scaling_config = db.relationship(ScalingConfig.ScalingConfig,
                                     backref=db.backref("scaling_config_batch"))

    create_date = db.Column(db.DateTime, default=datetime.now)
    update_date = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, name=None):
        self.name = name

    def combo(self):
        return self.query.order_by("name")
"""
