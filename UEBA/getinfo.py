import h5py,argparse, re
from tqdm import tqdm
import pandas as pd, numpy as np
import requests
import geoip2.database
import socket
import time
reader = geoip2.database.Reader('./GeoLite2-City_20210921/GeoLite2-City.mmdb')
def privateIp(ip):
    if re.match('^192\.168\..*',ip):
        return 'C'
    elif re.match('^10\..*',ip):
        return 'A'
    elif re.match('^172\..*', ip):
        return 'B'
    else:
        return 'D'
def geturlInfoGeoip(ip):
    body = reader.city(ip)
    return pd.Series([body.country.iso_code,body.location.latitude,body.location.longitude],index=['country','lat','lon'])
def geturlInfoIPApi(url):
    server='http://ip-api.com/json/'
    time.sleep(0.01)
    response = requests.get(server+url,headers={'User-agent': 'Firefox'})
    sleeptime = 10
    while response.status_code==429:
        if sleeptime>80:
            print('warning')
        time.sleep(sleeptime)
        sleeptime *= 2
        response = requests.get(server+url,headers={'User-agent': 'Firefox {}'.format(sleeptime)})
    body = response.json()
    return pd.Series([body.get('countryCode'),body.get('lat'),body.get('lon')],index=['country','lat','lon'])
def geturlInfo(url):
    if re.match('^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$', url):
        if privateIp(url)!='D':
            return baiduIpInfo
        return geturlInfoGeoip(url)
    else:
        try:
            ip = socket.gethostbyname(url)
            return geturlInfoGeoip(ip)
        except:
            return baiduIpInfo
        return geturlInfoIPApi(url)
psr = argparse.ArgumentParser()
psr.add_argument('-o', dest='opt', help='output file')
psr.add_argument('-i', dest='ipt', help='inputfile')
args = psr.parse_args()
trainDf = pd.read_csv('./train_data', encoding='gb2312')
urlSelect = trainDf['url'].apply(lambda x: re.match('^.*//(.*)$',x).group(1))
ip = socket.gethostbyname("baidu.com")
baiduIpInfo = geturlInfoGeoip(ip)
print(baiduIpInfo)
urlinfo = np.empty((urlSelect.shape[0],),dtype=[('country','S4'),('lat',float),('lon',float)])
with h5py.File(args.opt,'w') as opt:
#     if 'urlinfo' in opt.keys():
#         urlinfo = opt['urlinfo']
#         start = opt.attrs['start']
#     else:
#         urlinfo = opt.create_dataset('urlinfo', shape=(urlSelect.shape[0],),dtype=[('country','S4'),('lat',float),('lon',float)])
#         start = 0
#     for i in tqdm(range(start, urlSelect.shape[0])):
    start = 0
    for i in tqdm(range(start, urlSelect.shape[0])):
        temp = geturlInfo(urlSelect[i]).to_numpy()
        urlinfo[i]['country'] = temp[0]
        urlinfo[i]['lat'] = temp[1]
        urlinfo[i]['lon'] = temp[2]
#         opt.attrs['start'] = i
    opt.create_dataset('urlinfo', data=urlinfo, compression='gzip')
