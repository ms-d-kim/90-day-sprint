#!/usr/bin/env bash

# Day 03: Logging and log inspection demo

LOG_FILE="playground/logs/app.log"

echo "==> Creating log file at $LOG_FILE"
mkdir -p playground/logs

echo "INFO: service starting" > "$LOG_FILE"
echo "INFO: handling request id=1" >> "$LOG_FILE"
echo "ERROR: failed to handle request id=2" >> "$LOG_FILE"
echo "INFO: service shutting down" >> "$LOG_FILE"

echo
echo "==> Full log contents:"
cat "$LOG_FILE"

echo
echo "==> Only ERROR lines (grep ERROR):"
grep "ERROR" "$LOG_FILE" || echo "No ERROR lines found."

echo
echo "==> First 2 lines (head -n 2):"
head -n 2 "$LOG_FILE"

echo
echo "==> Following log in real time (tail -f)."
echo "    Open another terminal and run:"
echo "      echo \"INFO: new request\" >> $LOG_FILE"
echo "    Press Ctrl+C to stop tailing."
echo

tail -f "$LOG_FILE"