from hard import CONDITIONS

def rmv_xtra_space(string):
    string = string.split()
    string = ' '.join(string)
    return string

def rmv_fullstop(string):
    if string[-1] == '.':
        string = string[:-1]
    return string

def convert_or(string):
    for i in range(len(string) - 1):
        if string[i:i+2] == 'or':
            string = string[0:i] + "OR" + string[i+2:]
    return string

def convert_and(string):
    for i in range(len(string) - 2):
        if string[i:i+3] == 'and':
            string = string[0:i] + "AND" + string[i+3:]
    return string

def in_course_list(course, course_list):
    if course in course_list:
        return True
    return False

def is_unlocked(course_list, target_course):
    if len(target_course) != 8:
        string = target_course
    else:
        string = CONDITIONS[target_course]
    string = rmv_xtra_space(string)
    string = rmv_fullstop(string)
    string = convert_or(string)
    string = convert_and(string)
    
    condition_arr = []
    prereq_arr = string.split()
    i = 0; j = 0; open_bracket = -1; end = False
    while i < len(prereq_arr):

        if prereq_arr[i][0] == "(":
            while i+j < len(prereq_arr):
                
                prereq = prereq_arr[i+j]
                for char in prereq:

                    if char == "(":
                        open_bracket += 1
                    elif char == ")":
                        if open_bracket == 0:
                            end = True
                        else:
                            open_bracket -= 1

                if end:
                    break
                j += 1

            prereq_arr[i] = " ".join(prereq_arr[i:i+j+1])
            prereq_arr = prereq_arr[:i+1] + prereq_arr[i+j+1:]
            j = 0
            open_bracket = 0
        
        elif prereq_arr[i] == "AND" or prereq_arr[i] == "OR":
            condition_arr.append(prereq_arr[i])
            prereq_arr.remove(prereq_arr[i])
            i -= 1

        i += 1
    
    
    for i in range(len(prereq_arr)):
        course_type  = prereq_arr[i][:4]
        if course_type == "COMP" or course_type == "MTRN" or course_type == "DPST" or course_type == "MATH":
            prereq_arr[i] = in_course_list(prereq_arr[i], course_list)
        elif course_type[0] == "(":
            prereq_arr[i] = is_unlocked(course_list, prereq_arr[i][1:-1])
    print(prereq_arr)
    for condition in condition_arr:
        if condition == "OR":
            prereq_arr = [prereq_arr[0] or prereq_arr[1]] + prereq_arr[2:]
        if condition == "AND":
            prereq_arr = [prereq_arr[0] and prereq_arr[1]] + prereq_arr[2:]
        print(prereq_arr)
    
    return prereq_arr[0]

print(is_unlocked(["COMP1928", "COMP1521", "DPST1093", "COMP2521"], "COMP3151"))
