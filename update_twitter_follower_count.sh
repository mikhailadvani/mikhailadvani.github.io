#!/usr/bin/env bash
set -ex
./fetch_follower_count.py

GIT_DIFF_FILES=$(git diff --name-only)

if [[ "$GIT_DIFF_FILES" =~ "twitter_follower_count.json" ]]; then
    git add twitter_follower_count.json
    git commit -m "[CRON] Updating twitter count"
    git push origin master
else
    echo "Follower count unchanged"
fi