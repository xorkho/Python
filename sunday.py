'''SUM OF EVEN NUMBERS FROM LIST'''
# def sum_of_even_numbers(numbers):
#     return sum(num for num in numbers if num%2==0)
# numbers=[1,2,3,4,5,6,7,8,9]
# result=sum_of_even_numbers(numbers)
# print(result)

'''INPUT LIST OF STRINGS AND OUTPUT IS DICTIONARY'''
# def string_length(strings):
#     return{string:len(string) for string in strings}
# strings=["apples","bananas","apricot"]
# result=string_length(strings)
# print(result)

'''INPUT LIST OF NUMBERS AND REMOVE ITS DUPLICATE'''
def unique(numbers):
    l=[]
    for num in numbers:
        if num not in l:
            l.append(num)
    return(l)
numbers=[1,2,2,3,4,5,6,6,6,7,4]
result=unique(numbers)
print(result)