name1="Shayan"
name2="Hassan"

name3=name1+" "+name2
print(name3)


# Properties

print(len(name3))
print(name3[0:])
print(name3[0:6])  
print(name3[7:])    
print(name3[:6])    
print(name3[-6:])   

name3.endswith("n")
name3.capitalize()
new=name3.replace("Shayan", "Noman")
print(new)
find=name3.find("Sh")
print(find)