def filter_by_length(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    filtered_lines = []
    i = 0

    while i < len(lines):
        if lines[i].startswith("Length="):
            length_value = int(lines[i].split("=")[1])
            if length_value > 300:
                # Keep the next 4 lines and the current line (total 5 lines)
                filtered_lines.extend(lines[i - 4:i + 1])
        i += 1

    with open(output_file, 'w') as outfile:
        outfile.writelines(filtered_lines)

if __name__ == "__main__":
    input_file_path = "/mnt/e/blast_results/no_hits_headers_qp.txt"  # 替换成你的输入文件路径
    output_file_path = "/mnt/e/blast_results/filtered_output_qp.txt"  # 替换成你的输出文件路径
    filter_by_length(input_file_path, output_file_path)
    print(f"Filtered output saved to {output_file_path}")
