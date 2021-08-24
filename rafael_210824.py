print(" Question 2 *********************************")
luxo=["gol","like","love"]
reta=("navio","barco","lancha")
ashe={"banana1":"banana2"}
oil={"hippo":"hipopótamo", "cem":100, "market":luxo, "tubo":reta, "dado":ashe}
print(" Question 3 *********************************")
print(oil)
print(" Question 4 *********************************")
for key in oil.keys():
    print(key)
print(" Question 5 *********************************")
for value in oil.values():
    print(value)
print(" Question 6 *********************************")
for item in oil.items():
    print(item)
print(" Question 7 *********************************")
for key,value in oil.items():
    print("\nkey: " + key)
    print("Value: " + str(value))
print(" Question 8 *********************************")
