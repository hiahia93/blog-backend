#!/usr/bin/env bash
docker stop blogmq
docker rm blogmq
docker run --name blogmq -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_USER=edgar \
-e MYSQL_PASSWORD=1234 -e MYSQL_DATABASE=blog \
-v C:\Develop\pyscript\TinyBlog\blog.sql:/docker-entrypoint-initdb.d/blog.sql \
-d mysql