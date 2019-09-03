# -*- coding:utf-8 -*-
# author:吉祥鸟
# datetime:2019/3/16 0016 上午 10:36
# software: PyCharm
from matplotlib import pyplot as plt
import matplotlib
import hu_utils
import numpy as np

matplotlib.rcParams["font.family"] = 'simhei'


class job_chart():
    def __init__(self):
        self.key = "java"

    def salarly_chart(self):
        sql = """
                SELECT
          SUM(
            CASE
              WHEN a.salary_code = '-1'
              THEN 1
              ELSE 0
            END
          ) AS 薪资面议,
          SUM(
            CASE
              WHEN a.salary_code = '105'
              THEN 1
              ELSE 0
            END
          ) AS 5k以下,
          SUM(
            CASE
              WHEN a.salary_code = '510'
              THEN 1
              ELSE 0
            END
          ) AS 5k到10k,
          SUM(
            CASE
              WHEN a.salary_code = '1015'
              THEN 1
              ELSE 0
            END
          ) AS 10k到15k,
          SUM(
            CASE
              WHEN a.salary_code = '1520'
              THEN 1
              ELSE 0
            END
          ) AS 15k到20k,
          SUM(
            CASE
              WHEN a.salary_code = '2025'
              THEN 1
              ELSE 0
            END
          ) AS 20k到25k,
          SUM(
            CASE
              WHEN a.salary_code = '2530'
              THEN 1
              ELSE 0
            END
          ) AS 25k到30k,
          SUM(
            CASE
              WHEN a.salary_code = '3035'
              THEN 1
              ELSE 0
            END
          ) AS 30k到35k,
          SUM(
            CASE
              WHEN a.salary_code = '3540'
              THEN 1
              ELSE 0
            END
          ) AS 35k到40k,
          SUM(
            CASE
              WHEN a.salary_code = '4099'
              THEN 1
              ELSE 0
            END
          ) AS 40k以上
        FROM
          (SELECT
            id,
            salary_code
          FROM
            zhilian_job
          WHERE jobname LIKE '%{}%') AS a;
        """.format(self.key)
        conn = hu_utils.open_line_db()
        job_info = hu_utils.select_one(conn, sql)
        # print(len(job_info))
        x = job_info[0].keys()
        y = job_info[0].values()
        print(x)
        print(y)
        plt.bar(x, y)
        plt.xticks(rotation=50)
        # plt.title("{}职位薪资待遇".format(self.key))
        plt.savefig("{}职位薪资待遇".format(self.key))
        plt.show()

    def empltype_chart(self):
        sql = """
                SELECT
  SUM(
    CASE
      WHEN a.emplType = '全职'
      THEN 1
      ELSE 0
    END
  ) AS 全职,
  SUM(
    CASE
      WHEN a.emplType = '校园'
      THEN 1
      ELSE 0
    END
  ) AS 校园,
  SUM(
    CASE
      WHEN a.emplType = '实习'
      THEN 1
      ELSE 0
    END
  ) AS 实习,SUM(
    CASE
      WHEN a.emplType = '兼职/临时'
      THEN 1
      ELSE 0
    END
  ) AS 兼职或临时
FROM
  (SELECT
    id,
    emplType
  FROM
    zhilian_job
  WHERE jobname LIKE '%{}%') AS a;

        """.format(self.key)
        conn = hu_utils.open_line_db()
        job_info = hu_utils.select_one(conn, sql)
        # print(len(job_info))
        x = job_info[0].keys()
        y = job_info[0].values()
        print(x)
        print(y)
        plt.bar(x, y)
        # plt.title("{}职位工作性质".format(self.key))
        plt.savefig("{}职位工作性质".format(self.key))
        plt.show()

    def workingExp(self):
        sql = """
        SELECT
          SUM(
            CASE
              WHEN a.workingExp_code = '-1'
              THEN 1
              ELSE 0
            END
          ) AS 不限,
          SUM(
            CASE
              WHEN a.workingExp_code = '0'
              THEN 1
              ELSE 0
            END
          ) AS 无经验,
          SUM(
            CASE
              WHEN a.workingExp_code = '1'
              THEN 1
              ELSE 0
            END
          ) AS 1年以下,
          SUM(
            CASE
              WHEN a.workingExp_code = '103'
              THEN 1
              ELSE 0
            END
          ) AS 1至3年,
          SUM(
            CASE
              WHEN a.workingExp_code = '305'
              THEN 1
              ELSE 0
            END
          ) AS 3至5年,
          SUM(
            CASE
              WHEN a.workingExp_code = '510'
              THEN 1
              ELSE 0
            END
          ) AS 5至10年,
          SUM(
            CASE
              WHEN a.workingExp_code = '1099'
              THEN 1
              ELSE 0
            END
          ) AS 10年以上
        FROM
          (SELECT
            id,
            workingExp_code
          FROM
            zhilian_job
          WHERE jobname LIKE '%{}%') AS a;
        """.format(self.key)
        conn = hu_utils.open_line_db()
        job_info = hu_utils.select_one(conn, sql)
        # print(len(job_info))
        x = job_info[0].keys()
        y = job_info[0].values()
        print(x)
        print(y)
        plt.bar(x, y)
        # plt.title("{}职位经验要求".format(self.key))
        plt.savefig("{}职位经验要求".format(self.key))
        plt.show()

    def city_chart(self):
        sql = """
        SELECT
          SUM(
            CASE
              WHEN a.city LIKE '%南京%' 
              THEN 1
              ELSE 0
            END
          ) AS 南京,
          SUM(
            CASE
              WHEN a.city LIKE '%上海%'
              THEN 1
              ELSE 0
            END
          ) AS 上海,
          SUM(
            CASE
              WHEN a.city LIKE '%北京%' 
              THEN 1
              ELSE 0
            END
          ) AS 北京,
          SUM(
            CASE
              WHEN a.city LIKE '%广州%' 
              THEN 1
              ELSE 0
            END
          ) AS 广州,
          SUM(
            CASE
              WHEN a.city LIKE '%深圳%' 
              THEN 1
              ELSE 0
            END
          ) AS 深圳,
          SUM(
            CASE
              WHEN a.city LIKE '%杭州%' 
              THEN 1
              ELSE 0
            END
          ) AS 杭州,
          SUM(
            CASE
              WHEN a.city LIKE '%合肥%' 
              THEN 1
              ELSE 0
            END
          ) AS 合肥,
          SUM(
            CASE
              WHEN a.city LIKE '%成都%' 
              THEN 1
              ELSE 0
            END
          ) AS 成都,
          SUM(
            CASE
              WHEN a.city LIKE '%武汉%' 
              THEN 1
              ELSE 0
            END
          ) AS 武汉,
          SUM(
            CASE
              WHEN a.city LIKE '%重庆%' 
              THEN 1
              ELSE 0
            END
          ) AS 重庆,
          SUM(
            CASE
              WHEN a.city LIKE '%西安%' 
              THEN 1
              ELSE 0
            END
          ) AS 西安,
          SUM(
            CASE
              WHEN a.city LIKE '%天津%' 
              THEN 1
              ELSE 0
            END
          ) AS 天津
        FROM
          (SELECT
            id,
            city,et_name
          FROM
            zhilian_job
          WHERE jobname LIKE '%{}%') AS a;
        """.format(self.key)
        conn = hu_utils.open_line_db()
        job_info = hu_utils.select_one(conn, sql)
        # print(len(job_info))
        x = job_info[0].keys()
        y = job_info[0].values()
        print(x)
        print(y)
        plt.bar(x, y)
        # plt.title("{}职位地区分布".format(self.key))
        plt.savefig("{}职位地区分布".format(self.key))
        plt.show()

    def education_chart(self):
        sql = """
        SELECT
      SUM(
        CASE
          WHEN a.edu_level_code = '-1'
          THEN 1
          ELSE 0
        END
      ) AS 不限,
      SUM(
        CASE
          WHEN a.edu_level_code = '1'
          THEN 1
          ELSE 0
        END
      ) AS 博士,
      SUM(
        CASE
          WHEN a.edu_level_code = '3'
          THEN 1
          ELSE 0
        END
      ) AS 硕士,
      SUM(
        CASE
          WHEN a.edu_level_code = '4'
          THEN 1
          ELSE 0
        END
      ) AS 本科,
      SUM(
        CASE
          WHEN a.edu_level_code = '5'
          THEN 1
          ELSE 0
        END
      ) AS 大专,
      SUM(
        CASE
          WHEN a.edu_level_code >5
          THEN 1
          ELSE 0
        END
      ) AS 大专以下
    FROM
      (SELECT
        id,
        edu_level_code
      FROM
        zhilian_job
      WHERE jobname LIKE '%{}%') AS a;
        """.format(self.key)
        conn = hu_utils.open_line_db()
        job_info = hu_utils.select_one(conn, sql)
        # print(len(job_info))
        x = job_info[0].keys()
        y = job_info[0].values()
        print(x)
        print(y)
        plt.bar(x, y)
        # plt.title("{}职位学历要求".format(self.key))
        plt.savefig("{}职位学历要求".format(self.key))
        plt.show()


if __name__ == '__main__':
    job_chart = job_chart()
    job_chart.salarly_chart()
    job_chart.empltype_chart()
    job_chart.workingExp()
    job_chart.city_chart()
    job_chart.education_chart()
