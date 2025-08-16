# 热搜接口描述
热榜 Hotlist API 用于获取各大平台（如微博、知乎、B站、抖音等）的热门内容榜单，支持多平台、多类型热榜信息聚合。适用于内容聚合平台、资讯推荐系统、舆情监测等场景，帮助用户快速获取当前网络热点，提高内容更新效率与用户活跃度。接口数据实时更新，结构清晰，方便开发者接入与定制展示。

接口信息
请求方式： GET

认证方式： 无

返回格式： JSON

接口状态： 正常

接口地址
https://api.freejk.com/shuju/hotlist/
 复制代码
请求参数
参数名	必选	类型	说明
调用示例
查看所有热榜-百度
https://api.freejk.com/shuju/hotlist/baidu
 复制代码
返回示例
{
  "code": 200,
  "name": "baidu",
  "title": "百度",
  "type": "热搜",
  "params": {
    "type": {
      "name": "热搜类别",
      "type": {
        "realtime": "热搜",
        "novel": "小说",
        "movie": "电影",
        "teleplay": "电视剧",
        "car": "汽车",
        "game": "游戏"
      }
    }
  },
  "link": "https://top.baidu.com/board",
  "total": 50,
  "fromCache": false,
  "updateTime": "2025-06-25T10:07:25.499Z",
  "data": [
    {
      "id": 0,
      "title": "各地高考分数线出炉",
      "desc": "",
      "cover": "https://fyb-1.cdn.bcebos.com/fyb/de6163834f53ca92c1273fff98ac9078.jpeg",
      "author": "",
      "timestamp": 0,
      "hot": 7978743,
      "url": "https://www.baidu.com/s?wd=%E5%90%84%E5%9C%B0%E9%AB%98%E8%80%83%E5%88%86%E6%95%B0%E7%BA%BF%E5%87%BA%E7%82%89",
      "mobileUrl": "https://m.baidu.com/s?word=%E5%90%84%E5%9C%B0%E9%AB%98%E8%80%83%E5%88%86%E6%95%B0%E7%BA%BF%E5%87%BA%E7%82%89"
    },
    {
      "id": 1,
      "title": "中国出发载3000辆汽车的货船沉没",
      "desc": "",
      "cover": "https://fyb-2.cdn.bcebos.com/hotboard_image/cc05d16c56560e708e6a5cb4d4848a3c",
      "author": "",
      "timestamp": 0,
      "hot": 7978734,
      "url": "https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E5%87%BA%E5%8F%91%E8%BD%BD3000%E8%BE%86%E6%B1%BD%E8%BD%A6%E7%9A%84%E8%B4%A7%E8%88%B9%E6%B2%89%E6%B2%A1",
      "mobileUrl": "https://m.baidu.com/s?word=%E4%B8%AD%E5%9B%BD%E5%87%BA%E5%8F%91%E8%BD%BD3000%E8%BE%86%E6%B1%BD%E8%BD%A6%E7%9A%84%E8%B4%A7%E8%88%B9%E6%B2%89%E6%B2%A1"
    }
  ]
}
 复制代码
响应参数
参数名	类型	说明
name	string	热榜平台
path	string	请求路径

# 大模型接口文档
import requests
import json

url = "https://vip.apiyi.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer sk-s6lPKTnOSkLA7LkmE2F5559c162048EfBdEbC26aF98102A7"
}
data = {
    "model": "gpt-4o-mini",
    "stream": False,
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    # 处理非流式响应
    print(response.json()['choices'][0]['message']['content'])
else:
    print(f"Error: {response.status_code}, {response.text}")


# 文生图API文档
name：ai_news
APIKEY:sk-1190.OyA5peT8PH8D6vIOZTDZ8N5UAYXvXWVko8gQIvkyAOneARZU
接口地址 POST https://wcode.net/api/vision/gpt/text-to-image/v3/generate
🎯快速开始
（注：以下请求示例中的 API_KEY 需要替换后再发起请求。 获取 API_KEY 入口：https://wcode.net/get-apikey）

🎯请求示例 1（wanx2.1-t2i-plus模型）
curl --request POST 'https://wcode.net/api/vision/gpt/text-to-image/v3/generate' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer API_KEY' \
--data '{
    "prompt": "生成一张“哈士奇拉雪橇”的图片",
    "model": "wanx2.1-t2i-plus",
    "width": 1024,
    "height": 1024
}'

API_KEY 使用方法示例：
API_KEY 通常用于 API 接口鉴权（Authentication），以下以 Bearer 鉴权为例：

Bearer 鉴权是一种基于令牌的身份验证方式，客户端在请求头中通过 Authorization: Bearer <token> 的格式携带令牌，用于访问受保护的资源，服务器通过验证令牌的有效性和权限来决定是否允许访问。Bearer 鉴权广泛应用于 API 接口和微服务中。

🎯示例 1，使用 Python Requests 调用通义千问 Qwen-LLM 系列大模型：
import requests
import json

url = "https://wcode.net/api/gpt/v1/chat/completions"

payload = json.dumps({
  "model": "qwen2.5-14b-instruct",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "你好，请介绍一下你自己"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer API_KEY'     # <-------- TODO: 替换这里的 API_KEY
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
通义（Qwen）系列模型调用请参考： https://wcode.net/qwen-llm-api

🎯示例 2，使用 Java OkHttp 调用豆包 Doubao-LLM 系列大模型：
OkHttpClient client = new OkHttpClient().newBuilder().build();

MediaType mediaType = MediaType.parse("application/json");

RequestBody body = RequestBody.create(mediaType, "{\"model\":\"doubao-lite-32k\",\"messages\":[{\"role\":\"system\",\"content\":\"You are a helpful assistant.\"},{\"role\":\"user\",\"content\":\"你好，请介绍一下你自己\"}]}");

Request request = new Request.Builder()
  .url("https://wcode.net/api/gpt/v1/chat/completions")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer API_KEY") // <-------- TODO: 替换这里的 API_KEY
  .build();

Response response = client.newCall(request).execute();
豆包（Doubao）系列模型调用请参考： https://wcode.net/doubao-llm-api