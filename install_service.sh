#!/bin/bash

# 安裝 Discord Bot 系統服務
SERVICE_NAME="com.division.bot"
PLIST_FILE="com.division.bot.plist"
SERVICE_PATH="$HOME/Library/LaunchAgents/$PLIST_FILE"

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🤖 Discord Bot 系統服務安裝器${NC}"
echo ""

# 檢查是否已安裝
if [ -f "$SERVICE_PATH" ]; then
    echo -e "${YELLOW}⚠️  服務已存在，正在卸載舊版本...${NC}"
    launchctl unload "$SERVICE_PATH" 2>/dev/null
    rm -f "$SERVICE_PATH"
fi

# 複製服務文件
echo -e "${BLUE}📁 正在安裝系統服務...${NC}"
cp "$PLIST_FILE" "$SERVICE_PATH"

# 載入服務
echo -e "${BLUE}🚀 正在啟動服務...${NC}"
launchctl load "$SERVICE_PATH"

# 檢查服務狀態
sleep 3
if launchctl list | grep -q "$SERVICE_NAME"; then
    echo -e "${GREEN}✅ 服務安裝成功！${NC}"
    echo ""
    echo -e "${BLUE}📋 服務管理命令：${NC}"
    echo -e "  啟動服務: launchctl load $SERVICE_PATH"
    echo -e "  停止服務: launchctl unload $SERVICE_PATH"
    echo -e "  查看狀態: launchctl list | grep $SERVICE_NAME"
    echo -e "  查看日誌: tail -f /Users/kouhei/Downloads/division/bot.log"
    echo ""
    echo -e "${GREEN}🎉 Bot 現在會在系統啟動時自動運行！${NC}"
else
    echo -e "${RED}❌ 服務安裝失敗${NC}"
    echo -e "${YELLOW}💡 請檢查日誌文件: /Users/kouhei/Downloads/division/bot.log${NC}"
fi 