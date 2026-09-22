#!/bin/bash
# Serves the site locally and opens it in your browser.
# Close the Terminal window (or press Control-C) when you're done.
cd "$(dirname "$0")/dist" || exit 1
PORT=8765
while lsof -i ":$PORT" >/dev/null 2>&1; do PORT=$((PORT+1)); done
echo "Serving the Er-Con site at http://localhost:$PORT/"
echo "Press Control-C here when you're finished."
echo
python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 &
SERVER=$!
trap 'kill $SERVER 2>/dev/null' EXIT
sleep 1
open "http://localhost:$PORT/"
wait $SERVER
