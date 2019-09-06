def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    number_of_splits = int(n/k)
    for split_num in range(number_of_splits):
        split = string[split_num*k:split_num*k+(k)]
        unique_string = ''
        for char in split:
            if char in unique_string:
                do_nothing = 1
            else:
                unique_string+=char
        print(unique_string)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
