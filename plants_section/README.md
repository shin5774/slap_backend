# Plants_section

> 게시판관련 기능들의 설명을 적어놓은 문서

## URL별 기능

※ 아래의 기능은 로그인이 되어있어 쿠키로 세션 데이터를 가지고 있다는 전재로 설명함

1. [post] plants_section/ \
기능: 게시물 생성 \
필요값: id,password,name,email \
반환값: 사용자 db값(model 인자 전부) \
   (이 url은 만들긴 했지만 우리의 의논상 사용하지는 않는걸로)


2. [delete] plants_section/ \
기능: 게시물 삭제 \
필요값: 없음 \
반환값: 없음  


3. [get] plants_section/section_by_farm/ \
기능: 해당 농장의 전체 섹션의 data 반환
필요값: name:농장 이름
반환값: 농장안의 모든 섹션의 dgata (질병판단은 status)
