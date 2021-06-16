# FAST_API

### docker hub 주소 jo1013/fast_api:0.05

* docker container에 필요한 추가 라이브러리가 있을 경우 (컨테이너실행중) 설치 후 커밋 docker hub에 푸시하면 된다. 

### 도커 컨테이너 실행 
```
$ docker run -it --rm -p [로컬포트]:[컨테이너포트] -v [local 경로]:[컨테이너경로] [image]:[tag]
$ docker run -it --rm -p 8888:8888 -p 8000:8000 -v ~/workspace:/home jo1013/fast_api:0.05
```
### docker docker 터미널 
```
$docker exec -it b83b5afe25bd bash
$docker exec -it [CONTAINER ID] bash
```

### docker cotainer ID check

``` 
$docker ps
```


### docker commit 

```
$ docker commit 977bd1a14aa6 jo1013/fastapi:0.01
$ docker commit [container_id] [image]:[tag]
```


### docker push 
```
$ docker push jo1013/fastapi:0.01
$ docker push [images]:[tag]
```


### docker bash
```
$ jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --no-browser
```
 
 
