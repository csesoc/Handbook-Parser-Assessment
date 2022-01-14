from hard import CONDITIONS

#####################################
# String formatting functions

def rmv_xtra_space(string):         # Remove random spaces
    string = string.split()
    string = ' '.join(string)
    return string

def rmv_fullstop(string):           # Remove fullstops at the end
    if string[-1] == '.':
        string = string[:-1]
    return string

def convert_or(string):             # Convert all "or"s to "OR"s
    for i in range(len(string) - 1):
        if string[i:i+2] == 'or':
            string = string[0:i] + "OR" + string[i+2:]
    return string

def convert_and(string):            # Convert all "and"s to "AND"s
    for i in range(len(string) - 2):
        if string[i:i+3] == 'and':
            string = string[0:i] + "AND" + string[i+3:]
    return string

#####################################

def convert_uoc(prereq_arr):        # Converts all uoc prerequisites into a certain format below
    i = 0; j = 1                    #  uoc | prereq
    while i < len(prereq_arr):
        
        if prereq_arr[i].isnumeric():
            uoc = prereq_arr[i]
            
            while  (i+j < len(prereq_arr) and
                    not prereq_arr[i+j].isnumeric() and 
                    prereq_arr[i+j] != "COMP" and
                    not prereq_arr[i+j][0] == "("):

                j += 1
            
            if i+j >= len(prereq_arr):   # Completion of ___ units of credit
                uoc = uoc + "|" + ""
            elif prereq_arr[i+j][0] == "(":    # Completion of ___ units of credit in (courses)
                uoc = uoc + "|" + prereq_arr[i+5][1:-1]
                j += 1
            elif prereq_arr[i+j] == "COMP":     # Completion of ___ units of credit in COMP courses
                uoc = uoc + "|" + "COMP"
                j += 2
            elif prereq_arr[i+j].isnumeric():     # Completion of ___ units of credit in level _ COMP courses
                uoc = uoc + "|" + "COMP" + str(prereq_arr[i+j])
                j += 3
            
            prereq_arr = prereq_arr[:i] + [uoc] + prereq_arr[i+j:]
            j = 1
            
        i += 1
    
    return prereq_arr

def in_course_list(course, course_list):        # Checks if a course is in the course_list
    if course in course_list:
        return True
    return False

def eval (uoc, prereq, course_list):            # Handles the uoc requirements
    
    uoc = int(uoc) / 6; prereq = prereq.split(", ")
    if len(prereq) > 1:        # if prereq was a list
        intersect = set(course_list) & set(prereq)

        if len(intersect) >= uoc:
            return True
        
    else:       # if prereq was of the form ["COMP1"] for lvl 1 courses etc
        count = 0; course_type = prereq[0]; 
        for course in course_list:
            if course_type in course:
                count += 1
            
        if count >= uoc:
            return True
        
    return False

def is_unlocked(course_list, target_course):
    if len(target_course) != 8:         # Recursive
        string = target_course
    else:
        string = CONDITIONS[target_course]      # First time

    string = rmv_xtra_space(string)
    string = rmv_fullstop(string)
    string = convert_or(string)
    string = convert_and(string)
    
    condition_arr = []
    prereq_arr = string.split()

    i = 0; j = 0; open_bracket = -1; end = False

    # Makes anything in brackets into one element AND 
    # Copies all "AND"s / "OR"s into condition_arr

    while i < len(prereq_arr):

        if prereq_arr[i][0] == "(":
            while i+j < len(prereq_arr):
                
                # Checks to see which ")" is the matching one to the "(" found
                # In case of multiple brackets e.g. (COMP1511 AND (COMP1521))

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
            j = 0; open_bracket = -1; end = False
        
        elif prereq_arr[i] == "AND" or prereq_arr[i] == "OR":
            condition_arr.append(prereq_arr[i])
            prereq_arr.remove(prereq_arr[i])
            i -= 1

        i += 1
    
    prereq_arr = convert_uoc(prereq_arr)
    
    i = 0
    while i < len(prereq_arr):
        course_type  = prereq_arr[i][:4]
        
        if course_type == "COMP" or course_type == "MTRN" or course_type == "DPST" or course_type == "MATH" or course_type == "ELEC":
            prereq_arr[i] = in_course_list(prereq_arr[i], course_list)
        elif course_type[0] == "(":                                             # Bracketed element
            prereq_arr[i] = is_unlocked(course_list, prereq_arr[i][1:-1])
        elif course_type[0].isnumeric():                                        # UOC prereq element
            temp = prereq_arr[i].split("|")
            prereq_arr[i] = eval(temp[0], temp[1], course_list)
        else:                                                                   # Irrelevant words e.g. Condition of, Prerequisite:
            prereq_arr.remove(prereq_arr[i])
            i -= 1
        
        i += 1
    
    # len(condition_arr) == len(prereq_arr) + 1     ALWAYS

    for condition in condition_arr:
        if condition == "OR":
            prereq_arr = [prereq_arr[0] or prereq_arr[1]] + prereq_arr[2:]
        if condition == "AND":
            prereq_arr = [prereq_arr[0] and prereq_arr[1]] + prereq_arr[2:]
    
    return prereq_arr[0]

print(is_unlocked(["COMP2511", "COMP6789", "COMP3141", "COMP3821"], "COMP4601"))