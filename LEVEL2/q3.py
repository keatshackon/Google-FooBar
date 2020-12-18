def solution(pegs):
    d = [pegs[x+1]-pegs[x] for x in range(len(pegs)-1)]
    x = 0
    for i in d:
        x = i - x

    if len(d)%2 == 0:
        sol =  [x*-2,1]
    elif len(d)%2 == 1:
        if x*2 % 3 == 0:
            sol = [x*2/3,1]
        else:
            sol = [x*2,3]

    gs = [float(sol[0])/float(sol[1])]
    x = gs[0]
    for i in d:
        x = i - x
        gs.append(x)
    if any([True for x in gs if x<=1]):
        return [-1,-1]
    else:
        return sol
print(answer([4,30,50]))
