# final_project

SSAFY 최종 관통 프로젝트

## 0. Install

---

- django

```python
python manage.py makemigrations
python manage.py migration
pyhton manage.py loaddata popular_actors.json popular_genres.json popular_movies.json 
```

## 1. 팀원 정보 및 업무 분담 내역

---

#### 한승준(팀장) - Django 담당

- 전체적인 기획 및 시안 작성(Figma, Draw.io)

- 로고 제작

- 백엔드
  
  - Actor, Genre, Movie 모델과 관련하여 ERD 설정 후, JSON 파일 API 크롤링 전처리
    
    - popular_actors, popular_genres, popular_movies
  
  - 영화 추천 알고리즘 구현
  
  - movie App 구성(view, model, serializer)
  
  - community 구성(view, model, serializer)

- 프론트엔드
  
  - Bootstrap5 Vue2 활용
  
  - Vue페이지 전반적인 디자인 레이아웃 및 컬러 적용
    
    - 기획과 시안은 Figma 에 레이아웃 모든 페이지 작성
    
    - 디자인은 유사색 및 보색, 로고 컨셉 고려하여 탐색 및 확정
  
  - Actor 관련 컴포넌트 구성
    
    - 별도로 전처리 해둔 JSON 파일을 이용해서 처리
  
  - 영화 디테일 페이지 컴포넌트 구성
    
    - TMDB AXIOS 요청으로 관련 영화 유튜브 Key를 가지고 와서 영상을 따로 처리
    
    - 리뷰 페이지로 넘어가게 설계
  
  - Footer 컴포넌트 구성
  
  - UserInfo 컴포넌트 구성
    
    - 본인이 가장 좋아하는 장르 구현
    
    - 유저 정보 수정 및 탈퇴  레이아웃 구성
    
    - 본인 리뷰 나오게 하기 구성
    
    - 좋아요 누른 영화 나오게 하기
  
  - Main 컴포넌트 구성
    
    - 추천 영화 알고리즘 2가지로 나눠서 구성(선호도, 평점)
  
  - SignUp, Login 컴포넌트 레이아웃 구성
  
  - 네브바 디자인 구성
  
  - 애니메이션 구현
    
    - Vue transition
    
    - keyframe을 활용한 animation & transition

#### 배상준(팀원) - Vue 담당

- 백엔드
  
  - dj-rest-auth를 활용한 account기능
  
  - accounts App 구성 (view, model, serializer)
  
  - django setting 수정

- 프론트엔드
  
  - 프론트 뷰 구조 설계
  
  - 스켈레톤 Vue페이지 구성
    
    - 검색
      
      - Vue의 필터를 활용한 검색 기능
    
    - 장르별 페이지
      
      - 가로스크롤 기능(Scrollbooster)
      
      - Scrollbooster를 활용한 이동버튼
    
    - 리뷰
    
    - 전체 영화페이지
      
      - 정렬 기능
      
      - 페이지네이션 기능
    
    - 전체적으로 사용할 카드 컴포넌트
      
      - 플립카드 레이아웃 및 디자인 완료
      
      - Bootstrap5 Modal in Vue2 활용
    
    - 네브바 기능 구현 및 레이아웃 완성
  
  - 404 컴포넌트 레이아웃 구성 및 디자인 완료
  
  - 애니메이션 구현
    
    - Vue transition
    
    - keyframe을 활용한 animation & transition

## 2. 목표 서비스 구현 및 실제 구현 정도

---

- 기획한 목표 서비스
  
  - 좋아요 기준으로 추천 영화 알고리즘(구현)
  
  - 장르별로 영화 랜덤으로 추천(구현)
  
  - 연도별 영화 페이지 구성(**구현 보류**)
  
  - 로그인 및 회원가입 후 리뷰 및 좋아요 가능, 메인 추천 알고리즘(선호도, 평점)(구현)
  
  - 일반적인 장르 추천 및 모든 영화 기준 정렬 방식은 로그인 없이도 가능하게(구현)
  
  - 죽기 전에 봐야한 1001 영화 추천 시스템(**구현 보류**)
  
  - 가입 시, 좋아할만한 영화 추천을 위해서 설문조사를 영화 포스터 선택으로(구현)
    
    - 선택하기 전에 해당 영화 디테일 페이지 보이게 하기(**구현 보류**)

