# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# author:吉祥鸟
# datetime:2019/3/14 0014 下午 3:02
# software:     PyCharm
import requests
from pprint import pprint
import time
import hu_utils
from urllib import parse
import os
import json


class zhilian_info():
    def __init__(self):
        # 一次爬取多少页
        self.page = 30
        # 关键字
        self.kws = ["python", '爬虫', '数据分析', '开发']
        self.job_info = []
        self.workExperiences = ['0', '-1', '1', '103', '305', '510', '1099']
        self.educations = ['-1', '1', '4', '3', '5', '12', '13']

    def get_info(self):
        for kw in self.kws:
            kw_parse = parse.quote(kw)
            for workExperience in self.workExperiences:
                for education in self.educations:
                    for p in range(1, self.page):
                        print("关键字：{}；工作经验：{}；学历：{}；正在爬取第{}页".format(kw, workExperience, education, p))
                        referer = 'https://sou.zhaopin.com/?p={}&jl=489&kw={}&kt=3'.format(p, kw_parse)
                        # print(referer)
                        headers = {
                            'Accept': 'application/json, text/plain, */*',
                            'Referer': referer,
                            'Origin': 'https://sou.zhaopin.com',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
                        }
                        params = (
                            ('start', (p - 1) * 100),
                            ('pageSize', '100'),
                            ('cityId', '489'),
                            ('workExperience', workExperience),
                            ('education', education),
                            ('companyType', '-1'),
                            ('employmentType', '-1'),
                            ('jobWelfareTag', '-1'),
                            ('sortType', 'publish'),
                            ('kw', kw),
                            ('kt', '3'),
                            ('_v', '0.45698675'),
                            ('x-zp-page-request-id', '21db425991da4b0f85deb9d8af9c5f7b-1552531215877-432072'),
                        )
                        response = requests.get('https://fe-api.zhaopin.com/c/i/sou', headers=headers, params=params).text
                        time.sleep(0.5)
                        print(response)
                        results = json.loads(response)["data"]["results"]
                        # pprint(results)

                        if not results:
                            print("页面已爬取，跳过关键字：{}".format(kw))
                            break
                        for result in results:
                            info = {}
                            # pprint(result)
                            info["city"] = result["city"]["display"]
                            info["et_name"] = result["company"]["name"]
                            info["et_name_num"] = result["company"]["number"]
                            # info["et_size_code"] = result["company"]["size"]["code"]
                            info["et_size_name"] = result["company"]["size"]["name"]
                            # 学历要求
                            # info["edu_level_code"] = result["eduLevel"]["code"]
                            info["edu_level_name"] = result["eduLevel"]["name"]
                            info["emplType"] = result["emplType"]
                            info["jobname"] = result["jobName"].lower()
                            # info["jobTag"] = result["jobTag"]["searchTag"]
                            # info["jobType"] = result["jobType"]["display"]
                            info["salary"] = result["salary"]
                            info["updateDate"] = result["updateDate"]
                            info["url"] = result["positionURL"]
                            info["welfare"] = ",".join(result["welfare"])
                            try:
                                # info["workingExp_code"] = result["workingExp"]["code"]
                                info["workingExp_name"] = result["workingExp"]["name"]
                            except Exception as e:
                                print("出错判断：KeyError: 'code'")
                                print(e)
                            info["job_id"] = result["number"]
                            info["kw"] = kw
                            # print("单条数据：",info)
                            self.job_info.append(info)
                            # print("多条数据：",self.job_info)
                            # os._exit(0)
                            if len(self.job_info) > 3999:
                                try:
                                    conn = hu_utils.open_line_db()
                                    hu_utils.insert_update_many(conn, self.job_info, "zhilian_job")
                                    self.job_info.clear()
                                except:
                                    print("数据库操作失败")
                        print("未存储数据条数：{}".format(len(self.job_info)))
        try:
            conn = hu_utils.open_line_db()
            hu_utils.insert_update_many(conn, self.job_info, "zhilian_job")
            self.job_info.clear()
        except:
            print("数据库操作失败")

    def main(self):
        self.get_info()


if __name__ == '__main__':
    start_time = time.time()
    zhilian = zhilian_info()
    zhilian.main()
    end_time = time.time()
    run_time = int(end_time - start_time)
    print("爬虫一共运行时间：{}分钟".format(run_time//60))
