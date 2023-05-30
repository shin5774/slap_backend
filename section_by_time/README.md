# Section_by_time

> 게시판관련 기능들의 설명을 적어놓은 문서

## URL별 기능

※ 아래의 기능은 로그인이 되어있어 쿠키로 세션 데이터를 가지고 있다는 전재로 설명함

1. [post] section_by_time/section_update/ \
기능: section update \
필요값: name(농장명),image(농장내 섹션 이미지,개수에 맞게 해줘야함) \
반환값: id,image_url,section_id,is_disease(질병여부),disease:{name,explain}(질병이 있는경우) \
   
2. [get] section_by_time/latest_section/ \
기능: section id에 맞는 최신 상태 반환
필요값: section_id(plants_section의 id)
반환값: section_by_time의 data 전체+is_disease,disease,explain
ps. 한 섹션에서 여러질병 반환을 고려 안함.


