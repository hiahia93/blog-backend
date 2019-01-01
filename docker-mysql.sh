#!/usr/bin/env bash
docker run --name blogmq -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_USER=edgar \
-e MYSQL_PASSWORD=1234 -e MYSQL_DATABASE=blog \
-v /home/edgar/Development/py/app/TinyBlog/blog.sql:/docker-entrypoint-initdb.d/blog.sql \
-d mysql