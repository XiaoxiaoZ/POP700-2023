%test if all entries in the bottom row are zero or positive
flag = isPositive([1 -2 -1 0 2])
assert(~flag)
flag = isPositive([1 2 1 0 2])
assert(flag)
function bool=isPositive(a)
 %returns true if all the values in the array (a) are positive. Otherwise
 %it returns false
 bool=false
end