
# 1.
word = input('단어를 입력하세요: ')

#is_palin = True # 회문 판별값을 저장하는 변수, 초깃값은 True
#for i in range(len(word) // 2): # 0부터 문자열 길이의 절반만큼 반복
#    if word[i] != word[-1-i]: #왼쪽문자와 오른쪽 문자를 비교해서 문자가 다르면 
#        is_palin = False
#        break

#print(is_palin) # 회문 판별값 출력

# 2.시퀀스 뒤집기로 문자 검사하기 
print(word == word[::-1]) # 원래 문자열과 반대로 뒤집은 문자열 비교
