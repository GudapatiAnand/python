# anand={1:"names","sno":2.2,11:True}
# print(type(anand))
# anand[1]="Name"
# print(anand)

# leela={"sno":1,"name":"Anand","phno":[12,13]}
# print(leela.get("name"))
# print(leela.keys())
# print(leela.values())
# print(leela.items())
# leela.update({"food":"biryani"})
# print(leela)
# leela.pop("sno")
# print(list(leela))


# leela={"sno":1,"name":"Anand","phno":[12,13]}
# for k,l in leela.items():
#     print(k,l)


phani={
    1:'a',
    2:'b',
    3:{1:'aa'}
}
print(phani[3][1])