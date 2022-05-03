# '''
# Pattern 1

# *****
# *****
# *****
# *****
# *****
# '''

# for i in range(5):
#     for j in range(5):
#       print('*',end=' ')
#     print()




# '''
# pattern 2

# 11111
# 22222
# 33333
# 44444
# 55555

# '''
# for i in range(1,6):
#     for j in range(1,6):
#       print(i,end=' ')
#     print()


# '''
# Pattern 3

# 1
# 22
# 333
# 4444
# 55555

# '''
# for i in range(1,6):
#     for j in range(1,i+1):
#        print(i,end=' ')
#     print()

# '''
# pattern 4

# *****
# ****
# ***
# **
# *
# '''

# for i in range(5):
#     for j in range(i-1,4):
#        print('*',end=' ')
#     print()




# '''


# pattern 5

#         *
#       * * 
#     * * *
#   * * * *
# * * * * *

# '''

# for i in range(0,5):
#    for j in range(0,5-i-1):
#       print(" ",end=' ')
#    for j in range(0,i+1):
#       print('*',end=' ')
#    print()










# '''
# pattern 6

#     *
#    ***
#   *****
#  *******
# *********
# '''
# # n = int(input("enter num of rows: "))
# for i in range(0,5):
#    for j in range(0,5-i-1):
#       print(end=" ")
#    for j in range(i+1):
#       print('*',end=' ')
#    print()

