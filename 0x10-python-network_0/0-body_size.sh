#!/bin/bash
# Get the body size from outgoing request to url introduced as arguement
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
