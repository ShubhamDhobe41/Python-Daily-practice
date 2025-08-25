# remove given word from list ad strip it at same time 
def rem(l, word):
    # Strip all items first
    l = [item.strip() for item in l]
    
    # Remove the given word if it exists
    if word in l:
        l.remove(word)
    return l

l= ["harry", "rohan","shubham","anand"]
print(rem(l,"shubham"))
