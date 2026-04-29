#!/bin/bash

echo "===== SYSTEM HEALTH CHECK ====="

echo ""
echo "---- CPU Usage ----"
top -bn1 | grep "Cpu(s)"

echo ""
echo "---- Memory Usage ----"
free -h

echo ""
echo "---- Disk Usage ----"
df -h

echo ""
echo "---- Uptime ----"
uptime
