# 重庆共青团微信公众号（青年大学习板块）API

## 获取用户信息
根据 `openid` 获取用户信息。

**请求URL：**
```
http://qndxx.cqyouths.com/api/user/userInfo?openid={}
```

**返回格式：**

```json
{
    "status": "HTTP状态码（如200表示成功）",
    "message": "响应消息（如果没有特别的消息，则为空字符串）",
    "error": "错误信息（如果没有错误，则为空字符串）",
    "data": {
        "id": "用户的唯一标识符",
        "openid": "用户的OpenID标识符",
        "username": "用户名",
        "avatar": "用户头像链接",
        "mobile": "用户手机号",
        "real_name": "用户的真实姓名",
        "league_id": "用户所属组织的主要标识符",
        "league_id1": "组织层级1的标识符",
        "league_id2": "组织层级2的标识符",
        "league_id3": "组织层级3的标识符",
        "league_id4": "组织层级4的标识符",
        "league_id5": "组织层级5的标识符",
        "league_id6": "组织层级6的标识符",
        "league_name": "用户所属组织的完整名称",
        "is_teacher": "标记用户是否为教师（0否，1是）",
        "school": "用户所属学校（如果有的话，否则为null）",
        "introduce": "用户介绍（如果有的话，否则为null）",
        "sex": "用户性别（例如1代表男性，2代表女性）",
        "province": "用户所在省份（如果有的话，否则为null）",
        "city": "用户所在城市（如果有的话，否则为null）",
        "area": "用户所在区域（如果有的话，否则为null）",
        "address": "用户地址",
        "age": "用户年龄",
        "score": "用户的分数",
        "study_course_number": "用户学习的课程数量",
        "last_login_at": "上次登录时间（如果有的话，否则为null）",
        "login_times": "登录次数",
        "status": "用户状态标识符",
        "created_at": "用户账户的创建时间",
        "updated_at": "用户账户的最后更新时间",
        "old_openid": "用户的旧OpenID（如果有的话，否则为null）",
        "league": {
            "id": "组织的唯一标识符",
            "level": "组织的层级",
            "name1": "组织层级1的名称",
            "name2": "组织层级2的名称",
            "total_user_number": "组织的用户总数",
            "name3": "组织层级3的名称",
            "name4": "组织层级4的名称",
            "name5": "组织层级5的名称",
            "name6": "组织层级6的名称",
            "status": "组织的状态",
            "sequence": "组织的序列号",
            "parent_id": "上级组织的标识符",
            "next_count": "下一级组织的数量"
        },
        "leagueData": [
            {
                "id": "组织层级的唯一标识符",
                "name": "组织层级的名称"
            }
            // ... 其他组织层级数据
        ],
        "lottery_draw_score": "抽奖所需的分数",
        "user_league_name": {
            // 这个对象与上面的 'league' 对象结构相同
            "id": "组织的唯一标识符",
            // ... 其他与 'league' 相同的字段
        }
    }
}
```

## 获取当前最新课程信息
指定当前 timestamp，获取当前最新的课程信息。

**请求URL：**
```
http://qndxx.cqyouths.com/new_course.json?time={}
```

**返回格式：**

```json
{
    "data": [
        {
            "id": "课程的唯一标识符",
            "name": "课程名称",
            "season_id": "季节的标识符",
            "period_id": "时间段的标识符",
            "score": "课程分数或评分",
            "type": "课程类型标识符",
            "admin_id": "管理员或创建者的标识符",
            "sort": "排序或分类的标记（如果有的话，否则为null）",
            "study_number": "学习该课程的用户数",
            "cover": "课程封面图片链接（如果有的话，否则为空字符串）",
            "link": "课程相关链接",
            "status": "课程的状态标识符",
            "publish_time": "课程发布时间",
            "is_study": "标记用户是否已学习（例如0表示未学习，1表示已学习）",
            "created_at": "课程创建时间",
            "updated_at": "课程最后更新时间"
        }
    ]
}
```

## 学习课程
指定 `课程id` 来学习课程。

**请求URL：**
```
http://qndxx.cqyouths.com/api/course/studyCourse?openid={}&id={}
```

**返回格式：**

```json
{
    "status": "HTTP状态码（如200表示成功）",
    "message": "响应消息（如'增加学习记录成功'）",
    "error": "错误信息（如果没有错误，则为空字符串）",
    "data": {
        "user_id": "用户标识符",
        "course_id": "课程标识符",
        "flag": "标志位，表示特定状态或类型",
        "updated_at": "记录的最后更新时间",
        "created_at": "记录的创建时间",
        "id": "学习记录的唯一标识符",
        "user_score": "用户当前的分数"
    }
}	
```

## 获取所有课程信息
获取所有课程的信息，支持分页显示。

**请求URL：**
```
http://qndxx.cqyouths.com/api/user/studyCourseList?openid={}&status={}&page={}&page_size={}
```

**参数含义：**
- `openid`: 指定用户
- `status`: 视频学习状态，1=已学习，2=已补学，3=未学习
- `page`: 分页显示相关，默认值为1
- `page_size`: 分页显示相关，默认值为10

**返回格式：**

```json
{
    "status": "HTTP状态码（如200表示成功）",
    "message": "响应消息（如'查询成功'）",
    "error": "错误信息（如果没有错误，则为空字符串）",
    "data": {
        "current_page": "当前页码",
        "data": [
            {
                "id": "唯一标识符",
                "user_id": "用户标识符",
                "course_id": "课程标识符",
                "flag": "标志位",
                "updated_at": "最后更新时间",
                "created_at": "创建时间",
                "name": "课程名称",
                "link": "课程链接",
                "publish_time": "发布时间",
                "finish_time": "完成时间",
                "study_status": "学习状态"
            },
            // ... 其他课程信息，每个课程都有类似的结构
        ],
        "first_page_url": "第一页的URL",
        "from": "当前显示的记录开始序号",
        "last_page": "最后一页的页码",
        "last_page_url": "最后一页的URL",
        "next_page_url": "下一页的URL",
        "path": "API路径",
        "per_page": "每页显示的记录数",
        "prev_page_url": "上一页的URL",
        "to": "当前显示的记录结束序号",
        "total": "总记录数"
    }
}
```



docker run -d -e OPENID='o1Nb9ji2aXFB1BotaN0ByDeU5Ig8' -e CRON_TIME='0 9 * * 2' my-qndxx-app
