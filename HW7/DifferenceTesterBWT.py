
import sys

def open_file(file_name):
    data = []
    with open(file_name) as f:
        data = f.readline().rstrip("\n").split(" ")
    return data

def compare_data(correct_data, my_data):
    print(len(correct_data))
    print(len(my_data))
    correct = 0
    for d in my_data:
        if d not in correct_data:
            correct = 1
            print(d)
    return correct

def main():
    correct_data = open_file("./output/rosalind_extra_data_output_p76.txt")
    my_data = open_file("./output/rosalind_output_p76.txt")
    if compare_data(correct_data,my_data) == 1:
        print("Not the same")
    else:
        print("the same")

if __name__ == "__main__":
    main()