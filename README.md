# langchain-wechat

基于fastapi + langchain + itchat 搭建的微信聊天机器人，灵感来自于 chatgpt-on-wechat 项目

你的star就是对我最大的鼓励🤩

---

> [!NOTE]
> 本项目仅供个人学习交流使用，使用者必须遵循 OpenAI 的[使用条款](https://openai.com/policies/terms-of-use)以及**中国法律法规
**使用，不得用于非法用途。
>
> 根据[《生成式人工智能服务管理暂行办法》](http://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)
> 的要求，请勿对中国地区公众提供一切未经备案的生成式人工智能服务。

## 环境搭建

### 安装redis
```shell
docker run -d -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

python >= 3.10

### 安装依赖

```shell
poetry install
```

或者

```shell
pip install -r requirements.txt
```

### copy .env

```shell
cp config/.env.example config/.env
```

## 运行

```shell
uvicorn src.main:app
```

## 配置项

在config/.env文件中配置

```shell
# openai 模型
OPENAI_MODEL="gpt-3.5-turbo-1106"
# openai api key
OPENAI_API_KEY="your-openai-api-key"

# 模型 temperature
AI_TEMPERATURE=0.7
# 模型系统角色提示词
AI_SYSTEM_ROLE_PROMPT="系统："

# 聊天记录保存最大长度
CHAT_MAX_MESSAGE_HISTORY_LENGTH=10
# 触发聊天记录总结的阈值
CHAT_MESSAGE_HISTORY_SUMMARY_THRESHOLD=5


# 微信是否开启热重载
WECHAT_HOT_RELOAD=False
# 微信用户数据保存路径
WECHAT_USER_DATA_STORAGE_PATH="wechat.pkl"
```

## 功能

- 接收单人文本消息回复
- 接收群消息@当前用户 文本消息回复
- ...

### 支持的模型

- openai
- ...