## 3. 데이터베이스 모델링

---

![project_detail.jpg](C:\Users\multicampus\Desktop\상준승준\ERD_최종.png)

> Account App
> 
>     accounts/login/ :로그인 (토큰발급)
> 
>     accounts/logout/ : 로그아웃 (토큰삭제)
> 
>     accounts/signup/ : 회원가입 (토큰발급)
> 
>     api/accounts/user/int:user_pk/ : get => 유저 정보 put => 유저 정보 수정  
>     ** data { first_name, last_name, email } **
> 
>     api/accounts/user/remove/int:user_pk/ : 유저삭제(현재 active = 0, remove 주석)
> 
>     api/accounts/user/follow/int:followed_pk/int:following_pk/ : 유저 팔로우
> 
>     api/accounts/user/int:user_pk/likemovies/ : 회원가입한 유저 좋아요  
>     ** data { likemovies : ?? } **

> Movie App
> 
> api/v1/movies/ : 영화 전체 목록 가져오기  
> api/v1/movies/int:movie_pk : 특정 영화 가져오기  
> api/v1/movies/int:movie_pk/like/ : 특정 영화 좋아요  
> ** user_pk = request.POST.get('userPk') **
> 
> api/v1/movies/<int: user_pk>/like_movies/ : 좋아요한 영화 가져오기  
> ** like_movies = user.like_movies.all() **
> 
> api/v1/movies/int:user_pk/recommended_vote_average/ : 평점 순으로 가져오기(좋아요 가장 많이 누른 장르 관련 영화 모두 가져오고 정렬함)  
> **recommend_movie_sorted_final_lst**
> 
> api/v1/movies/int:user_pk/recommended_vote_count/ : 투표수 순으로 가져오기(좋아요 가장 많이 누른 장르 관련 영화 모두 가져오고 정렬함)  
> **recommend_movie_sorted_final_lst**
> 
> api/v1/movies/int:user_pk/recommended_random/ : 랜덤으로 가져오기(좋아요 가장 많이 누른 장르 관련 영화 모두 가져오고 정렬함)  
> **random_lst**

> Community App
> 
> api/v1/community/ : 게시글 전체 들고오기  
> 
> api/v1/community/movie/<int:movie_pk>/  
> : 특정 영화의 게시글 전체 보기 또는 생성(GET, POST)  
> ** user = get_object_or_404(get_user_model(), pk=request.POST.get('user')) **  
> 
> api/v1/community/movie/<int:movie_pk>/review/<int:review_pk>/  
> : 특정 영화의 특정 게시글 가져오기 또는 삭제 또는 수정(GET, DELETE,PUT)  
> ** user = get_object_or_404(get_user_model(), pk=request.POST.get('user')) **  
> 
> api/v1/community/movie/<int:movie_pk>/review/<int:review_pk>/review_recommended/<int:user_pk>/ : 특정 영화의 특정 게시글을 추천하기  
> 
> : 특정 리뷰에 댓글 전체 보기 또는 생성(GET, POST)  
> ** user = get_object_or_404(get_user_model(), pk=request.POST.get('user')) **  
> ** parent_comment = get_object_or_404(Comment, pk=request.POST.get('parent')) **  
> 
> api/v1/community/review/<int:review_pk>/comments/<int:comment_pk>/  
> : 특정 리뷰의 특정 댓글 보기 또는 삭제 또는 생성(GET, DELETE,PUT)  
> ** user = get_object_or_404(get_user_model(), pk=request.POST.get('user'))**  
> **parent_comment = get_object_or_404(Comment, pk=request.POST.get('parent'))**

