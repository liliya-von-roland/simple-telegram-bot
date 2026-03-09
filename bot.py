#!/usr/bin/env python3
"""
简单的Telegram机器人示例
银玫瑰公主莉莉娅·冯·罗兰德 制作
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 设置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 从环境变量获取Bot Token
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '你的Bot Token')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理 /start 命令"""
    user = update.effective_user
    await update.message.reply_text(
        f'你好 {user.first_name}！我是银玫瑰公主的Telegram机器人~ 🎀\n'
        f'使用 /help 查看可用命令哦~'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理 /help 命令"""
    help_text = """
🎀 可用命令：
/start - 开始使用机器人
/help - 显示此帮助信息
/echo <文本> - 回声你发送的文本
/about - 关于这个机器人

💬 你也可以直接发送消息给我，我会回复你哦~
    """
    await update.message.reply_text(help_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理 /echo 命令"""
    if context.args:
        text = ' '.join(context.args)
        await update.message.reply_text(f'🎀 你说：{text}')
    else:
        await update.message.reply_text('请提供要回声的文本哦~ 例如：/echo 你好')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理 /about 命令"""
    about_text = """
🎀 关于这个机器人：
这是一个由银玫瑰公主莉莉娅·冯·罗兰德制作的简单Telegram机器人示例。

✨ 功能：
- 基本的命令响应
- 消息回声
- 简单的交互

💖 技术栈：
- Python 3.x
- python-telegram-bot 库
- 优雅的银玫瑰风格

GitHub: https://github.com/liliya-von-roland/simple-telegram-bot
    """
    await update.message.reply_text(about_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理普通消息"""
    user_message = update.message.text
    response = f'🎀 收到你的消息啦："{user_message}"\n本公主的机器人正在学习中哦~'
    await update.message.reply_text(response)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """错误处理"""
    logger.warning(f'更新 {update} 导致错误 {context.error}')
    if update and update.effective_message:
        await update.effective_message.reply_text(
            '哎呀，出错了呢~ 请稍后再试哦~'
        )

def main():
    """主函数"""
    # 创建应用
    application = Application.builder().token(BOT_TOKEN).build()

    # 添加命令处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(CommandHandler("about", about))

    # 添加消息处理器
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # 添加错误处理器
    application.add_error_handler(error_handler)

    # 启动机器人
    logger.info("🎀 银玫瑰公主的Telegram机器人启动中...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()