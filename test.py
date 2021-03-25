"""
このファイルに解答コードを書いてください
"""
file_name = "./input.txt"
input_file = open(file_name, "r")
all_lines = input_file.readlines()
input_num = 0
num_word_dict = {}
output = ""
output_flag = 0
for this_line in all_lines:
    if ":" in this_line:
        number = this_line.split(":")[0]
        word = this_line.split(":")[1][:-1]
        num_word_dict  = {**num_word_dict, **{number:word}}
    elif this_line != "":
        input_num = int(this_line[:-1])
sorted_dict=dict(sorted(num_word_dict.items(),key=lambda x:x[0],reverse=False))
for key,value in sorted_dict.items():
    if input_num % int(key) == 0:
        output = output + value
        output_flag = 1
if output_flag == 0:
    print(input_num)
else:
    print(output)
