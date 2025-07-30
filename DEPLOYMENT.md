# 🤖 Discord Bot 雲端部署指南

## 🚂 Railway 部署（推薦方案）

Railway 是最簡單的雲端部署方案，完全免費且部署簡單。

### 優點
- ✅ **完全免費**
- ✅ **部署超簡單**
- ✅ **自動重啟**
- ✅ **無需信用卡**
- ✅ **良好文檔**

---

## 📋 部署步驟

### 步驟 1：準備 GitHub 倉庫

```bash
# 初始化 Git 倉庫
git init
git add .
git commit -m "Initial commit"

# 推送到 GitHub
git remote add origin https://github.com/yourusername/division-bot.git
git push -u origin main
```

### 步驟 2：部署到 Railway

#### 方法 A：使用自動部署腳本（推薦）
```bash
./deploy_railway.sh
```

#### 方法 B：手動部署
1. 訪問 [Railway.app](https://railway.app)
2. 使用 GitHub 登入
3. 點擊 "New Project"
4. 選擇 "Deploy from GitHub repo"
5. 選擇您的倉庫
6. 在 "Variables" 標籤中添加環境變量：
   - 名稱：`DISCORD_TOKEN`
   - 值：您的 Discord Bot Token
7. 等待自動部署完成

### 步驟 3：監控和維護

#### 查看日誌
- 在 Railway 控制台查看實時日誌
- 或使用 CLI：`railway logs`

#### 重啟服務
- 在 Railway 控制台點擊 "Restart"
- 或使用 CLI：`railway restart`

#### 更新 Bot
- 推送新代碼到 GitHub
- Railway 會自動重新部署

---

## 🔧 環境變量

必須設置以下環境變量：

| 變量名 | 說明 | 範例 |
|--------|------|------|
| `DISCORD_TOKEN` | Discord Bot Token | `your_discord_bot_token_here` |

---

## 🆘 常見問題

### Q: Bot 無法連接 Discord？
A: 檢查 DISCORD_TOKEN 是否正確設置

### Q: Bot 經常斷線？
A: Railway 有自動重啟功能，通常不會有問題

### Q: 如何更新 Bot？
A: 推送新代碼到 GitHub，Railway 會自動重新部署

### Q: 如何備份數據？
A: 所有遊戲數據都在代碼中，更新代碼即可

---

## 📊 部署後檢查

部署完成後，請檢查：

1. **Bot 是否在線**：在 Discord 中查看 Bot 狀態
2. **命令是否正常**：測試 `/help` 命令
3. **日誌是否正常**：在 Railway 控制台查看日誌
4. **自動重啟**：測試重啟功能

---

## 🎉 完成！

部署完成後，您的 Bot 將：
- ✅ 24/7 在線運行
- ✅ 自動重啟（如果崩潰）
- ✅ 無需本地電腦
- ✅ 完全免費使用 