#!/bin/bash

# Discord Bot 管理腳本
BOT_NAME="division_bot"
LOG_FILE="bot.log"
PID_FILE="bot.pid"

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 檢查 Bot 是否在運行
check_status() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p $PID > /dev/null 2>&1; then
            echo -e "${GREEN}✅ Bot 正在運行 (PID: $PID)${NC}"
            return 0
        else
            echo -e "${RED}❌ Bot 進程不存在，但 PID 文件存在${NC}"
            rm -f "$PID_FILE"
            return 1
        fi
    else
        echo -e "${YELLOW}⚠️  Bot 未運行${NC}"
        return 1
    fi
}

# 啟動 Bot
start_bot() {
    echo -e "${BLUE}🚀 正在啟動 Discord Bot...${NC}"
    
    if check_status > /dev/null 2>&1; then
        echo -e "${YELLOW}⚠️  Bot 已經在運行中${NC}"
        return 1
    fi
    
    # 啟動 Bot
    nohup python3 main.py > "$LOG_FILE" 2>&1 &
    PID=$!
    echo $PID > "$PID_FILE"
    
    # 等待幾秒檢查是否成功啟動
    sleep 3
    if check_status > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Bot 成功啟動！(PID: $PID)${NC}"
        echo -e "${BLUE}📝 日誌文件: $LOG_FILE${NC}"
        echo -e "${BLUE}🔍 查看日誌: tail -f $LOG_FILE${NC}"
    else
        echo -e "${RED}❌ Bot 啟動失敗${NC}"
        rm -f "$PID_FILE"
        return 1
    fi
}

# 停止 Bot
stop_bot() {
    echo -e "${BLUE}🛑 正在停止 Discord Bot...${NC}"
    
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p $PID > /dev/null 2>&1; then
            kill $PID
            rm -f "$PID_FILE"
            echo -e "${GREEN}✅ Bot 已停止${NC}"
        else
            echo -e "${YELLOW}⚠️  Bot 進程不存在${NC}"
            rm -f "$PID_FILE"
        fi
    else
        echo -e "${YELLOW}⚠️  Bot 未運行${NC}"
    fi
}

# 重啟 Bot
restart_bot() {
    echo -e "${BLUE}🔄 正在重啟 Discord Bot...${NC}"
    stop_bot
    sleep 2
    start_bot
}

# 查看日誌
show_logs() {
    if [ -f "$LOG_FILE" ]; then
        echo -e "${BLUE}📝 顯示最近的日誌 (最後 20 行):${NC}"
        tail -20 "$LOG_FILE"
    else
        echo -e "${YELLOW}⚠️  日誌文件不存在${NC}"
    fi
}

# 實時監控日誌
monitor_logs() {
    if [ -f "$LOG_FILE" ]; then
        echo -e "${BLUE}👀 實時監控日誌 (按 Ctrl+C 退出):${NC}"
        tail -f "$LOG_FILE"
    else
        echo -e "${YELLOW}⚠️  日誌文件不存在${NC}"
    fi
}

# 顯示幫助
show_help() {
    echo -e "${BLUE}🤖 Discord Bot 管理工具${NC}"
    echo ""
    echo "用法: $0 [命令]"
    echo ""
    echo "命令:"
    echo -e "  ${GREEN}start${NC}     - 啟動 Bot"
    echo -e "  ${RED}stop${NC}      - 停止 Bot"
    echo -e "  ${YELLOW}restart${NC}   - 重啟 Bot"
    echo -e "  ${BLUE}status${NC}    - 查看 Bot 狀態"
    echo -e "  ${BLUE}logs${NC}      - 查看日誌"
    echo -e "  ${BLUE}monitor${NC}   - 實時監控日誌"
    echo -e "  ${BLUE}help${NC}      - 顯示此幫助"
    echo ""
    echo "範例:"
    echo "  $0 start"
    echo "  $0 status"
    echo "  $0 logs"
}

# 主程序
case "$1" in
    start)
        start_bot
        ;;
    stop)
        stop_bot
        ;;
    restart)
        restart_bot
        ;;
    status)
        check_status
        ;;
    logs)
        show_logs
        ;;
    monitor)
        monitor_logs
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        show_help
        exit 1
        ;;
esac 