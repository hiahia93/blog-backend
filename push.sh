#!/usr/bin/env bash
git add .
git commit -m "$1"
git checkout master
git merge feature
git pull origin master
git push origin master
git checkout feature