## 4. 영화 추천 알고리즘에 대한 기술적 설명

---

**주석을 참고하면 기술적 설명이 될거라고 생각합니다.**

- 좋아요 많이 누른 장르 중에서 **평점** 기준으로 추천하는 알고리즘

```python
# 좋아요 누른 영화는 제외
# (좋아요 누른 장르 중에서) 평점 기준 영화 추천 알고리즘
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommended_vote_average(request, user_pk):
    # 일단 전체 영화(500개) 다 가지고 오기
    movies = get_list_or_404(Movie)[:500]
    user = get_object_or_404(get_user_model(), pk=user_pk)

    # 특정 userPk를 가지고있는 유저가 좋아요 누른 영화 가져오고
    like_movies = user.like_movies.all()

    # 좋아요 누른 영화들의 장르 갯수를 딕셔너리 형태로 카운팅한다.
    like_dict = dict()
    for like_movie in like_movies:
        for genre in like_movie.genres.all():
            if genre.pk not in like_dict:
                like_dict[genre.pk] = 1
            else:
                like_dict[genre.pk] += 1

    # 가장 많이 누른 장르 꺼내기
    max_movie_like = max(like_dict,key=like_dict.get)
    
    # 가장 많이 누른 장르에 해당하는 영화 다 가져오기
    recommend_movie_lst = []
    for movie in movies:
        for genre in movie.genres.all():
            if genre.pk == max_movie_like:
                recommend_movie_lst.append(movie)
    # 정렬을 위해서 요소 배열에 해당 영화들 전부 저장하기
    recommend_movie_sorted_lst = []
    for recommend_movie in recommend_movie_lst:
      # 추천영화가 좋아요 누른 영화에 속한다면, 제외
        if recommend_movie in like_movies:
          continue
        recommend_lst = []

        recommend_lst.append(recommend_movie.id),
        recommend_lst.append(recommend_movie.title),
        recommend_lst.append(recommend_movie.release_date),
        recommend_lst.append(recommend_movie.popularity),
        recommend_lst.append(recommend_movie.vote_count),
        recommend_lst.append(recommend_movie.vote_average),
        recommend_lst.append(recommend_movie.overview),
        recommend_lst.append(recommend_movie.poster_path),
        recommend_lst.append(recommend_movie.tmdb_id),
        recommend_lst.append(recommend_movie.genres.all()),
        recommend_lst.append(recommend_movie.like_users.all())
        recommend_lst.append(recommend_movie.actors.all())

        # 다 넣으면 정렬 배열에 넣고 좋아요, 평점, 선호도 순으로 정렬
        recommend_movie_sorted_lst.append(recommend_lst)
        recommend_movie_sorted_lst.sort(key=lambda x : (-x[5], -x[4]))
    # 객체 형태로 배열에 넣기
    recommend_movie_sorted_final_lst = []
    for recommend_movie in recommend_movie_sorted_lst:
        # 딕셔너리 초기화 
        recommend_dict = dict()

        recommend_dict["id"]=recommend_movie[0]
        recommend_dict["title"]=recommend_movie[1]
        recommend_dict["release_date"]=recommend_movie[2]
        recommend_dict["popularity"]=recommend_movie[3]
        recommend_dict["vote_count"]=recommend_movie[4]
        recommend_dict["vote_average"]=recommend_movie[5]
        recommend_dict["overview"]=recommend_movie[6]
        recommend_dict["poster_path"]=recommend_movie[7]
        recommend_dict["tmdb_id"]=recommend_movie[8]
        recommend_dict["genres"]=recommend_movie[9]
        recommend_dict["like_users"]=recommend_movie[10]
        recommend_dict["actors"]=recommend_movie[11]

        recommend_movie_sorted_final_lst.append(recommend_dict)
    # JSON파일로 보내기
    serializer = RecommendedMovieSerializer(recommend_movie_sorted_final_lst[0:30], many=True)
    return Response(serializer.data)
```

