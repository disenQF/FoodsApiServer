from dao.base import BaseDao


class CateDao(BaseDao):
    def list(self, order_by, page_num):
        # [ {"id":1, "name":"" }, {...}, {}]
        data = super().list('t_foods',
                            'id', 'name', 'price', 'step_minute',
                            order_by=order_by,
                            page_num=page_num)
        return data
