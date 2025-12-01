#!/usr/bin/env bash

# Day 03: Process management demo

echo "==> Starting a background sleep 30 process..."
sleep 30 &
SLEEP_PID=$!

echo
echo "Started sleep process with PID: $SLEEP_PID"

echo
echo "==> Showing processes matching 'sleep':"
ps aux | grep "sleep" | grep -v "grep"

echo
echo "==> Killing sleep process with kill $SLEEP_PID"
kill "$SLEEP_PID"

echo
echo "==> Verifying it's gone:"
ps aux | grep "sleep" | grep -v "grep" || echo "No sleep process remaining."