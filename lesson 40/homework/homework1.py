#1
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m

#2
def make_upper_case(s):
    return s.upper()

# 3
def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)

# 4
def are_you_playing_banjo(name):
    if name.lower().startswith("r"):
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


#5
def abbrev_name(name):
    first, last = name.split() 
    return f"{first[0].upper()}.{last[0].upper()}"  