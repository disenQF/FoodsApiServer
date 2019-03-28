from flask import Blueprint
from flask import request, jsonify

from app import app

from dao.cate import CateDao

blue = Blueprint('category', __name__)


@blue.route('/cate/')
def query_all():
    page_num = request.args.get('page_num')
    page_num = 1 if page_num is None else int(page_num)
    dao = CateDao()
    data = dao.list(order_by='parent_id', page_num=page_num)
    return jsonify({'data': data})