# non primitive data 
# list  (ordered ,indexed ,mutable ,duplicate allowed, mutable and immutable)
# tuple (ordered, indexed ,immutable, duplicate allowed, )
# set  (unordered , notindexed ,mutable, duplicate not allowed,only immutable)
# dict  (ordered, keyed ,mutable ,duplicate allowed, only immutable )

# list
# list=[1,2,3,4]
# print(list)
# print(list[2])
# a=list.append(78)
# print(list)


# tuple=(1,2,3,4)
# print(tuple)
# print(tuple[3])


# set={1,2,3,4}
# print(set)
# print(set[2])
# a=set.add(67)
# print(set)


# dict={"name":"sonali","age":20}
# print(dict)
# print(dict["name"])


list=[10,20,40,30,70,40]
# list.append(50)           add last index
# list.extend([50,60,70])    merge 2 array 
# list.insert(3,90)
# list.insert(80,7)
# list.remove(40)
# list.pop(2)            last in first out remove in last
# list.clear()           all are remove
a=list.index(70)
print(a)
print(list)



tuple=(1,2,3,4)
print(tuple.count(1))
print(tuple.index(3))

set_A={1,2,3,4}
set_B={4,5,6,7}
set_A.add(5)
# set_A.update([5,8])
# set_A.update([9,8])
# set_A.update([5,8])
# set_A.remove(10)    remove re error 
# set_A.discard(10)         discard re doesnot show error
u_set=set_A.union(set_B)
u_set=set_A.intersection(set_B)
u_set=set_A.difference(set_B)
u_set={5,4}.issubset(set_B)
print(u_set) 


dict={"name":"sonali","age":22}
print(dict.get("name"))
print(dict.keys())
print(dict.values())
