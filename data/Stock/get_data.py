import akshare as ak

if __name__ == '__main__':
    # stock_zh_a_spot_df = ak.stock_zh_a_spot()
    # stock_zh_a_spot_df.to_csv("./stack_data.csv", index = False)
    # print(stock_zh_a_spot_df)
    data_btkj = ak.stock_zh_a_daily('sz300031', adjust='hfq')
    data_btkj.to_csv('./stack_btkj_data.csv', index=False)
    print(data_btkj)
