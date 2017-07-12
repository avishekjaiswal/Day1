# print " ","*"*3," "
# for i in range(2):
# 	print "*"," "*2,"*"
# print "*"*5
# for i in range(3):
# 	print "*"," "*2,"*"


result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);