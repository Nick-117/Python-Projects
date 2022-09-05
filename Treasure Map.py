# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# # The first digit is the column(vertical) and the second digit is row(horizonal)

# we need to somehow code the input into index [] numbers

# we need to change the input number into an x by first taking the [] indexed value then turning it into an "x"  

position_num = int(position)

# print(position_num)





tgtFirst_digit = position[0]
tgtSecond_digit = position[1]



Column_num = int(tgtFirst_digit)
Row_num = int(tgtSecond_digit)

Column_sub1 = Column_num -1
Row_sub1 = Row_num -1

# print(Column_num + Row_num)


map[Row_sub1][Column_sub1] = "x"

# map[Row_num]

# map[Column_num][Row_num] = "c"


# print(map[position_num])

# split_num_position = position_num.split(",")

# print(split_num_position)

# "x" = position


 



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")