"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()
    
# Just realized that it was probably intended for us to use CONDITIONS here (never worked w JSON before so just ignored it lol)
# I'll try think up and put up another solution using it in another branch

def is_unlocked(course_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """

    def eval (uoc, courses):        # Checks whether the UOC condition has been met

        if len(courses) > 1:        # if courses was a list
            intersect = set(course_list) & set(courses)
            if len(intersect) >= uoc:
                return intersect.pop()

        else:       # if courses was of the form ["COMP1"] for lvl 1 courses etc
            count = 0; course_type = courses[0]; 
            for course in course_list:
                if course_type in course:
                    count += 1
                    sample = course
            
            if count >= uoc:
                return sample
        
        return "UOC NOT MET"
    
    """
    Dic Format Example  -    "Course": [[Arr1], [Arr2], final_condition]

    For each Array within dic["Course"], if the last element was OR, check whether
    any one of the courses within the Array exists in course_list

    if the last element was AND, check whether the Array (without the AND) is a 
    subset of course_list

    For Arrays containing the eval function, the eval functioned returned a course
    present in course_list if the UOC condition was met (TRUE), 
    and "UOC NOT MET" if not (FALSE). This would provide the same desired output
    when combined with the AND or OR in the arrays

    For some conditions like that of COMP3151, I modified slightly to fit my format
    COMP3151: COMP1927 OR ((COMP1521 OR DPST1092) AND COMP2521)     -->
    COMP3151: COMP1927 OR (COMP1521 AND COMP2521) OR (DPST1092 AND COMP2521)
    """

    dic = {     
        "COMP1511": [["AND"], "OR"],
        "COMP1521": [["COMP1511", "DPST1091", "COMP1911", "COMP1917", "OR"], "OR"],
        "COMP1531": [["COMP1511", "DPST1091", "COMP1917", "COMP1921", "OR"], "OR"],
        "COMP2041": [["COMP1511", "DPST1091", "COMP1917", "COMP1921", "OR"], "OR"],
        "COMP2111": [["MATH1081", "OR"], ["COMP1511", "DPST1091", "COMP1921", "COMP1917", "OR"], "AND"],
        "COMP2121": [["COMP1917", "COMP1921", "COMP1511", "DPST1091", "COMP1521", "DPST1092", "OR"], ["COMP1911", "MTRN2500", "AND"], "OR"],
        "COMP2511": [["COMP1531", "OR"], ["COMP2521", "COMP1927", "OR"], "AND"],
        "COMP2521": [["COMP1511", "DPST1091", "COMP1917", "COMP1921", "OR"], "OR"],
        "COMP3121": [["COMP1927", "COMP2521", "OR"], "OR"],
        "COMP3131": [["COMP2511", "COMP2911", "OR"], "OR"],
        "COMP3141": [["COMP1927", "COMP2521", "OR"], "OR"],
        "COMP3151": [["COMP1927", "OR"], ["COMP1521", "COMP2521", "AND"], ["DPST1092", "COMP2521", "AND"], "OR"],
        "COMP3153": [["MATH1081", "OR"], "OR"],
        "COMP3161": [["COMP1927", "COMP2521", "OR"], "OR"],
        "COMP3211": [["COMP3222", "ELEC2141", "OR"], "OR"],
        "COMP3900": [["COMP1531", "OR"], ["COMP2521", "COMP1927", "OR"], [eval(102 / 6, [""]), "OR"], "AND"],
        "COMP3901": [[eval(12 / 6, ["COMP1"]), "OR"], [eval(18 / 6, ["COMP2"]), "OR"], "AND"],
        "COMP3902": [["COMP3901", "OR"], [eval(12 / 6, ["COMP3"]), "OR"], "AND"],
        "COMP4121": [["COMP3121", "COMP3821", "OR"], "OR"],
        "COMP4128": [["COMP3821", "OR"], ["COMP3121", eval(12 / 6, ["COMP3"]), "AND"], "OR"],
        "COMP4141": [["MATH1081", "OR"], ["COMP1927", "COMP2521", "OR"], "AND"],
        "COMP4161": [[eval(18 / 6, [""]), "OR"], "OR"],
        "COMP4336": [["COMP3331", "OR"], "OR"],
        "COMP4418": [["COMP3411", "OR"], "OR"],
        "COMP4601": [["COMP2511", "COMP2911", "OR"], [eval(24 / 6, [""]), "OR"], "AND"],
        "COMP4951": [[eval(36 / 6, ["COMP"]), "OR"], "OR"],
        "COMP4952": [["COMP4951", "OR"], "OR"],
        "COMP4953": [["COMP4952", "OR"], "OR"],
        "COMP9301": [[eval(12 / 6, ["COMP6443", "COMP6843", "COMP6445", "COMP6845", "COMP6447"]), "OR"], "OR"],
        "COMP9302": [["COMP6441", "COMP6841", "OR"], [eval(12 / 6, ["COMP6443", "COMP6843", "COMP6445", "COMP6845", "COMP6447"]), "OR"], "AND"],
        "COMP9417": [["MATH1081", "OR"], ["COMP1531", "COMP2041", "COMP1927", "COMP2521", "OR"], "AND"],
        "COMP9418": [["MATH5836", "COMP9417", "OR"], "OR"],
        "COMP9444": [["COMP1927", "COMP2521", "MTRN3500", "OR"], "OR"],
        "COMP9447": [["COMP6441", "COMP6841", "COMP3441", "OR"], "OR"],
        "COMP9491": [[eval(18 / 6, ["COMP9417", "COMP9418", "COMP9444", "COMP9447"]), "OR"], "OR"]
    }

    prereq = dic[target_course]
    truth_table = []
    final_condition = prereq.pop()

    for arr in prereq:
        condition = arr.pop()
        if condition == "OR":
            truth_table.append(not set(arr).isdisjoint(course_list))
        elif condition == "AND":
            truth_table.append(set(arr) <= set(course_list))
    
    if final_condition == "AND":
        if False not in truth_table:
            return True
        else:
            return False
    elif final_condition == "OR":
        if True in truth_table:
            return True
        else:
            return False
