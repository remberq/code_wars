"""
CodeWars Katas.

"""
import operator
from math import sqrt

"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer.
"""


def square_digits(num):
    result = int(''.join(map(lambda number: str(int(number) ** 2), str(num))))
    return result


"""

You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

"""


def area_or_perimeter(l, w):
    if l == w:
        return l * w
    return (l + w) * 2


"""

You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

"""


def likes(names):
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) < 3:
        return f'{names[0]} and {names[1]} likes this'
    elif len(names) < 4:
        return f'{names[0]}, {names[1]} and {names[2]} likes this'
    else:
        return f'{names[0]}, {names[1]} and {len(names[2:])} others like this'


"""

Description:
Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. 
For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

Examples

remove("Hi!") === "Hi!"
remove("Hi!!!") === "Hi!"
remove("!Hi") === "Hi!"
remove("!Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!"
remove("Hi") === "Hi!"

"""


def remove(s):
    return s.replace('!', '') + '!'


"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

"""


def anagrams(word, words: list):
    return [i for i in words if sorted(i) == sorted(list(word))]


"""

Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => 
returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

"""


def spin_words(sentence):
    temp = []
    for item in sentence.split():
        if len(item) > 4:
            temp.append(item[::-1])
        else:
            temp.append(item)
    return ' '.join(temp)


"""
Write a function, which takes a non-negative integer (seconds) as input 
and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(seconds):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 3600 % 60
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


"""
Implement the function unique_in_order which takes as argument a sequence 
and returns a list of items without any elements with the same value next to each other 
and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(iterable):
    x = [iterable[0]]
    for i in iterable[1:]:
        if i != x[-1]:
            x.append(i)
    return x


"""
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input 
and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. 
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
"""


def find_missing_letter(chars):
    data = "abcdefghijklmnopqrstuvwxyz"
    if chars[0].isupper():
        check = sorted(data.upper())
    else:
        check = sorted(data)
    temp = [index for index, val in enumerate(check) if val in chars]
    index = [i for i in range(temp[0], temp[-1] + 1) if i not in temp]
    return check[index[0]]


"""
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string. 
You don't have to worry with strings with less than two characters.
"""


def remove_char(s):
    return s[1:-1]


"""
Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""


def create_phone_number(n):
    temp = list(map(str, n))
    return f'({"".join(temp[:3])}) {"".join(temp[3:6])}-{"".join(temp[6:])}'


"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(sentence):
    import re
    return len(re.findall(r'[aeiou]', sentence))


"""
In this kata you have to create all permutations of an input string and remove duplicates, if present. 
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.
"""


def permutations(string: str):
    from itertools import permutations
    temp = list(set(''.join(val) for val in permutations(string)))
    return temp


"""
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(array):
    return sorted(array, key=lambda x: x == 0)


"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""


def zero(func=None):
    if func:
        return int(eval('0' + func))
    return 0


def one(func=None):
    if func:
        return int(eval('1' + func))
    return 1


def two(func=None):
    if func:
        return int(eval('2' + func))
    return 2


def three(func=None):
    if func:
        return int(eval('3' + func))
    return 3


def four(func=None):
    if func:
        return int(eval('4' + func))
    return 4


def five(func=None):
    if func:
        return int(eval('5' + func))
    return 5


def six(func=None):
    if func:
        return int(eval('6' + func))
    return 6


def seven(func=None):
    if func:
        return int(eval('7' + func))
    return 7


def eight(func=None):
    if func:
        return int(eval('8' + func))
    return 8


def nine(func=None):
    if func:
        return int(eval('9' + func))
    return 9


def plus(func):
    return f'+ {func}'


def minus(func):
    return f'- {func}'


def times(func):
    return f'* {func}'


def divided_by(func):
    return f'// {func}'


"""
Pete likes to bake some cakes. He has some recipes and ingredients. 
Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and 
returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts 
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""


def cakes(recipe, available):
    check = []
    for key, value in recipe.items():
        if not available.get(key):
            return 0
        check.append(int(available[key] / value))
    return min(check)


"""
You need to write a function, that returns the first non-repeated character in the given string.

If all the characters are unique, return the first character of the string.
If there is no unique character, return null in JS or Java, and None in Python.

You can assume, that the input string has always non-zero length.

Example
first_non_repeated("test") # returns "e"
first_non_repeated("teeter") # returns "r"
first_non_repeated("trend") # returns "t" (all the characters are unique)
first_non_repeated("aabbcc") # returns None (all the characters are repeated)
"""


def first_non_repeated(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None


"""
Given a string and an array of index numbers, 
return the characters of the string rearranged to be in the order specified 
by the accompanying array.

Ex:

scramble('abcd', [0,3,1,2]) -> 'acdb'

The string that you will be returning back will have: 
'a' at index 0, 'b' at index 3, 'c' at index 1, 'd' at index 2, 
because the order of those characters maps to their corresponding numbers 
in the index array.

In other words, put the first character in the string at the index 
described by the first element of the array

You can assume that you will be given a string and array of equal length and 
both containing valid characters (A-Z, a-z, or 0-9).
"""


def scramble(string, array):
    data = dict(zip(array, string))
    result = ''
    for i in range(len(array)):
        result += data.get(i)
    return result


"""
You are Saitama (a.k.a One Punch Man), 
and you are fighting against the monsters! You are strong enough 
to kill them with one punch, but after you punch 3 times, 
one of the remaining monsters will hit you once.

Your health is health; number of monsters is monsters, 
damage that monster can give you is damage.

Task
Write a function that will calculate:

how many hits you received, how much damage you received and 
your remaining health.

if your health is <= 0, you die and function should return "hero died".

Examples
killMonsters(100, 3, 33); // => "hits: 0, damage: 0, health: 100"
killMonsters(50, 7, 10); // => "hits: 2, damage: 20, health: 30"
Note
All numbers are strictly positive. Your function should always return a string.
"""


def kill_monsters(health, monsters, damage):
    hits = int(monsters / 3 if monsters % 3 else (monsters / 3) - 1)
    damage = damage * hits
    health = health - damage
    if health <= 0:
        return 'hero died'
    return f'hits: {hits}, damage: {damage}, health: {health}'


"""
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Call nb_dig (or nbDig or ...) the function taking n and d as parameters and 
returning this count.

Examples:
n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

nb_dig(25, 1) returns 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
Note that 121 has twice the digit 1.
"""


def nb_dig(n, d):
    return sum(str(i * i).count(str(d)) for i in range(n + 1))


"""
Ask a small girl - "How old are you?". 
She always says strange things... Lets help her!

For correct answer program should return int from 0 to 9.

Assume test input string always valid and 
may look like "1 year old" or "5 years old", etc.. The first char is number only
"""


def get_age(age):
    return int(age[0])


"""
Given a string, swap the case for each of the letters.

e.g. CodEwArs --> cODeWaRS

Examples
""           ->   ""
"CodeWars"   ->   "cODEwARS"
"abc"        ->   "ABC"
"ABC"        ->   "abc"
"123235"     ->   "123235"
"""


def swap(string_):
    x = ''
    for i in string_:
        if i.isupper():
            x += i.lower()
        else:
            x += i.upper()
    return x


"""
Create the function that converts a given string into an md5 hash. 
The return value should be encoded in hexadecimal.

Code Examples
passHash("password") // --> "5f4dcc3b5aa765d61d8327deb882cf99"
passHash("abc123") // --> "e99a18c428cb38d5f260853678922e03"
"""


def pass_hash(str):
    import hashlib
    return hashlib.md5(str.encode()).hexdigest()


"""
Modify the spacify function so that it returns the given string 
with spaces inserted between each character.

spacify("hello world") # returns "h e l l o   w o r l d"
"""


def spacify(string):
    return ' '.join(string)


"""
Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible, containing distinct letters -
each taken only once - coming from s1 or s2.
"""


def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))


"""
Description
Frank just bought a new calculator. But, this is no normal calculator. 
This is a 'Sticky Calculator.

Whenever you add add, subtract, multiply or 
divide two numbers the two numbers first stick together:

For instance:

50 + 12 becomes 5012
and then the operation is carried out as usual:

(5012) + 12 = 5024
Task
It is your job to create a function which takes 3 parameters:

stickyCalc(operation, val1, val2)
which works just like Frank's sticky calculator

Some Examples
stickyCalc('+', 50, 12)     // Output: (5012 + 12) = 5024
stickyCalc('-', 7, 5)       // Output: (75 - 5) = 70
stickyCalc('*', 13, 20)     // Output: (1320 * 20 ) = 26400
stickyCalc('/', 10, 10)     // Output: (1010 / 10) = 101
"""


def sticky_calc(operation, val1, val2):
    first_num = str(round(val1)) + str(round(val2))
    result = f'{first_num} {operation} {str(round(val2))}'
    return round(eval(result))
