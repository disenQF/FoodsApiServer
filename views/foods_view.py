from flask import Blueprint, jsonify
from flask import request

from dao.base import BaseDao
from utils import redis_

blue = Blueprint('foods', __name__)


@blue.route('/foods/')
def query_category():
    dao = BaseDao()
    sql = """
        select * from v_foods_cate
        order by cate_name
        limit %s, 10
    """

    page_num = request.args.get('page')
    page_num = int(page_num) if page_num else 1

    data = dao.query(sql, (page_num-1)*10)
    total = dao.total('t_foods')
    return jsonify({'data':data,
                    'total_rows': total,
                    'total_page': total//10 + 1 if (total % 10) > 0 else 0})


@blue.route('/foods/<int:id>/')
def get_by_id(id):
    dao = BaseDao()
    sql = 'select * from v_foods_cate where id=%s'
    data = dao.query(sql, id)

    # 将当前查看的foods_id加入人气排行中
    redis_.add_popu_rank_foods(id)

    return jsonify(data)


@blue.route('/rank_foods/')
def top_rank_foods():
    rank_list = redis_.top_popu_rank_foods(5)  # 前5个人气排行

    dao = BaseDao()
    sql = 'select * from v_foods_cate where id=%s'
    results = {
        score: dao.query(sql, foods_id)[0]
        for foods_id, score in rank_list
    }

    return jsonify(results)