def main():
    scores = [[75, 45, 70, 59], [33, 80, 56, 47], [54, 20, 67]]
    for index, score in enumerate(scores):
        for inner_index, inner_value in enumerate(score):
             print(f"inner_value: ", inner_value, end='\t')
             print(f"inner index: ", inner_index)

             print(f"inner list: ", score, end='\t')
             print(f"inner list index: ", index)


def dic():
   days_per_month = {'january': 31, 'february': 28, 'march': 30, 'april': 31,}
   for key, value in days_per_month.items():
       print()
       print(key, value)
   for month_name in days_per_month.keys():
       print()
       print(month_name)
       print(month_name, days_per_month[month_name])
   for days in days_per_month.values():
       print()
       print(days)
       print(days, days_per_month[month_name])

def dic2():
    number_dic = {1: "one", 2: "two", 3: "three", 4: "four", 5: "six",}
    print(number_dic)
    number_dic[5] = "five"
    print(number_dic[5])
    print(number_dic[3])
    number_dic[3] = "thirty_three"
    print(number_dic[3])
    number_dic[7] = "seven"
    print(number_dic[7])
    print(number_dic)
    del number_dic[3]
    print(number_dic)
    #print(number_dic[9])
    print(number_dic.get(9))
    print(number_dic.get(9, "Second argument"))
    print(number_dic.pop(2))


def convert_number_to_words(numbers):
    numbers_to_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
    }
    return numbers_to_words.get(numbers, "Invalid number")





if __name__ == "__main__":
    main()
    dic()
    dic2()

    number = int(input("Enter a number: "))
    numbers_to_words = convert_number_to_words(number)
    print(f"The number {number} is: {numbers_to_words}")