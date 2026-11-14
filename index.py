# SET-BASED PROGRAMS

# 1. Add Element
s = {1, 2, 3}
s.add(4)
print(s)

# 2. Remove Element
s = {1, 2, 3}
s.discard(2)
print(s)

# 3. Union
a, b = {1, 2}, {2, 3}
print(a | b)

# 4. Intersection
print(a & b)

# 5. Difference
print({1, 2, 3} - {2, 3})

# 6. Check Subset
print({1, 2}.issubset({1, 2, 3}))

# 7. Set Length
print(len({1, 2, 3}))

# 8. Clear Set
s = {1, 2, 3}
s.clear()
print(s)

# 9. Symmetric Difference
print({1, 2, 3} ^ {2, 3, 4})

# 10. List to Set
print(set([1, 2, 2, 3]))


# DICTIONARY-BASED PROGRAMS

# 11. Create Dictionary from Two Lists
keys = ["a", "b"]
values = [1, 2]
print(dict(zip(keys, values)))

# 12. Update Dictionary Value
d = {"a": 1}
d["a"] = 2
print(d)

# 13. Remove Key
d = {"a": 1, "b": 2}
d.pop("b")
print(d)

# 14. Check Key Existence
d = {"x": 1}
print("x" in d)

# 15. Iterate Dictionary
d = {"a": 10, "b": 20}
for k, v in d.items():
    print(k, v)

# 16. Dictionary Length
print(len({"x": 1, "y": 2}))

# 17. Merge Dictionaries
a = {"a": 1}
b = {"b": 2}
print({**a, **b})

# 18. Get Value with Default
d = {"a": 1}
print(d.get("b", 0))

# 19. Count Frequency of Elements
lst = [1, 2, 2, 3]
d = {}
for x in lst:
    d[x] = d.get(x, 0) + 1
print(d)

# 20. Invert Dictionary
d = {"a": 1, "b": 2}
print({v: k for k, v in d.items()})

# 21. Key with Maximum Value
d = {"a": 10, "b": 20, "c": 15}
print(max(d, key=d.get))

# 22. Sort Dictionary by Values
d = {"a": 3, "b": 1, "c": 2}
print(sorted(d.items(), key=lambda x: x[1]))

# 23. Dictionary of Squares
print({x: x*x for x in range(1, 4)})

# 24. Filter Dictionary by Value
d = {"a": 10, "b": 5, "c": 15}
print({k: v for k, v in d.items() if v > 10})

# 25. Combine Duplicate Keys
a = {"a": 1, "b": 2}
b = {"a": 3, "c": 4}
d = a.copy()
for k, v in b.items():
    d[k] = d.get(k, 0) + v
print(d)

# 26. Word Frequency
words = "apple banana apple".split()
d = {}
for w in words:
    d[w] = d.get(w, 0) + 1
print(d)

# 27. Remove Duplicate Values
d = {"a": 1, "b": 2, "c": 1}
result = {}
for k, v in d.items():
    if v not in result.values():
        result[k] = v
print(result)

# 28. Common Keys
a = {"a": 1, "b": 2}
b = {"b": 3, "c": 4}
print(list(a.keys() & b.keys()))

# 29. Swap Keys and Values Safely
d = {"x": 1, "y": 2}
print({v: k for k, v in d.items()})

# 30. Delete Items by Value
d = {"a": 1, "b": 2, "c": 1}
print({k: v for k, v in d.items() if v != 1})
