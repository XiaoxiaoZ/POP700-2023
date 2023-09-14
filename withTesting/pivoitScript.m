simplatrix=    [-10    20     1     0     0    22;
                    5    10     0     1     0    49;
                    1     0     0     0    -1     4;
                    1    -4     0     0     0     0]

minV = 1
minIcol = 1
minIrow = 3

simplatrixNext = [0    20     1     0   -10    62;
     0    10     0     1     5    29;
     1     0     0     0    -1     4;
     0    -4     0     0     1    -4]

assert(isequal(simplatrixNext,pivot(simplatrix,minIrow,minIcol)))

function [outputMatrix] = pivot(simplexMatrix,minIrow,minIcol)
%pivot Do pivoit process

end