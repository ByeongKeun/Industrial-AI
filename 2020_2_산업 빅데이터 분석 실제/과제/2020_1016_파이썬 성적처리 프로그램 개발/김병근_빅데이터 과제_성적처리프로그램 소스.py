# ----- 실행 main() -----
def main():

    students = []

    print()
    print("┌------------------------------------------------------------┐");
    print("│                 성적 처리 프로그램 - 김병근                │");
    print("└------------------------------------------------------------┘\n");
    print()
    while True:
        select = int(input("1.성적입력 2.점수처리 3.종료 \n"))

        # ----- 성적 입력 -----
        if select == 1:
            students = Insert(students)

        # ----- 처리 결과 Report -----
        elif select ==2:
            students = Report(students)
        
        # ----- dispose -----
        else:
            print("종료되었습니다.")
            break

# ----- 성적 입력 -----
def Insert(students):
    
    cntstudents = int(input("학생수를 입력하세요: "))

    for i in range(cntstudents):
        id = input('학번을 입력하세요 : ')
        
        #이름이 중복일 경우
        if (id in students) == True:
            print('이미 등록된 학번입니다.다시 등록해주세요')
            id = input('학번을 입력하세요 : ')

        #성적 입력
        name = input('이름을 입력하세요 : ')
        kor =  int(input('국어 성적을 입력하세요 : '))        
        math = int(input('수학 성적을 입력하세요 : '))
        eng =  int(input('영어 성적을 입력하세요 : '))
        print('등록완료 되었습니다.')

        score = kor+eng+math
        avg = round(score/3, 3)

        students.append({'이름':name, '학번':id,'국어':kor,'영어':eng, '수학':math, '총점':score, '평균':avg})

    return students

# ----- 처리 결과 Report -----
def Report(students):
    print("=================== 처리 결과 Report ===================")           
    total_score = []
    total_avg = []
    
    #점수 합계 기록 ---------------------------------------
    cntstudents = len(students)
    for i in range(cntstudents): 
        
        total_score.append(students[i].get('총점'))    #total score 저장
        total_avg.append(students[i].get('평균'))    #total score 저장

    print("1. 총점 목록(total_score): ", total_score)
    print("2. 평균 목록(total_avg): ", total_avg)
    print("3. 등수대로 출력======================================================================")

    #총점 순위대로 sorting  ---------------------------------------
    grade = []
    for i in range(cntstudents):
        a = 1
        for j in range(cntstudents):
            if (students[i].get('평균') < students[j].get('평균')):
                a += 1
                j += 1        
        grade.append({"순위":a})

    for i in range(cntstudents):
        grade[i].update(students[i])
        
    grade_rank = sorted(grade,key=lambda k: k['순위'] )

    
    for i in range(cntstudents):
        print(grade_rank[i])
    print("====================================================================================")

    return students        

main()