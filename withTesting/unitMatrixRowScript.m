simplatrix=    [-10    20     1     0     0    22;
                    5    10     0     1     0    49;
                    1     0     0     0    -1     4;
                    1    -4     0     0     0     0]
minIcol = 1
minIrow = 2

outputMatrix = [  -10.0000   20.0000    1.0000         0         0   22.0000;
                    1.0000    2.0000         0    0.2000         0    9.8000;
                    1.0000         0         0         0   -1.0000    4.0000;
                    1.0000   -4.0000         0         0         0         0]

assert(isequal(unitMatrixRow(simplatrix,minIrow,minIcol),outputMatrix))

function [outputMatrix] = unitMatrixRow(simplexMatrix,minIrow,minIcol)
%unitMatrixRow Do matrix operation that the choosen number become 1

end