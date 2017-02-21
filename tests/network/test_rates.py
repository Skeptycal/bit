# from time import sleep, time
#
# from bit.network.rates import (
#     RatesApi, btc_to_satoshi, currency_to_satoshi, currency_to_satoshi_cached,
#     mbtc_to_satoshi, satoshi_to_satoshi, ubtc_to_satoshi
# )
#
#
# def test_satoshi_to_satoshi():
#     s = satoshi_to_satoshi()
#     assert isinstance(s, int)
#     assert s == 1
#
#
# def test_ubtc_to_satoshi():
#     s = ubtc_to_satoshi()
#     assert isinstance(s, int)
#     assert s == 100
#
#
# def test_mbtc_to_satoshi():
#     s = mbtc_to_satoshi()
#     assert isinstance(s, int)
#     assert s == 100000
#
#
# def test_btc_to_satoshi():
#     s = btc_to_satoshi()
#     assert isinstance(s, int)
#     assert s == 100000000
#
#
# def test_currency_to_satoshi():
#     assert currency_to_satoshi(1, 'usd') > currency_to_satoshi(1, 'jpy')
#
#
# def test_rates_close():
#     rates = sorted([
#         api_call() for api_call in RatesApi.USD_RATES
#     ])
#     assert rates[-1] - rates[0] < 2000
#
#
# class TestRateCache:
#     def test_cache(self):
#         sleep(0.2)
#
#         start_time = time()
#         currency_to_satoshi_cached(1, 'usd', expires=0)
#         initial_time = time() - start_time
#
#         start_time = time()
#         currency_to_satoshi_cached(1, 'usd', expires=600)
#         cached_time = time() - start_time
#
#         assert initial_time > cached_time
#
#     def test_expires(self):
#         sleep(0.2)
#
#         currency_to_satoshi_cached(1, 'usd', expires=0)
#
#         start_time = time()
#         currency_to_satoshi_cached(1, 'usd', expires=600)
#         cached_time = time() - start_time
#
#         sleep(0.2)
#
#         start_time = time()
#         currency_to_satoshi_cached(1, 'usd', expires=0.1)
#         update_time = time() - start_time
#
#         assert update_time > cached_time