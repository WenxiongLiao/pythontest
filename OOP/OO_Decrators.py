# def add_candles(cake_func):
#     def insert_candles():
#         return cake_func() + 'candles'
#     return insert_candles
#
# def make_cake():
#     return 'cake'
#
# gift_func = add_candles(make_cake)
#
# print(make_cake())
# print(gift_func)


def add_candles(cake_func):
    def insert_candles():
        return cake_func() + 'candles'
    return insert_candles

@add_candles
def make_cake():
    return 'cake'

#make_cake = add_candles(make_cake)

print(make_cake())
# print(gift_func)