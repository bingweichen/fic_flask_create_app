# !/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g
from flask_restplus import Resource, Namespace, fields
from app.{{cookiecutter.project_slug}} import service as {{cookiecutter.project_slug}}_service
from common.decorators import arguments_parser, catch_error
from common.responses import created, ok
from app.user.service import token_required
from app.{{cookiecutter.project_slug}}.model import {{cookiecutter.ClassName}}


api = Namespace('{{cookiecutter.project_slug}}', path='/{{cookiecutter.project_slug}}')
{{cookiecutter.project_slug}}_model = api.model('login', {
    # 'username': fields.String(required=True, description='user username'),
    # 'password': fields.String(required=True, description='user password '),
})


@api.route('')
class {{cookiecutter.ClassName}}sResource(Resource):
    """{{cookiecutter.ClassName}} Resource"""

    @api.marshal_with({{cookiecutter.project_slug}}_model)
    def get(self):
        """获取所有 {{cookiecutter.project_slug}}"""
        return {{cookiecutter.ClassName}}.query.filter_by().all()

    @api.doc(description='create {{cookiecutter.project_slug}}')
    @api.expect({{cookiecutter.project_slug}}_model, validate=True)
    @arguments_parser
    @catch_error
    @token_required
    def post(self):
        """创建 {{cookiecutter.project_slug}}"""
        data = g.args
        current_user = g.user
        result = {{cookiecutter.project_slug}}_service.create_{{cookiecutter.project_slug}}(data, current_user)
        return created(result)


@api.route('/<string:{{cookiecutter.project_slug}}_id>')
class {{cookiecutter.ClassName}}Resource(Resource):
    @api.marshal_with({{cookiecutter.project_slug}}_model)
    def get(self, {{cookiecutter.project_slug}}_id):
        """获取{{cookiecutter.project_slug}}"""
        return {{cookiecutter.ClassName}}.query.filter_by(id={{cookiecutter.project_slug}}_id).first()

    @token_required
    def delete(self, {{cookiecutter.project_slug}}_id):
        """删除{{cookiecutter.project_slug}}"""
        result = {{cookiecutter.project_slug}}_service.delete_{{cookiecutter.project_slug}}({{cookiecutter.project_slug}}_id)
        return ok(result, "delete success")

    @api.expect({{cookiecutter.project_slug}}_model, validate=True)
    @arguments_parser
    @catch_error
    @token_required
    @api.marshal_with({{cookiecutter.project_slug}}_model)
    def put(self, {{cookiecutter.project_slug}}_id):
        """更新{{cookiecutter.project_slug}}"""
        result = {{cookiecutter.project_slug}}_service.update_{{cookiecutter.project_slug}}({{cookiecutter.project_slug}}_id={{cookiecutter.project_slug}}_id, data=g.args)
        return result


