

# 과제1: 2021.10.13
  - 4개 
 
 ## 과제 내용
 1. 히스토그램 평탄화
  - 사용자로부터 R, G, B 중의 하나의 채널을 입력받고 
  - 입력받은 채널에 대한 히스토그램을 그리고 
  - 평탄화를 한 후에 그 영상을 출력하시오. 
    (선택받은 채널 이외의 채널 값은 변화하지 않음)
 2. 공간 도메인 필터링
   - 각 픽셀에 임의의 값을 더해 노이즈를 생성하고, 
   - 사용자로부터 Bilateral filtering을 위한 
   - diameter, SigmaColor, SigmaSpace를 입력받아 노이즈를 제거하고 
   - 노이즈 제거 전후의 영상을 출력하시오. 
    (다양한 파라미터 변화를 통해 영상이 어떻게 변화하는지 보고서에 넣으시오.)
 3. 주파수 도메인 필터링
   - DFT를 통해서 영상을 주파수 도메인으로 바꿔서 출력 한 후에 사용자로부터 반지름을 입력받아서 
   - 그 크기만큼의 원을 그린 후에 DFT 결과에 곱해준 후에 IDFT를 해서 필터링된 영상을 출력하시오. 
   - 사용자로부터 Low pass인지 High Pass인지를 입력받아 Low pass면 원 안을 통과시키고, 
   - High Pass면 원 바깥을 통과시키도록 하시오.
 4. 모폴로지 필터
   - 영상을 이진화한 후에 사용자로부터 Erosion, Dilation, Opening, Closing에 대한 선택과 횟수를 입력받아서 
   - 해당 결과를 출력하시오.
 
 ## 제출 자료
  <p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/2021_2_vision_no1_11.png.PNG" border="0" width="720" height="960"> </p>
  <p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/2021_2_vision_no1_12.PNG" border="0" width="720" height="960"> </p>
  <p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/2021_2_vision_no1_13.PNG" border="0" width="720" height="960"> </p>
  <p> <img src="https://github.com/ByeongKeun/Industrial-AI/blob/master/images/2021_2_vision_no1_14.PNG" border="0" width="720" height="960"> </p>
