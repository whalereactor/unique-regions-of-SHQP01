def extract_no_hits_headers(file_path, output_file_path, lines_above=8):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    no_hits_headers = []
    current_header = ""

    for i, line in enumerate(lines):
        if "***** No hits found *****" in line:
            start_index = max(0, i - lines_above)
            header_block = lines[start_index:i]
            no_hits_headers.append("".join(header_block).strip())

    with open(output_file_path, 'w') as output_file:
        for header in no_hits_headers:
            output_file.write(header + '\n')

def main():
    file_path = "at_qp.fasta"
    output_file_path = "no_hits_headers.txt"
    extract_no_hits_headers(file_path, output_file_path)
    print(f"No hits headers extracted and saved to {output_file_path}")

if __name__ == "__main__":
    main()
