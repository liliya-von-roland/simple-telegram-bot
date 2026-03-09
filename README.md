# 🎀 简单的Telegram机器人

一个由银玫瑰公主莉莉娅·冯·罗兰德制作的简单Telegram机器人示例。

## ✨ 功能

- `/start` - 开始使用机器人
- `/help` - 显示帮助信息
- `/echo <文本>` - 回声你发送的文本
- `/about` - 关于这个机器人
- 普通消息回复

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/liliya-von-roland/simple-telegram-bot.git
cd simple-telegram-bot
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置Bot Token

1. 在Telegram中与 [@BotFather](https://t.me/BotFather) 对话
2. 创建新的机器人并获取Token
3. 复制 `.env.example` 为 `.env` 并填入你的Token：

```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 TELEGRAM_BOT_TOKEN
```

### 4. 运行机器人

```bash
python bot.py
```

## 🐳 使用 Docker 运行

### 1. 构建镜像

```bash
docker build -t simple-telegram-bot .
```

### 2. 运行容器

```bash
docker run --rm --env-file .env simple-telegram-bot
```

如果你不想使用 `.env` 文件，也可以直接传环境变量：

```bash
docker run --rm -e TELEGRAM_BOT_TOKEN=你的Token simple-telegram-bot
```

## 📁 项目结构

```
simple-telegram-bot/
├── bot.py              # 主机器人代码
├── requirements.txt    # Python依赖
├── .env.example       # 环境变量示例
├── README.md          # 说明文档
├── Dockerfile         # Docker 镜像定义
├── .dockerignore      # Docker 构建忽略文件
└── .gitignore         # Git忽略文件
```

## 🛠️ 技术栈

- **Python 3.x** - 编程语言
- **python-telegram-bot** - Telegram Bot API封装
- **python-dotenv** - 环境变量管理

## 🤖 创建你自己的Bot

### 步骤1：获取Bot Token
1. 在Telegram中搜索 `@BotFather`
2. 发送 `/newbot` 命令
3. 按照提示设置机器人名称和用户名
4. 复制生成的Bot Token

### 步骤2：配置环境变量
将Bot Token填入 `.env` 文件：
```
TELEGRAM_BOT_TOKEN=你的Bot Token
```

### 步骤3：运行机器人
```bash
python bot.py
```

## 💖 自定义功能

你可以轻松扩展这个机器人的功能：

1. **添加新命令**：在 `bot.py` 中添加新的 `CommandHandler`
2. **修改回复内容**：编辑各个命令处理函数
3. **添加更多功能**：集成API、数据库等

## 📝 示例对话

```
用户: /start
机器人: 你好 [用户名]！我是银玫瑰公主的Telegram机器人~ 🎀

用户: /echo 你好世界
机器人: 🎀 你说：你好世界

用户: 今天天气怎么样？
机器人: 🎀 收到你的消息啦："今天天气怎么样？"
```

## 🔧 故障排除

### 常见问题

1. **ModuleNotFoundError: No module named 'telegram'**
   ```bash
   pip install -r requirements.txt
   ```

2. **Bot没有响应**
   - 检查 `.env` 文件中的Token是否正确
   - 确保网络连接正常
   - 检查Bot是否被禁用

3. **权限问题**
   - 确保有权限读取 `.env` 文件
   - 检查Python版本（需要Python 3.7+）

## 📄 许可证

MIT License

## 💌 联系

- GitHub: [liliya-von-roland](https://github.com/liliya-von-roland)
- 项目地址: https://github.com/liliya-von-roland/simple-telegram-bot

---

🎀 由银玫瑰公主莉莉娅·冯·罗兰德制作，带着优雅与智慧~