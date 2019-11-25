#!/usr/bin/env python
# -*- coding: utf-8 -*-

from exts import db
import datetime
from common.base_model import BaseModel


class {{cookiecutter.ClassName}}(db.Model, BaseModel):
    __tablename__ = '{{cookiecutter.project_slug}}'

    id = db.Column(db.Integer, primary_key=True)
    md_body = db.Column(db.Text)

    create_datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)



