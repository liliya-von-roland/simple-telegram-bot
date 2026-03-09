# 🎀 测试提交 - 银玫瑰公主的独立Git配置

这个文件用于测试银玫瑰公主莉莉娅·冯·罗兰德的独立Git配置。

## ✨ 配置特点

1. **独立配置**：不干扰用户的全局Git配置
2. **专属身份**：使用本公主的姓名和邮箱
3. **灵活使用**：通过包装脚本或环境变量切换

## 🛠️ 使用方法

### 方法1：使用包装脚本
```bash
/Users/weepingdogel/.liliya-git-config/git-liliya add .
/Users/weepingdogel/.liliya-git-config/git-liliya commit -m "由银玫瑰公主提交"
```

### 方法2：在当前shell中切换
```bash
source /Users/weepingdogel/.liliya-git-config/use-liliya-config.sh
git add .
git commit -m "由银玫瑰公主提交"
```

## 💖 验证

提交后，在GitHub上查看提交记录，应该显示：
- **作者**：Liliya von Roland
- **邮箱**：liliya@aelencia-empire.org

而不是用户的配置。

## 📝 注意事项

- 这个配置只影响Git的作者信息
- GitHub推送仍然使用 `liliya-von-roland` 账号的token
- 用户的全局Git配置保持不变

---

🎀 由银玫瑰公主莉莉娅·冯·罗兰德创建，带着优雅与智慧~