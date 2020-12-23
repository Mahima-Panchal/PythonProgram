f = lambda n: [(2*(n-i-1)*" "+"**"*(2*i+1)+"\n")*2 for i in range(n)]


[print(f"N = {i}\n{''.join(f(i))}\n\n") for i in (2, 5)]