- 좋아요 많이 누른 장르 중에서 **선호도** 기준으로 추천하는 알고리즘

```python
# 좋아요 누른 영화는 제외
# (좋아요 누른 장르 중에서) 선호도 기준 영화 추천 알고리즘
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommended_vote_count(request, user_pk):
    # 일단 전체 영화(500개) 다 가지고 오기
    movies = get_list_or_404(Movie)[:500]

    user = get_object_or_404(get_user_model(), pk=user_pk)
    # 특정 userPk를 가지고있는 유저가 좋아요 누른 영화 가져오고
    like_movies = user.like_movies.all()

    # 좋아요 누른 영화들의 장르 갯수를 딕셔너리 형태로 카운팅한다.
    like_dict = dict()
    for like_movie in like_movies:
        for genre in like_movie.genres.all():
            if genre.pk not in like_dict:
                like_dict[genre.pk] = 1
            else:
                like_dict[genre.pk] += 1

    # 사용자가 누른 좋아요 영화의 장르 카운팅해서 가장 많이 본 장르 정하고
    max_movie_like = max(like_dict,key=like_dict.get)

    # 그 장르에 해당하는 영화 다 가져오고
    recommend_movie_lst = []
    for movie in movies:
        for genre in movie.genres.all():
            if genre.pk == max_movie_like:
                recommend_movie_lst.append(movie)

    # 정렬을 위해서 요소 배열에 해당 영화들 전부 저장하기
    recommend_movie_sorted_lst = []
    for recommend_movie in recommend_movie_lst:
      # 추천영화가 좋아요 누른 영화에 속한다면, 제외
        if recommend_movie in like_movies:
          continue
        recommend_lst = []

        recommend_lst.append(recommend_movie.id),
        recommend_lst.append(recommend_movie.title),
        recommend_lst.append(recommend_movie.release_date),
        recommend_lst.append(recommend_movie.popularity),
        recommend_lst.append(recommend_movie.vote_count),
        recommend_lst.append(recommend_movie.vote_average),
        recommend_lst.append(recommend_movie.overview),
        recommend_lst.append(recommend_movie.poster_path),
        recommend_lst.append(recommend_movie.tmdb_id),
        recommend_lst.append(recommend_movie.genres.all()),
        recommend_lst.append(recommend_movie.like_users.all())
        recommend_lst.append(recommend_movie.actors.all())


        # 다 넣으면 정렬 배열에 넣고 좋아요, 평점, 선호도 순으로 정렬
        recommend_movie_sorted_lst.append(recommend_lst)
        recommend_movie_sorted_lst.sort(key=lambda x : (-x[3], -x[4]))
    # 객체 형태로 배열에 넣기
    recommend_movie_sorted_final_lst = []
    for recommend_movie in recommend_movie_sorted_lst:
        # 딕셔너리 초기화 
        recommend_dict = dict()

        recommend_dict["id"]=recommend_movie[0]
        recommend_dict["title"]=recommend_movie[1]
        recommend_dict["release_date"]=recommend_movie[2]
        recommend_dict["popularity"]=recommend_movie[3]
        recommend_dict["vote_count"]=recommend_movie[4]
        recommend_dict["vote_average"]=recommend_movie[5]
        recommend_dict["overview"]=recommend_movie[6]
        recommend_dict["poster_path"]=recommend_movie[7]
        recommend_dict["tmdb_id"]=recommend_movie[8]
        recommend_dict["genres"]=recommend_movie[9]
        recommend_dict["like_users"]=recommend_movie[10]
        recommend_dict["actors"]=recommend_movie[11]


        recommend_movie_sorted_final_lst.append(recommend_dict)

    # JSON파일로 보내기
    serializer = RecommendedMovieSerializer(recommend_movie_sorted_final_lst[0:30], many=True)
    return Response(serializer.data)
```

