from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
m_r = append(m,[['Avg',12,15,13,11]],0)

print(m_r)

m_c = append(m,[[23],[24],[25],[26],[27],[28],[29]],1)

print(m_c)

m = delete(m,[2],0)

print(m)

m = delete(m,s_[2],1) # similar as above but column here

print(m)