#!/usr/bin/env bash

# Day 03: Inspect the dummy HTTP service on port 8000

LOG_FILE="playground/logs/web.log"
PID_FILE="playground/tmp/webserver.pid"

echo "==> Checking that the PID file exists..."
if [ ! -f "$PID_FILE" ]; then
    echo "PID file not found: $PID_FILE"
    echo "Run start_dummy_service.sh first."
    exit 1
fi

SERVER_PID=$(cat "$PID_FILE")

echo
echo "==> Checking if process $SERVER_PID is running..."
ps aux | grep "$SERVER_PID" | grep -v "grep" || echo "No process with PID $SERVER_PID found."

echo
echo "==> Checking port 8000 for listening services..."
lsof -i tcp:8000 || echo "Nothing is listening on port 8000."

echo
echo "==> Showing last 10 lines of web log:"
if [ -f "$LOG_FILE" ]; then
    tail -n 10 "$LOG_FILE"
else
    echo "Log file not found: $LOG_FILE"
fi