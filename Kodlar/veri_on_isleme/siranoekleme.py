def add_line_numbers(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    with open(output_file, 'w', encoding='utf-8') as output_file:
        for i, line in enumerate(lines, start=1):
            output_file.write(f"{i}. {line}")

# Kullanım örneği
input_file_path = 'final1.txt'  # Okunacak dosyanın adı
output_file_path = 'final2.txt'  # Yazılacak dosyanın adı

add_line_numbers(input_file_path, output_file_path)
