#!/usr/bin/env bash

# Day 03: Basic navigation and filesystem demo

echo "==> Where am I right now?"
pwd

echo
echo "==> What is in this directory?"
ls

echo
echo "==> Creating a nested directory structure under playground/test..."
mkdir -p playground/test/a/b/c

echo
echo "==> Listing playground recursively (-R means recursive):"
ls -R playground