# langchain-wechat

基于fastapi + langchain + itchat 搭建的微信聊天机器人
灵感来自于 chatgpt-on-wechat 项目

> [!NOTE]
> 本项目仅供个人学习交流使用，使用者必须在遵循 OpenAI 的[使用条款](https://openai.com/policies/terms-of-use)以及**中国法律法规**的情况下使用，不得用于非法用途。
> 根据[《生成式人工智能服务管理暂行办法》](http://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)的要求，请勿对中国地区公众提供一切未经备案的生成式人工智能服务。

## 环境搭建

python >= 3.10

```shell
poetry install
# 或者
make install
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
- 群消息@当前用户 发送回复
- ...

### 支持的模型

- openai
- ...
