guests = ['jinpin', 'Lily', 'lianxia']
message = "Invite " + guests[0].title() + " to my party."
print(message)

print(guests[1] + " cannot come.")
guests[1] = 'haerbin-gl'
print(guests)

print('Find a bigger room')
guests.insert(0, 'guangzhou-gl')
guests.insert(2, 'bj-gl')
guests.append('yuanxin')
print(guests)

print('room is too small')
name = guests.pop()
print('sorry ' + name)
name = guests.pop()
print('again ' + name)
guests.pop()
guests.pop()
print(guests)

print(guests[0] + ", u are my welcome")
print(guests[1] + ", u are my mvp")

del guests[0:2]
print('empty room, ' + str(guests))
