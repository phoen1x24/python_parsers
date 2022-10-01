import requests
import json

def get_data():

    cookies = {
        '_ym_uid': '1633065789844170228',
        'cfidsgib-w-mvideo': 'gCLyLfZ+mYfJJmzSlEEx6+not44YP+l/uzmtd2E9SSBEqS163Jkkp3RL0HZaGdctc62huq4w+1mFn6dU+PdZbGfMVL5OoMGegqVndXP250+aEvHFR2YsDbhhIMSAQp6PBdq07IwgTyT5tUlGzwv9EjYGNyR37AwvBC85',
        '__hash_': '56dd9961688a163075b8300bca77ffaa',
        '__lhash_': 'ae222929023cf14514ec62678ec0de23',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_2246',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GUEST_ID': '21548742513',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '5400000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_HANDOVER': '0',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '29',
        'MVID_REGION_SHOP': 'S955',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_SMART_BANNER_BOTTOM': '2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '7',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'flacktory': 'no',
        'searchType2': '3',
        '_ym_d': '1664589744',
        '_ym_isad': '1',
        '_gid': 'GA1.2.2075696569.1664589744',
        '_sp_ses.d61c': '*',
        'mindboxDeviceUUID': '565bb7c7-5898-40e5-b292-984c9488ca93',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22565bb7c7-5898-40e5-b292-984c9488ca93%22%7D',
        'SMSError': '',
        'authError': '',
        'advcake_track_id': 'd738a9bf-07f3-9a41-fde9-60c23cc79be1',
        'advcake_session_id': 'deff75bb-9f0b-c7c4-f0b7-f9f446d6ea1a',
        'flocktory-uuid': '32d1bc0f-444e-4cfb-a6d5-6c04a2f620d1-3',
        'afUserId': '724d52d5-b62e-47bf-8f20-7e541393309f-p',
        'AF_SYNC': '1664589755705',
        '_ga': 'GA1.2.1799976506.1664589744',
        '_ga_CFMZTSS5FM': 'GS1.1.1664589744.1.1.1664589954.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1664589744.1.1.1664589954.60.0.0',
        '_sp_id.d61c': '60ca8ad8-b36a-4463-9ae5-9aef139fa934.1664589745.1.1664589958..3f033083-59f0-4114-aea1-0b149b011a3d..1f18ddec-fd54-4a13-8755-63f1068b1263.1664589744555.4',
        '_dc_gtm_UA-1873769-37': '1',
        'JSESSIONID': 'BRRQj3jf5v1TQw7yT2Q2bdWXfyN1hZ8jW0pQG4CfLQspTnYblcNN!639869423',
        'bIPs': '-1707567431',
        'MVID_ENVCLOUD': 'prod2',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=71b914aa7c5a4869a1a85f9047b434e0,sentry-sample_rate=0%2C5',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ym_uid=1633065789844170228; cfidsgib-w-mvideo=gCLyLfZ+mYfJJmzSlEEx6+not44YP+l/uzmtd2E9SSBEqS163Jkkp3RL0HZaGdctc62huq4w+1mFn6dU+PdZbGfMVL5OoMGegqVndXP250+aEvHFR2YsDbhhIMSAQp6PBdq07IwgTyT5tUlGzwv9EjYGNyR37AwvBC85; __hash_=56dd9961688a163075b8300bca77ffaa; __lhash_=ae222929023cf14514ec62678ec0de23; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_2246; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GUEST_ID=21548742513; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=5400000100000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=0; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=29; MVID_REGION_SHOP=S955; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_SMART_BANNER_BOTTOM=2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=7; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=3; _ym_d=1664589744; _ym_isad=1; _gid=GA1.2.2075696569.1664589744; _sp_ses.d61c=*; mindboxDeviceUUID=565bb7c7-5898-40e5-b292-984c9488ca93; directCrm-session=%7B%22deviceGuid%22%3A%22565bb7c7-5898-40e5-b292-984c9488ca93%22%7D; SMSError=; authError=; advcake_track_id=d738a9bf-07f3-9a41-fde9-60c23cc79be1; advcake_session_id=deff75bb-9f0b-c7c4-f0b7-f9f446d6ea1a; flocktory-uuid=32d1bc0f-444e-4cfb-a6d5-6c04a2f620d1-3; afUserId=724d52d5-b62e-47bf-8f20-7e541393309f-p; AF_SYNC=1664589755705; _ga=GA1.2.1799976506.1664589744; _ga_CFMZTSS5FM=GS1.1.1664589744.1.1.1664589954.0.0.0; _ga_BNX5WPP3YK=GS1.1.1664589744.1.1.1664589954.60.0.0; _sp_id.d61c=60ca8ad8-b36a-4463-9ae5-9aef139fa934.1664589745.1.1664589958..3f033083-59f0-4114-aea1-0b149b011a3d..1f18ddec-fd54-4a13-8755-63f1068b1263.1664589744555.4; _dc_gtm_UA-1873769-37=1; JSESSIONID=BRRQj3jf5v1TQw7yT2Q2bdWXfyN1hZ8jW0pQG4CfLQspTnYblcNN!639869423; bIPs=-1707567431; MVID_ENVCLOUD=prod2',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '71b914aa7c5a4869a1a85f9047b434e0-aafd54d2783546af-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-set-application-id': '4584fa89-c12f-4f5b-91be-688e5e6a4638',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    # print(response)

    products_ids = response.get('body').get('products')
    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii = False)
    # print(products_ids)
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    #print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)



    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice' : item_base_price,
            'item_salePrice' : item_sale_price,
            'item_bonus' : item_bonus
        }

        with open('4_items_prices.json', 'w') as file:
            json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')
    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    get_result()
if __name__ =='__main__':
    main()