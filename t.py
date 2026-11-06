
import os
import requests
from openai import OpenAI

# ========== 第1步：用 uapis.cn 获取长春实时天气 ==========
url = "https://uapis.cn/api/v1/misc/weather"
headers = {"Authorization": "uapi-7jizkuwt6nIQnICSO3isqURwI2HVHkC3E4KydsIY"}
# 可选参数 extended=true 可额外返回体感温度、能见度、气压、空气质量等字段
params = {"city": "长春", "extended": "true"}

resp = requests.get(url, headers=headers, params=params, timeout=10)
resp.raise_for_status()  # 非 200 状态码会直接抛异常，避免把错误数据交给模型
data = resp.json()

# ========== 第2步：从返回的 JSON 中提取关键天气字段 ==========
# uapis.cn 返回的字段名见文档：weather, temperature, wind_direction,
# wind_power, humidity, report_time 等（见文档第22-25行）[reference:0]
weather_text = f"""
长春实时天气（数据来源：uapis.cn，更新时间：{data.get('report_time', '未知')}）：
- 天气状况：{data.get('weather', '未知')}
- 当前温度：{data.get('temperature', '未知')}℃
- 风向：{data.get('wind_direction', '未知')}
- 风力：{data.get('wind_power', '未知')}
- 相对湿度：{data.get('humidity', '未知')}%
"""

# 如果请求了 extended=true，下面这些字段可能也存在
if data.get("feels_like") is not None:
    weather_text += f"- 体感温度：{data['feels_like']}℃\n"
if data.get("visibility") is not None:
    weather_text += f"- 能见度：{data['visibility']} km\n"
if data.get("aqi") is not None:
    weather_text += f"- 空气质量指数（AQI）：{data['aqi']}\n"

# ========== 第3步：把天气数据交给 DeepSeek 生成自然语言回答 ==========
client = OpenAI(
    api_key='sk-3a7a7c5cc04a4dffbfbdd47c94c1cf89',
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {
            "role": "system",
            "content": "你是一个乐于助人的天气播报助手，请根据提供的实时天气数据，用简洁、自然的口语回答用户。",
        },
        {
            "role": "user",
            "content": f"用户问：今天长春绿园区天气如何？\n\n以下是实时天气数据，请据此回答：\n{weather_text}",
        },
    ],
    stream=False,
)

print(response.choices[0].message.content)