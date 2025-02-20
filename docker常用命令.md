## docker 状态查询
```bash
docker ps
docker ps -a

docker --version
docker info
docker --help
docker run --help
docker ps --help
...
```


## docker 操作镜像命令

```bash
docker images

docker rmi 镜像id/镜像名
```


## docker 操作容器命令

```bash
docker ps
docker ps -a
```

###  docker run 命令
```bash
# 端口映射 -p 参数
# 左边80是宿主机, 右边80是容器内部端口, 最后一个 nginx 是镜像名
docker run -d -p 80:80 nginx
docker run -d -p 80:80 --name nginx01 nginx

# 自动端口映射 -P 参数
# -P 表示暴漏出容器内部所有的端口, 并随机映射到宿主机的端口
docker run -d -P --name nginx01 nginx


docker start 容器id/容器名
docker stop 容器id/容器名


docker rm 容器id/容器名
docker rm -f 容器id/容器名
```

### docker run 容器异常退出后/挂掉自动删除( --rm 参数)
```bash
docker run --rm -d -p 80:80 --name nginx02 nginx 

docker stop nginx02  # 容器会自动删除, 即 docker ps -a 命令看不到
```

## docker 重启策略( --restart 参数 ), 三种重启策略
- no: 容器退出后不重启
- on-failure: 容器退出后, 一定次数内重启, 可以加上 :3, 表示最多重启3次
- always: 容器退出后, 一直重启

```bash
# always 会一直启动, 即开机自启
docker run --restart always -d -p 80:80 --name nginx02 nginx 
# on-failure 模式不会开机自启
docker run --restart on-failure:3 -d -p 80:80  --name nginx02 nginx

# 注意命令: docker stop 容器id/容器名 属于正常退出, 不会触发重启策略, 意外退出才会触发
```


## docker run 启动时加入环境变量
```bash
# docker inspect 容器id/容器名   查看容器配置信息
docker inspect nginx02

# -e 参数, 添加环境变量, 多个环境变量用多个 -e 参数 (也可以用 -env 参数, 效果与 -e 参数一样)
docker run -d -p 81:80 --name nginx_env -e HTTP_PROXY=http://172.30.xxx.xxx:7892 -e HTTPS_PROXY=http://172.30.xxx.xxx:7892 -e NO_PROXY=localhost,127.0.0.1 --restart always nginx

docker inspect nginx_env

或者

docker exec -it nginx_env bash
docker exec -it nginx_env env
```


## docker run 限制容器资源使用
```bash
# 内存限制
## -m 100m  # 限制内存使用100m (单位可以是 b, k, m, g) 
docker run -d -p 83:80 --name nginx_mem -m 2m --rm nginx
docker run -d -p 83:80 --name nginx_mem -m 8m --rm nginx

## 查看容器内存使用情况
docker stats 容器id/容器名
docker stats nginx_mem

# cpu 限制
## --cpus 1 # 限制cpu使用1个核
docker run -d -p 84:80 --name nginx_mem_cpu -m 8m --cpus 1 --rm nginx

```


## docker logs 查看容器日志
```bash
docker logs --help
docker logs 容器id/容器名
docker logs -f 容器id/容器名  # -f 参数, 实时查看日志
```

## 进入容器内部 docker exec -it 容器id/容器名 bash/其他命令
```bash
docker exec -it 容器id/容器名 bash
docker exec -it 容器id/容器名 env
```



## docker 启动一个系统镜像作为一个容器
```bash
# 拉取
docker pull ubuntu
docker pull centos
docker pull debian

# 拉取镜像后，可以使用 docker run 命令启动一个新容器。以下是启动 Ubuntu 容器的示例：
docker run -d -P --rm --name ubuntu_container1 ubuntu tail -f /dev/null      # tail -f /dev/null 是为了保持容器一直挂起运行, 若容器内没有服务, 容器会自动退出
docker run -d -P --rm --name centos_container1 centos tail -f /dev/null
docker run -d -P --rm --name centos_container2 centos tail -f /dev/null

```


## docker cp 命令, 复制宿主机文件到容器内部
```bash
docker cp 宿主机文件路径 容器id/容器名:容器内部路径
docker cp 容器id/容器名:容器内部路径 宿主机文件路径

# 复制文件到容器内部
docker cp /Users/xxx/Downloads/nginx.conf nginx_container1:/etc/nginx/nginx.conf

# 复制文件到宿主机
docker cp nginx_container1:/etc/nginx/nginx.conf /Users/xxx/Downloads/nginx.conf
```

