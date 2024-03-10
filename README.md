# langchain-wechat

基于fastapi + langchain + itchat 搭建的微信聊天机器人
灵感来自于 chatgpt-on-wechat 项目

## 环境搭建

python >= 3.10

```shell
poetry install
```

或者

```shell
pip install -r requirements.txt
```

## 运行

```shell
uvicorn src.main:app
```

## 功能

- 单人消息发送回复
- ...

### 支持的模型

- openai
