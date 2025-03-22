# FastAPI Docker 설정 및 실행 가이드

## Docker 이미지 정보
- Docker Hub: `jo1013/fast_api:0.05`

## Docker 컨테이너 실행

```bash
# 기본 실행 명령어
docker run -it -d -p 8124:8124 -p 8000:8000 -v ~/workspace:/home jo1013/fast_api:0.05

# 일반 형식
docker run -it --rm -p [로컬포트]:[컨테이너포트] -v [local경로]:[컨테이너경로] [이미지명]:[태그]
```

## Docker 컨테이너 관리 명령어

### 컨테이너 접속
```bash
docker exec -it b83b5afe25bd bash
docker exec -it [CONTAINER_ID 또는 CONTAINER_NAME] bash
```

### 실행 중인 컨테이너 확인
```bash
docker ps
```

### 컨테이너 변경사항 저장 (커밋)
```bash
docker commit 977bd1a14aa6 jo1013/fastapi:0.05
docker commit [container_id] [이미지명]:[태그]
```

### Docker Hub에 이미지 업로드
```bash
docker push jo1013/fastapi:0.05
docker push [이미지명]:[태그]
```

> **참고**: 컨테이너에 추가 라이브러리 설치가 필요한 경우, 설치 후 커밋하고 Docker Hub에 푸시하면 됩니다.

## Jupyter Notebook 실행

컨테이너 내에서 Jupyter Notebook 실행:
```bash
jupyter notebook --allow-root --ip=0.0.0.0 --port=8124 --no-browser
```

## FastAPI 영화 추천 서비스 실행

### 디렉토리 이동
```bash
cd fast_api
cd app
```

### FastAPI 서버 실행
```bash
uvicorn movie_recomendation:app --reload --host=0.0.0.0 --port=8000
uvicorn [py파일명]:[api_이름] --reload --host=0.0.0.0 --port=8000
```

### 서비스 접속
브라우저에서 `0.0.0.0:8000/items/[movie_id]`에 접속하면 개인 ID에 따른 영화 추천 결과를 확인할 수 있습니다.

## 참고 자료
- FastAPI 응답 모델: https://fastapi.tiangolo.com/tutorial/response-model/
- GitHub 저장소: https://github.com/lsjsj92/
