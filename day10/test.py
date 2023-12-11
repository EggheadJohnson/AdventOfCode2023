line = 'FJ||L7|LJLJFJ|LJL7FJLJL7L-7||||F-JFJ||LJLJLJ|L7FJL7SFJL7L7|FJLJLJLJL7|L-7F-7'
o = ''
prevCorner = None
for j, c in enumerate(line):

    if c in '|':
        o += 'p'
    elif c in 'LF':
        o += 'p'
        prevCorner = c
    elif c in 'J7':
        if c == 'J' and prevCorner == 'L':
            o += 'p'
        elif c == '7' and prevCorner == 'F':
            o += 'p'
        else:
            o += '.'
        prevCorner = None
    else:
        o += '.'
    # print(j, c, o)
print(line)
print(o)
'||F7L-7FJL7|LJF-7'
'ppppp..p.p.pppp.p'
