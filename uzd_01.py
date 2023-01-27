saraksts = [2, 3.75, "ABC", 59.354, 6, 7.7777, 8, 9, [1, 2]]

saraksts2 = [x for x in saraksts if isinstance(x, int)]
print(saraksts2)

