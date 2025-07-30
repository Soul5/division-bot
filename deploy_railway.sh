#!/bin/bash

# Railway 快速部署腳本
echo "🚂 Railway 快速部署腳本"
echo ""

# 檢查是否已安裝 Railway CLI
if ! command -v railway &> /dev/null; then
    echo "📦 正在安裝 Railway CLI..."
    npm install -g @railway/cli
fi

# 檢查 Git 倉庫
if [ ! -d ".git" ]; then
    echo "❌ 請先初始化 Git 倉庫："
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    echo "   git remote add origin https://github.com/yourusername/division-bot.git"
    echo "   git push -u origin main"
    exit 1
fi

# 登入 Railway
echo "🔐 請登入 Railway..."
railway login

# 創建新項目
echo "🚀 創建 Railway 項目..."
railway init

# 設置環境變量
echo "🔧 設置環境變量..."
read -p "請輸入您的 Discord Bot Token: " DISCORD_TOKEN
railway variables set DISCORD_TOKEN="$DISCORD_TOKEN"

# 部署
echo "📦 正在部署..."
railway up

echo ""
echo "✅ 部署完成！"
echo "🔍 查看日誌：railway logs"
echo "🌐 查看狀態：railway status" 