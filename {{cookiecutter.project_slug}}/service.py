#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.{{cookiecutter.project_slug}}.model import {{cookiecutter.ClassName}}
from common.mixins import DictMixin
from common.base_service import BaseService


def create_{{cookiecutter.project_slug}}(data, current_user):
    new_{{cookiecutter.project_slug}} = DictMixin.from_dict({{cookiecutter.ClassName}}, data)
    new_{{cookiecutter.project_slug}}.owner = current_user
    return new_{{cookiecutter.project_slug}}.add()


def update_{{cookiecutter.project_slug}}({{cookiecutter.project_slug}}_id, data):
    {{cookiecutter.project_slug}} = {{cookiecutter.ClassName}}.query.filter_by(id={{cookiecutter.project_slug}}_id).first()
    new_{{cookiecutter.project_slug}} = DictMixin.from_dict({{cookiecutter.project_slug}}, data)
    result = new_{{cookiecutter.project_slug}}.update()
    return new_{{cookiecutter.project_slug}}


def delete_{{cookiecutter.project_slug}}({{cookiecutter.project_slug}}_id):
    {{cookiecutter.project_slug}} = {{cookiecutter.ClassName}}.query.filter_by(id={{cookiecutter.project_slug}}_id).first()
    return {{cookiecutter.project_slug}}.delete()