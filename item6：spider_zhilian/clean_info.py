# -*- coding:utf-8 -*-
# author:吉祥鸟
# datetime:2019/3/19 0019 下午 3:57
# software: PyCharm
import hu_utils
from pprint import pprint


def clean_salary():
    salary_info_z = []
    sql = "select job_id,salary from zhilian_job where salary_code is null"
    conn = hu_utils.open_line_db()
    salary_infos = hu_utils.select_one(conn, sql)
    print(len(salary_infos))
    for salary_info in salary_infos:
        # print(salary_info)
        if salary_info["salary"] == "薪资面议" or salary_info["salary"] == "校招":
            salary_info["salary_code"] = -1
            salary_info_z.append(salary_info)
            continue
        if salary_info["salary"] == "1K以下":
            salary_info["salary_code"] = 105
            salary_info_z.append(salary_info)
            continue
        salary = salary_info["salary"].replace("K", "").split("-")
        salary_mid = (float(salary[0]) + float(salary[1])) // 2
        # print(salary_mid)
        if salary_info["salary"] == "1K以下" or salary_mid <= 5:
            salary_info["salary_code"] = 105
            salary_info_z.append(salary_info)
            continue
        if salary_mid <= 10:
            salary_info["salary_code"] = 510
            salary_info_z.append(salary_info)
            continue
        if salary_mid <= 15:
            salary_info["salary_code"] = 1015
            salary_info_z.append(salary_info)
            continue
        if salary_mid <= 20:
            salary_info["salary_code"] = 1520
            salary_info_z.append(salary_info)
            continue
        if salary_mid <= 25:
            salary_info["salary_code"] = 2025
            salary_info_z.append(salary_info)
            continue
        if salary_mid <= 30:
            salary_info["salary_code"] = 2530
            salary_info_z.append(salary_info)
            continue
        if salary_mid <= 35:
            salary_info["salary_code"] = 3035
            salary_info_z.append(salary_info)
            continue
        if salary_mid <= 40:
            salary_info["salary_code"] = 3540
            salary_info_z.append(salary_info)
            continue
        else:
            salary_info["salary_code"] = 4099
            salary_info_z.append(salary_info)
            continue
        # print(salary_info["salary_code"])
        # print("--------------")
    # pprint(salary_info_z)
    conn = hu_utils.open_line_db()
    hu_utils.insert_update_many(conn, salary_info_z, "zhilian_job")


def clean_jobname():
    job_name_infos = []
    sql = "select job_id,jobname from zhilian_job"
    conn = hu_utils.open_line_db()
    jobname_infos = hu_utils.select_one(conn, sql)
    print(jobname_infos)
    for jobname_info in jobname_infos:
        jobname_info["jobname"] = jobname_info["jobname"].lower()
        job_name_infos.append(jobname_info)
    conn = hu_utils.open_line_db()
    hu_utils.insert_update_many(conn, job_name_infos, "zhilian_job")


if __name__ == '__main__':
    clean_salary()
