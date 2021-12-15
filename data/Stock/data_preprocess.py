import pandas as pd
"""
这个因子名字叫“红三兵”，即
    1.连续三天阳线；
    2.第二、三天开盘价在前一天阳线实体之内；
    3.每天收盘价接近当天最高点；
    4.三根阳线实体部分近似等长；
    5.出现“红三兵”，看涨，记为1，否则记为0。
同时满足这5条时，买入信号即触发，即我们给它评1分，否则评0分。
"""


def is_red(data, i, n):
    if i > len(data) - n:
        return False
    else:
        res = True
        # 未来（包含当天）n天，收盘价高于开盘价则为True
        for j in range(i, i + n):
            res = res and data.close[j] > data.open[j]
            if not res:
                return False
        return res


def is_open_in_last_entity(data, i, n):
    if i > len(data) - n - 1:
        return False
    else:
        res = True
        # 未来（包含当天）n天，开盘价高于第二天开盘价则为True
        for j in range(i, i + n):
            res = res and data.open[j] > data.open[j + 1]
            if not res:
                return False
        return res


def is_close_near_high(data, i, n, p=0.01):
    if i > len(data) - n:
        return False
    else:
        res = True
        # 未来（包含当天）n天，收盘价与最高价的距离比值小于某个阈值则为True
        for j in range(i, i + n):
            if (data.high[j] <= 0):
                return False
            res = res and (data.high[j] - data.close[j]) / data.high[j] < p
        return res


def is_entity_equal(data, i, n, p=0.8):
    if i > len(data) - n:
        return False
    else:
        Max = 0
        Min = 10000
        Sum = 0
        # 未来（包含当天）n天，计算收盘价和开盘价的绝对偏差，计算n天内绝对偏差的最大值、最小值、平均值，计算比率(Max - Min) / (Sum / n)，小于p则为True
        for j in range(i, i + n):
            e = abs(data['close'][j] - data['open'][j])
            if e > Max:
                Max = e
            if e < Min:
                Min = e
            Sum = Sum + e

        if Sum > 0 and n > 0 and (Max - Min) / (Sum / n) < p:
            return True
        else:
            return False


def is_red_3_soldier(data, i, n=3, p1=0.01, p2=0.8):
    if i > len(data) - n:
        return False
    else:
        res1 = is_red(data, i, n) and is_open_in_last_entity(data, i, n - 1)
        res2 = is_close_near_high(data, i, n, p1) and is_entity_equal(
            data, i, n, p2)
        return res1 and res2


def preprocess(data):

    reserve_columns = ['date', 'open', 'high', 'low', 'close', 'turnover']
    data = data[reserve_columns]
    return data


if __name__ == '__main__':
    data_path = '/home/workdir/Informer2020/data/Stock/stack_btkj_data.csv'
    data = pd.read_csv(data_path)
    data = preprocess(data)
    data.to_csv(data_path, index=False)