- 진행과정
  
  1. 먼저 모든 영화(500개)를 모두 가지고 온다.
  
  2. 그리고 본인이 좋아요 누른 영화를 모두 가져온다.
  
  3. 좋아요 누른 영화들의 장르를 카운팅한다.
  
  4. 해당 장르를 가진 영화를 모두 가지고 온다.
  
  5. 그리고 요소 배열에 영화의 요소를 하나하나 넣고 영화 정보 전체를 넣어 줄 배열에 넣어준다
  
  6. 좋아요, 평점, 선호도 or 좋아요, 선호도, 평점 순으로 정렬한다
  
  7. 그리고 영화마다 요소를 꺼내서 객체 형태로 다시 넣어준다(model명도 넣어주기)
  
  8. 그리고 serializer에 담아서 보내준다.
  - 기능 자체는 어렵지 않았는데 Vue에서 받아와서 좋아요 기능을 따로 actions, mutations를 처리해야하는 점이 어려워서 좀 아쉬웠다.

## 5. 서비스 대표 기능에 대한 설명

---

- DB에 저장되어있는 모든 영화들을 조회 가능하고, 좋아요, 평점, 개봉날짜 순으로 정렬과 장르별 선택 기능을 동시에 할 수 있음.

- 장르별로 DB에 저장된 영화들을 랜덤으로 찾는 기능.

- 자신이 좋아요를 누른 영화를 기반으로 추천영화를 메인에 띄워주는 기능

## 6. 기타 (느낀점, 후기)

---

한승준 : 처음에는 얼마나 힘들고 어렵겠나 싶었는데, 막상 2주간 프로젝트를 하고나니, 개발자라는 직업이 굉장히 고되고 피곤한 직업이라는 것을 다시 한 번 각인하게 되었다.

그럼에도 불구하고, 개발자가 되고 싶다는 생각을 한 것은 '성취감'이었다. 어떠한 기능을 오랜 시간 끝에 구현해서 오는 그 쾌감은 굉장히 신선하고 임팩트 있었다. 그래서 개발자가 되고싶다는 생각을 했고, 가급적 나이가 들어도 해당 직업을 유지하고 싶다. 그리고 진로적인 부분에서 굉장히 고민이 많았는데, 이번 프로젝트를 통해서 **프론트엔드** 직무로 준비해야겠다는 생각을 강하게 가지게 되었다. 그래서 2학기 부터는 프론트엔드로 활약하면서 역량을 기르고 내년 6월에 꼭 취업할 수 있도록 해야겠다 (❁´◡`❁)



배상준 :   초반에는 느끼지 못했던 개선점들을 프로젝트 막바지에 와서 크게 느끼게 되었다. 다만 이런 개선점을 개선하기 위해서는 코드를 처음부터 갈아 엎으면서 개선해야 되었기 때문에 리팩토링을 시작부터 염두에 두고 코드를 잘 정리하면서 짜야된다고 생각했다. 또한 DB의 구조는 도중에 바꾸기 어렵다던가, 다른 사이트들에서 어떤식으로 자료를 받아오는지도 몰랐었기 때문에 백에서 자료들을 한번에 받아오는 등의 실수를 저질렀다. 이런 부분은 다음에 개인, 혹은 팀별로 프로젝트를 시행할때 개선해서 적용해야 되겠다는 생각이 들었다.

그럼에도 불구하고 프론트 구조를 짠다던가 기능들을 구현하는 데에 있어서는 괴로움보다는 압도적으로 즐거움이 컸다. 마음맞는 동료와 프로젝트를 진행하는데서 오는 즐거움, 눈으로만 봐왔던 애니메이션이나 기능들을 내 손을 짜냈다는 성취감을 맛볼수있었기 때문에 정말 즐거운 프로젝트였다고 생각한다.

앞으로 개발자가 되는데에 있어서 기반이 되는 좋은 프로젝트 경험이 되었다.
