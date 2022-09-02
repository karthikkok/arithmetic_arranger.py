def arithmetic_arranger(problems, results=False):      
    
    if len(problems) > 5 :
        return('Error: Too many problems.')

    line1 = list()
    line2 = list()
    line3 = list()
    line4 = list()
    for op in problems :
        if op.find('+') == -1 and op.find('-') == -1 :
            return("Error: Operator must be '+' or '-'.")
        terms = op.split()
      
        if terms[0].isnumeric() and terms[2].isnumeric() : 
            op1 = int(terms[0])
            op2 = int(terms[2])
        else : 
            return('Error: Numbers must only contain digits.')

        if len(terms[0]) > 4 or len(terms[2]) > 4 :
            return('Error: Numbers cannot be more than four digits.')
             
        offset = len(terms[0]) - len(terms[2])
        
        if offset > 0 :
            term = 2           
        elif offset < 0 :
            term = 0
            offset = offset * -1 
            

        index = 0         
        while index < offset :
            terms[term] = ' ' + terms[term]
            index = index + 1        
        
        terms[0] = '  ' + terms[0] 
        terms[2] = terms[1] + ' ' + terms[2]

        line = ''
        for ch in terms[2] : 
            line = line + '-'

        if results is True :
            if terms[1] == '+' :
                res = str(op1 + op2)   
            elif terms[1] == '-' :
                res = str(op1 - op2)   

                
            index = 0
            while index < ((len(terms[2]) - len(res) + 1)) : 
                res = ' ' + res
                index = index + 1
            line4.append(res)

        line1.append(terms[0])
        line2.append(terms[2])
        line3.append(line)
        

    l1 = ''
    for e1 in line1 :
       l1 = l1 + e1 + '    '
    l1 = l1.rstrip()

    l2 = ''
    for e2 in line2 :
        l2 = l2 + e2 + '    '
    l2 = l2.rstrip()

    l3 = ''
    for e3 in line3 : 
        l3 = l3 + e3 + '    '
    l3 = l3.rstrip()

    l4 = ''
    for e4 in line4 : 
        l4 = l4 + e4 + '    '
    l4 = l4.rstrip()

    arranged_problems = l1 + '\n' + l2 + '\n' + l3 
    if results is True :
       arranged_problems = arranged_problems + '\n' + l4
    return arranged_problems
