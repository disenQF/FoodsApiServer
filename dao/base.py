from pymysql.cursors import DictCursor

from dao import db


class BaseDao():
    def total(self, table):
        with db.cursor() as c:
            c.execute('select count(id) from %s ' % table)
            total = c.fetchone()[0]

        return total

    def query(self, sql, *args):
        with db.cursor(cursor=DictCursor) as c:
            c.execute(sql, args=args)
            data = list(c.fetchall())

        return data

    def list(self, table, *columns, **kwargs):
        order_by = kwargs.get('order_by')

        page_size = kwargs.get('page_size') # 分页的页面数据大小
        page_num = kwargs.get('page_num')  # 分页的页码

        cols = ','.join(columns)
        sql = 'select %s from %s' % (cols, table)

        if order_by:
            sql += ' order by %s' % order_by

        if page_num:
            # 判断每页显示的记录数是否未设置，未设置时，默认一页显示10条
            page_size = 10 if page_size is None else page_size

            sql += ' limit %s, %s' % ((page_num-1)*page_size, page_size)

        with db.cursor(cursor=DictCursor) as cursor:
            cursor.execute(sql)
            data = list(cursor.fetchall())

        return data

    def query_by_id(self, table, id, *columns):
        cols = ','.join(columns)
        sql = 'select %s from %s where id=%s' % (cols, table, id)
        with db.cursor(cursor=DictCursor) as cursor:
            cursor.execute(sql)
            data = cursor.fetchone()

        return data

    def save(self, table, instance: dict):
        pass

    def update(self, table, instance: dict):
        pass

    def delete(self, table, id):
        pass
