#ned to use nested for loops

# 
# |""""""""""|
#  \::::::::/
#   \::::::/
#    \::::/
#     \::/
#      ||
#     /::\
#    /::::\
#   /::::::\
#  /::::::::\
# |""""""""""|



def hourglass():
	
	for i in range(2):
		
		if i==1:
			print("      ||")

		print("|","\""*10,"|")
		
		for n in range(4,0,-1):
			print(" "*n,"/",":"*(8-2*n),"\\")	
			
# def hourglass():
# 	print("|","\""*10,"|")
# 	
# 	for i in range(4):
# 		print(" "*i,"\\",":"*(8-2*i),"/")	
# 		
# 	print("      ||")
# 	
# 	for i in range(4):
# 		print(" "*(3-i),"/",":"*2*(i+1),"\\")
# 		
# 	print("|","\""*10,"|")
# 	
	
# def hourglass():
# 	
# 	for i in range(2):
# 		print("|","\""*10,"|")
# 		
# 		for i in range(4):
# 			print(" "*i,"\\",":"*(8-2*i),"/")	
# 		
# 		print("      ||")
# 	
# 		for i in range(4):
# 			print(" "*(3-i),"/",":"*2*(i+1),"\\")
	

hourglass()

