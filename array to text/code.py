
"""
    You probably know the "like" system from Facebook and other pages. 
    People can "like" blog posts, pictures or other items. We want to create 
    the text that should be displayed next to such an item.

    Implement the function which takes an array containing the names of people 
    that like an item. It must return the display text as shown in the examples:

    []                                -->  "no one likes this"
    ["Peter"]                         -->  "Peter likes this"
    ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
    Note: For 4 or more names, the number in "and 2 others" simply increases.

"""


def likes(names):
    num_likes = len(names)
    if num_likes == 0:
        return "no one likes this"
    elif num_likes == 1:
        return f"{names[0]} likes this"
    elif num_likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {num_likes-2} others like this"

print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))



"""
    In this program, we first count the number of likes (num_likes) 
    by using the len() function on the names array.We then use an if statement 
    to check the number of likes and return the appropriate display text.

    If there are no likes (num_likes == 0), we return "no one likes this". 
    If there is only one like (num_likes == 1), we return the name of the person 
    followed by "likes this" (using an f-string). If there are two likes (num_likes == 2), 
    we return the names of the two people joined by "and" (also using an f-string). 
    If there are three likes (num_likes == 3), we return the names of the three people separated by commas, 
    with the last name joined by "and". Finally, if there are four or more likes (num_likes >= 4), 
    we return the names of the first two people joined by "and", followed by the number of remaining 
    likes (num_likes-2) and the string "others like this" (using an f-string).

"""