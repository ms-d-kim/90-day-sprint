#!/usr/bin/env bash

# Day 03: Start a dummy HTTP server on port 8000 and log its output

LOG_FILE="playground/logs/web.log"
PID_FILE="playground/tmp/webserver.pid"

echo "==> Ensuring log and tmp directories exist..."
mkdir -p playground/logs playground/tmp

echo
echo "==> Checking if something is already listening on port 8000..."
EXISTING_PID=$(lsof -ti tcp:8000 2>/dev/null || true)
if [ -n "$EXISTING_PID" ]; then
  echo "Found existing process on port 8000 (PID=$EXISTING_PID), killing it..."
  kill "$EXISTING_PID" || true
fi

echo
echo "==> Starting python3 -m http.server 8000 (background)..."
echo "    Logging to $LOG_FILE"

python3 -m http.server 8000 > "$LOG_FILE" 2>&1 &
NEW_PID=$!

echo "$NEW_PID" > "$PID_FILE"

echo
echo "Server started!"
echo "PID: $NEW_PID"
echo "PID saved to: $PID_FILE"
echo "Try: curl localhost:8000"