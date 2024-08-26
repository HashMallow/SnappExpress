import pandas as pd
import os

cities = []
for item in os.listdir('Vendors'):
    df_ = pd.read_csv(f'Vendors/{item}')
    cities+=[item.split('_')[-1].split('.')[0]]*df_.shape[0]

df = pd.read_csv('vendor_details.csv')

res = []
for i in range(df.shape[0]):
    row = eval(df.iloc[i]['Vendor_Details'])
    if 'data' in row:
        res.append(row['data']['superMarket']['data']['vendorInfo'])
    else:
        empty_dict = {'data': {'superMarket': {'__typename': 'SuperMarketResponse',
                          'data': {'__typename': 'SuperMarketResult',
                                   'sections': [],
                                   'vendorInfo': {'__typename': 'VendorInfo',
                                                  'address': '',
                                                  'area': '',
                                                  'backgroundImage': '',
                                                  'city': cities[i],
                                                  'code': df.iloc[i]['code'],
                                                  'commentCount': None,
                                                  'deliveryData': {},
                                                  'deliveryStatus': '',
                                                  'distance': None,
                                                  'hasSlowDelivery': None,
                                                  'id': df.iloc[i]['id'],
                                                  'isLiked': None,
                                                  'isOpen': None,
                                                  'isPreorderEnabled': None,
                                                  'isPro': None,
                                                  'latencyMinutes': None,
                                                  'location': {'__typename': 'Location',
                                                               'lat': None,
                                                               'lon': None},
                                                  'logo': '',
                                                  'maxDiscount': None,
                                                  'minOrder': None,
                                                  'minimumOrderValue': None,
                                                  'paymentTypesToShow': [],
                                                  'preOrderSchedule': {},
                                                  'preOrderStatus': '',
                                                  'preorderToday': {},
                                                  'preorderTomorrow': {},
                                                  'rating': None,
                                                  'reviewStars': {},
                                                  'schedules': [],
                                                  'status': '',
                                                  'textCommentCount': None,
                                                  'title': '',
                                                  'vendorImages': [],
                                                  'vendorImagesCount': None,
                                                  'vendorState': '',
                                                  'vendorStateText': ''}},
                          'errors': None,
                          'status': ''}}}
        
        res.append(empty_dict['data']['superMarket']['data']['vendorInfo'])

df = pd.DataFrame(res)
df['lat'] = df['location'].apply(lambda x:x['lat'])
df['lon'] = df['location'].apply(lambda x:x['lon'])
df.drop(columns=['location'],inplace=True)
df.to_csv('Vendor_Details_final.csv',index=False,encoding='utf-8-sig')