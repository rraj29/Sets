farm_animals = {"cow", "sheep", "hen"}

print(farm_animals)
for animal in farm_animals:
    print(animal)

print("*"*45)

wild_animals = set(["lion", "tiger", "hare", "Panther", "elephant"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

even = set(range(0,40,2))
print(even)
print(len(even))
squares_tuple = (1,4,9,16,25,36)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))
print("="*54)

print(squares.intersection(even))
print(squares & even)

print(len(squares.intersection(even)))

print("even minus squares")
print(even.difference(squares))
print(even-squares)

print("squares minus even")
print(squares.difference(even))
print(squares-even)
print("-"*52)
print(even)
print(squares)
# even.difference_update(squares)     #->   this won't produce a new set. but it'll update the tuple-(even) as (even-square)
# print(even)                         #->   just like the list.sort() function

print("symmetric even minus squares")       #  A symmetric B = (A union B)-(A intersection B)
print(sorted(even.symmetric_difference(squares)))
print("symmetric squares minus mean")
print(sorted(squares.symmetric_difference(even)))

squares.discard(1)
squares.discard(9)
squares.remove(25)
squares.discard(8)   # NOTE 8 is NOT in the set, yet it shows NO error
print(squares)
#squares.remove(8)    # NOTE 8 is NOT in the set, so it SHOWS ERROR.  Better to use DISCARD
if 8 in squares:
    squares.remove(8)

#using TRY and EXCEPT
try:
    squares.remove(8)
except:
    print("The number 8 does not exist in the set.")


print("we have already removed 1 and 25 from the squares in above steps, "
      "so only left are 4, 16, 36. They are all even.")
if squares.issubset(even):
    print("Squares is a subset of even.")

if even.issuperset(squares):
    print("Even is superset of squares.")
