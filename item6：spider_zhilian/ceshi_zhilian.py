# -*- coding:utf-8 -*-
# author:吉祥鸟
# datetime:2019/7/25 上午7:03
# software: PyCharm

import requests

headers = {
    'origin': 'https://sou.zhaopin.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://sou.zhaopin.com/?p=2&jl=489&kw=python&kt=3&sf=0&st=0',
    'authority': 'fe-api.zhaopin.com',
    'cookie': 'sts_deviceid=16adff4311833-07d15df7dfa5d7-162a1c0b-2073600-16adff4311ade; x-zp-client-id=6fea26f5-c334-4736-8ae7-26632df17cae; adfbid2=0; __utmz=269921210.1559279474.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); sou_experiment=unexperiment; _jzqa=1.723798106112072400.1559283156.1559283156.1561076286.2; _jzqx=1.1559283156.1561076286.1.jzqsr=zhaopin%2Ecom|jzqct=/.-; acw_tc=2760826c15615973610475130ec34e17650e240dbc59f7c5be16309d7c7291; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1559523942,1561076282,1561604916,1561863319; __utma=269921210.1616776710.1559279474.1561604916.1561863319.7; UM_distinctid=16ba64fb8c1273-01c4d88bb460ee-162a1c0b-1fa400-16ba64fb8c449f; sts_sg=1; sts_sid=16c2639a87b501-070006b2384182-162a1c0b-2073600-16c2639a87d775; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.google.com%2F; jobRiskWarning=true; urlfrom=121114584; urlfrom2=121114584; adfcid=www.google.com; adfcid2=www.google.com; adfbid=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221006586294%22%2C%22%24device_id%22%3A%2216adff43260427-07dc7a026e470e-162a1c0b-2073600-16adff4326388%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2216adff43260427-07dc7a026e470e-162a1c0b-2073600-16adff4326388%22%7D; dywea=95841923.2227774250925340200.1559279474.1561863319.1564009409.9; dywec=95841923; dywez=95841923.1564009409.9.3.dywecsr=google.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; dyweb=95841923.1.10.1564009409; ZP_OLD_FLAG=false; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%2201a5c23c-9134-4665-9147-e1de8ea87b92-sou%22%2C%22funczone%22:%22smart_matching%22}}; sts_evtseq=7',
}

params = (
    ('start', '90'),
    ('pageSize', '90'),
    ('cityId', '489'),
    ('workExperience', '-1'),
    ('education', '-1'),
    ('companyType', '-1'),
    ('employmentType', '-1'),
    ('jobWelfareTag', '-1'),
    ('kw', 'python'),
    ('kt', '3'),
    ('_v', '0.84889719'),
    ('x-zp-page-request-id', '00b8cc2f1dfe476a8f8bd4e27dc96413-1564009415329-505361'),
    ('x-zp-client-id', '6fea26f5-c334-4736-8ae7-26632df17cae'),
)

response = requests.get('https://fe-api.zhaopin.com/c/i/sou', headers=headers, params=params)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.84889719&x-zp-page-request-id=00b8cc2f1dfe476a8f8bd4e27dc96413-1564009415329-505361&x-zp-client-id=6fea26f5-c334-4736-8ae7-26632df17cae', headers=headers)
