import pandas as pd
from Python import another_one
from Python import sona
from time import sleep


def main_brain(buy_list, sell_list):
    last_list = []

    for i in buy_list:
        b_sticker, b_order_type, b_volume, buy_price = i[0:4]
        for j in sell_list:
            s_sticker, s_order_type = j[0:2]

            if b_sticker == s_sticker and s_order_type == b_order_type:
                s_volume, sell_price = j[2:4]
                if b_volume == s_volume:
                    last_list.append([s_sticker, buy_price, sell_price, s_volume])
                    sell_list.remove(j)
                    break
                elif b_volume > s_volume:
                    last_list.append([s_sticker, buy_price, sell_price, s_volume])
                    sell_list.remove(j)
                    buy_list.append(b_sticker, b_order_type, (int(b_volume) - int(s_volume)), buy_price)
                elif b_volume < s_volume:
                    last_list.append([s_sticker, buy_price, sell_price, b_volume])
                    sell_list.remove(j)
                    sell_list.append(s_sticker, s_order_type, (int(s_volume) - int(b_volume)), sell_price)

            else:
                continue

    # print(last_list)
    another_one.brokerage_calulator(last_list)


sona.starting_part()

sleep(10)


trade_book = pd.read_csv("/home/ai/Downloads/orders.csv")

trade_book.sort_values(by=["Time"], inplace=True)
trade_book.drop(trade_book[trade_book["Status"] != "COMPLETE"].index, inplace=True)

real_data = trade_book.drop(["Time", "Status"], axis=1)

temp_list = real_data.values.tolist()

stocks_buy_list = []
stocks_sell_list = []

for i in temp_list:
    if i[0] == "BUY":
        stocks_buy_list.append([i[1], i[2], i[3], i[4]])
    elif i[0] == "SELL":
        stocks_sell_list.append([i[1], i[2], i[3], i[4]])


main_brain(stocks_buy_list, stocks_sell_list)

















