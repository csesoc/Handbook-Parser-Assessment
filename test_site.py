# OR = not set(a).disjoint(b) check if any of the elements exist in course_list
# AND = set(a) <= set(b) check if subset of course_list

# OR = if true in course_list then is good
# AND = if false not in course_list then is good
def eval (uoc, courses):
    
    if len(courses) > 1:

        intersect = set(course_list) & set(courses)

        if len(intersect) >= uoc:
            return intersect.pop()
    
    else:
        
        count = 0; course_type = courses[0]; 

        for course in course_list:
            if course_type in course:
                count += 1
                sample = course
        
        if count >= uoc:
            return sample
    
    return "UOC NOT MET"

course_list = []

dic = {
    "COMP1511": [["AND"], "AND"],
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

prereq = dic["COMP1511"]
truth_table = []
final_condition = prereq.pop()

print(course_list , prereq)

for arr in prereq:
    condition = arr.pop()
    if condition == "OR":
        print(course_list , arr)
        truth_table.append(not set(arr).isdisjoint(course_list))
    elif condition == "AND":
        print(course_list , arr)
        truth_table.append(set(arr) <= set(course_list))
print(truth_table)
if final_condition == "AND":
    if False not in truth_table:
        print("True")
    else:
        print("False")
elif final_condition == "OR":
    if True in truth_table:
        print("True")
    else:
        print("False")
