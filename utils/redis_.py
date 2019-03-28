from utils import rd


def add_popu_rank_foods(foods_id):
    # 添加人气排行
    rd.zincrby('popu_foods_rank', 1, foods_id)


def top_popu_rank_foods(top_n):
    # 查询人气排行
    # [(b'1001', 5.0), (b'1003', 4.0)]  -> { 1:{id, name, price..},  2:{}}
    top_list = rd.zrevrange('popu_foods_rank', 0, top_n-1, withscores=True)

    return [(int(foods_id.decode()), int(score)) for foods_id, score in top_list ]