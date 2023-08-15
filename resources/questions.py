import json
import traceback
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt, get_jwt_identity, decode_token

from sqlalchemy.orm.attributes import flag_modified

import uuid
import datetime

from models import UserModel, SessionTokenModel
from schema import QuestionsGenerated

from db import db, addAndCommit, deleteAndCommit

from globals import DEBUG, DEFAULT_CATEGORIES, DEFAULT_EXAMPLES

from helpers.ProcessQuestions import ProcessQuestions

blp = Blueprint('questions', __name__, description='Questions generator')

processQuestions = ProcessQuestions()

@blp.route('/<int:n>')
class QuestionGenerator(MethodView):
    @jwt_required(refresh=True)
    @blp.response(200, QuestionsGenerated)
    def get(self, n):
        
        user = UserModel.query.get_or_404(get_jwt_identity())
        
        settings = user.settings
        
        result = processQuestions.get_questions(categories=settings['categories'], examples=settings['examples'], n=n)
        
        return {'questions': result}

