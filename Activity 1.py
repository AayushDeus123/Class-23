#Dictionery Data Structure (Get rid of duplicates)
student_data = {'Id-1' : {'Name' : 'Sara', 
                          'Class' : 'VII',
                          'Subjects' : 'Maths, English, Science'},
                'Id-2' : {'Name' : 'Aayush',
                          'Class' : 'X',
                          'Subjects' : 'Maths, English, Science'},
                'Id-3' : {'Name' : 'Sara', 
                          'Class' : 'VII',
                          'Subjects' : 'Maths, English, Science'},
                'Id-4' : {'Name' : 'Surya',
                          'Class' : 'XI',
                          'Subjects' : 'Maths, English, Science'}
                }
result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
        
print(result)