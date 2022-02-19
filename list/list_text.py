data = '12, 3 4, 56, 78, 90'
print(data.split((",")))


# 문자열의 공백을 없애는 방법
# strip, replace

user_lst = ['']
user_input_data = "1668".split(",")
user_lst.extend(i.replace(' ', '') for i in user_input_data)

sample_list = list(filter(None, data.split((","))))
new_strip_data = [i.strip() for i in data.split((","))]
new_replace_data = [i.replace(' ', '') for i in data.split((","))]

print("strip :", new_strip_data)
print("replace :", new_replace_data)

user_lst = ['']
user_input_data = data.split(",")

# 리스트끼리 병합하기
# extent
user_lst.extend(i.replace(' ', '') for i in user_input_data)

print(user_lst)