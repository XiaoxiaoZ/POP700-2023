M=[2,3,4;2,3,4;3,4,5]
array = extractLine(M,2)
assert(isequal(array,[2,3,4]),'not equel')
function array=extractLine(M,index)
%To extract a whole line from a bigger matrix
array=[2,3,4]
end