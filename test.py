buf_ = "some text"
colors = [30, 31, 32, 33, 34, 35, 36, 40, 41, 42, 43, 44, 45, 46, 47]
for i in colors:
    print(buf_, f"\x1b[31m日本語は{buf_}\x1b[0m\n")

'''
30 black
31 red
32 green
33 yellow
34 blue
35 purple
36 sky blue
40 black back
41 red back
42 green back
43 yellow back(difficult read)
44 blue back
45 purple back
46 sky blue back
47 white back(for hidden?)
'''
