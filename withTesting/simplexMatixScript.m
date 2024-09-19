inputMatrix = [ -10 20 22;...
                5 10 49;...
                1 0 4;...
                1 -4 0]
inequality = [1;1;-1]
simplatrix=    [-10    20     1     0     0    22;
                    5    10     0     1     0    49;
                    1     0     0     0    -1     4;
                    1    -4     0     0     0     0]

assert(isequal(simplexMatrix(inputMatrix,inequality),simplatrix))
function simplexMatrix = simplexMatrix(inputMatrix,inequality)
%SIMPLEXMATRIX take a input matrix and inequality vector, generate matrix for interation

end