# FAST_API

### docker hub 주소 jo1013/fast_api:0.05

* docker container에 필요한 추가 라이브러리가 있을 경우 (컨테이너실행중) 설치 후 커밋 docker hub에 푸시하면 된다. 

### 도커 컨테이너 실행 


```
$ docker run -it --rm -p -d 8124:8124 -p 8000:8000 -v ~/workspace:/home jo1013/fast_api:0.05

$ docker run -it --rm -p [로컬포트]:[컨테이너포트] -v [local 경로]:[컨테이너경로] [image]:[tag]


```
### docker docker 터미널 

```
$docker exec -it b83b5afe25bd bash
$docker exec -it [CONTAINER ID or CONTAINER NAME] bash
```

### docker cotainer ID check

``` 
$docker ps
```


### docker commit 

```
$ docker commit 977bd1a14aa6 jo1013/fastapi:0.05
$ docker commit [container_id] [image]:[tag]
```


### docker push 

```
$ docker push jo1013/fastapi:0.05
$ docker push [images]:[tag]
```


### docker bash에서 쥬피터 켜기

```
$ jupyter notebook --allow-root --ip=0.0.0.0 --port=8124 --no-browser
```
 
 ## fast_api  개인 영화 추천 

 * 터미널에서  실행할때 경로는 터미널 기준으로 py가실행되므로 py파일 import에 app 폴더안에서 실행 필요 

 ```
$ cd fast_api
$ cd app
```


```
$ uvicorn movie_recomendation:app --reload --host=0.0.0.0 --port=8000
$ uvicorn [py파일]]:[api_name] --reload --host=0.0.0.0 --port=8000
```




*  0.0.0.0:8000/items/[movie_id] 입력시 개인 id 에 따른 추천이 나오게된다. 


참고자료 : https://fastapi.tiangolo.com/tutorial/response-model/
https://github.com/lsjsj92/
