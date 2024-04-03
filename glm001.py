import os
from zhipuai import ZhipuAI

# 从环境变量中获取ZHIPU_API_KEY的值
apikey = os.environ.get("ZHIPU_API_KEY")


client = ZhipuAI(api_key=apikey) # 填写您自己的APIKey

response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的slogan"},
        {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
        {"role": "user", "content": "智谱AI开放平台"},
        {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
        {"role": "user", "content": "创造一个更精准、吸引人的slogan"}
    ],
)
print(response.choices[0].message)



# response = client.chat.asyncCompletions.create(
#     model="glm-4",  # 填写需要调用的模型名称
#     messages=[
#         {
#             "role": "user",
#             "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"
#         }
#     ],
# )
# print(response)


# response = client.chat.completions.create(
#     model="glm-4v",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "图里有几个人，他们可能要去哪里"
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": "https://ts1.cn.mm.bing.net/th/id/R-C.3997eb10814025183c8fbbc6b5373713?rik=fSPsSA1rrKXAzw&riu=http%3a%2f%2fdpic.tiankong.com%2fau%2fpw%2fQJ6612208802.jpg&ehk=c%2f0WAvYPgW2uwrHdpUenuYb4L%2f0oQkiOmmJoSawaX4A%3d&risl=&pid=ImgRaw&r=0"
#                     }
#                 }
#             ]
#         }
#     ],
# )
# print(response.choices[0].message)

# response = client.images.generations(
#     model="cogview-3", #填写需要调用的模型名称
#     prompt="一艘飞船正在以0.1倍光速度穿在宇宙中穿梭，科幻画风格",
# )
# print(response.data[0].url)