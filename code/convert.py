input_file = 'input.txt'  # 输入文件名
output_file = 'output.txt'  # 输出文件名

with open(input_file, 'r', encoding='utf-8') as file:
    data = file.readlines()
output_data = {}
for line in data:
    id_val = line.split("'id': '")[1].split("_")[-1].split("'")[0].lstrip('0')  # 去掉前导零
    name_val = line.split("'name': '")[1].split("'")[0]
    output_data[id_val] = name_val
formatted_output = ", ".join([f"{key}: '{value}'" for key, value in output_data.items()])
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(formatted_output)
