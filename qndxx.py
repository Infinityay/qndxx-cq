# -*- coding: utf-8 -*-
# @Project : YouthStudy-qndxx-Chongqing
# @Time    : 2024/1/14 16:29
# @Author  : infinityay
# @File    : qndxx.py
# @Software: PyCharm 
# @Contact me: https://github.com/Infinityay or stu.lyh@outlook.com
# @Comment :
import os
import random
import time
from datetime import datetime
import requests
import logging

# 配置日志
log_filename = "qndxx.log"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=log_filename,
                    filemode='a')
logger = logging.getLogger(__name__)

# 基础URL
BASE_URL = "http://qndxx.cqyouths.com"


def get_latest_course():
    """获取当前最新课程ID"""
    timestamp = datetime.now().timestamp()
    url = f"{BASE_URL}/new_course.json?time={timestamp}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data and "data" in data and len(data["data"]) > 0:
                latest_course = data["data"][0]
                return latest_course["id"], latest_course["name"], latest_course["publish_time"]
        logger.warning("获取课程失败，或者没有新课程可供获取。")
    except Exception as e:
        logger.error("请求课程数据时出错: %s", e)
    return None


def study_course(openid, course_id):
    """学习指定的课程"""
    try:
        url = f"{BASE_URL}/api/course/studyCourse?openid={openid}&id={course_id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data["status"] == 200:
                return True
            else:
                err_msg = data["message"]
                logger.warning(f"{err_msg}")
        else:
            logger.warning("学习课程失败，响应码：%d", response.status_code)
    except Exception as e:
        logger.error("请求学习课程时出错: %s", e)
    return False


openid = "o1Nb9ji2aXFB1BotaN0ByDeU5Ig8"
# 添加随机延迟5min范围
random_delay = random.randint(0, 3)  # 单位是秒
time.sleep(random_delay)

logger.info("====================开始学习课程脚本=====================")
latest_course_info = get_latest_course()
if latest_course_info:
    latest_course_id, latest_course_name, latest_course_publish_time = latest_course_info
    logger.info("====================最新课程消息已成功获取=====================")
    if study_course(openid, latest_course_id):
        logger.info(f"成功学习课程《{latest_course_name}》, 该课程发布时间为 {latest_course_publish_time}")
    else:
        logger.warning(f"学习课程《{latest_course_name}》失败, 该课程发布时间为 {latest_course_publish_time}")

else:
    logger.warning("没有获取到最新课程信息。")

logger.info("====================结束脚本=====================")
