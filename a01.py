# don't change any function name write you all code inside the function only for every question solution and return you output as mentioned in problem statement.

def question_first_solution(input_seq):
    # Write your code here
    pass

def question_second_solution(tickets):
    starts = []
    ends = []
    final = {}
    for i in tickets:
        starts.append(i)
        ends.append(tickets.get(i))
    for i in starts:
        if i not in ends:
            start = i
    while len(final) < len(tickets):
        final.setdefault(start,tickets.get(start))
        start = final.get(start)
    return final

def question_third_solution(states):
    final = {}
    for i in states:
        for k in states.get(i):
            l = []
            if k in final:
                for j in final.get(k):
                    l.append(j)
                l.append(i)
                final[k] = l
            else:
                l.append(i)
                final.setdefault(k,l)
    return final

def question_fourth_solution(brackets):
    # Write your code here
    pass

def question_fifth_solution(number):
    # Write your code here
    pass

def question_sixth_solution(code):
    # Write your code here
    pass

def question_seventh_solution(string):
    # Write your code here
    pass

def question_eighth_solution(string):
    # Write your code here
    pass

def question_ninth_solution(arr, k):
    # Write your code here
    pass

def question_tenth_solution(nums):
    # Write your code here
    pass