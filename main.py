from pyeda.inter import *


f = expr("((a11 ^ a12 | b11 ^ b12) & "
         "(a11 ^ a13 | b11 ^ b13) &"
         "(a11 ^ a14 | b11 ^ b14) &"
         "(a12 ^ a13 | b12 ^ b13) &"
         "(a12 ^ a14 | b12 ^ b14) &"
         "(a13 ^ a14 | b13 ^ b14)) &"

         "((a21 ^ a22 | b21 ^ b22) & "
         "(a21 ^ a23 | b21 ^ b23) &"
         "(a21 ^ a24 | b21 ^ b24) &"
         "(a22 ^ a23 | b22 ^ b23) &"
         "(a22 ^ a24 | b22 ^ b24) &"
         "(a23 ^ a24 | b23 ^ b24)) &"

         "((a31 ^ a32 | b31 ^ b32) & "
         "(a31 ^ a33 | b31 ^ b33) &"
         "(a31 ^ a34 | b31 ^ b34) &"
         "(a32 ^ a33 | b32 ^ b33) &"
         "(a32 ^ a34 | b32 ^ b34) &"
         "(a33 ^ a34 | b33 ^ b34)) &"

         "((a41 ^ a42 | b41 ^ b42) & "
         "(a41 ^ a43 | b41 ^ b43) &"
         "(a41 ^ a44 | b41 ^ b44) &"
         "(a42 ^ a43 | b42 ^ b43) &"
         "(a42 ^ a44 | b42 ^ b44) &"
         "(a43 ^ a44 | b43 ^ b44)) &"


         "((a11 ^ a21 | b11 ^ b21) & "
         "(a11 ^ a31 | b11 ^ b31) &"
         "(a11 ^ a41 | b11 ^ b41) &"
         "(a21 ^ a31 | b21 ^ b31) &"
         "(a21 ^ a41 | b21 ^ b41) &"
         "(a31 ^ a41 | b31 ^ b41)) &"

         "((a12 ^ a22 | b12 ^ b22) & "
         "(a12 ^ a32 | b12 ^ b32) &"
         "(a12 ^ a42 | b12 ^ b42) &"
         "(a22 ^ a32 | b22 ^ b32) &"
         "(a22 ^ a42 | b22 ^ b42) &"
         "(a32 ^ a42 | b32 ^ b42)) &"

         "((a13 ^ a23 | b13 ^ b23) & "
         "(a13 ^ a33 | b13 ^ b33) &"
         "(a13 ^ a43 | b13 ^ b43) &"
         "(a23 ^ a33 | b23 ^ b33) &"
         "(a23 ^ a43 | b23 ^ b43) &"
         "(a33 ^ a43 | b33 ^ b43)) &"

         "((a14 ^ a24 | b14 ^ b24) & "
         "(a14 ^ a34 | b14 ^ b34) &"
         "(a14 ^ a44 | b14 ^ b44) &"
         "(a24 ^ a34 | b24 ^ b34) &"
         "(a24 ^ a44 | b24 ^ b44) &"
         "(a34 ^ a44 | b34 ^ b44)) &"


         "((a11 ^ a22 | b11 ^ b22) & "
         "(a11 ^ a21 | b11 ^ b21) &"
         "(a11 ^ a11 | b11 ^ b12) &"
         "(a12 ^ a22 | b12 ^ b22) &"
         "(a12 ^ a21 | b12 ^ b21) &"
         "(a21 ^ a22 | b21 ^ b22)) &"

         "((a13 ^ a24 | b13 ^ b24) & "
         "(a13 ^ a14 | b13 ^ b14) &"
         "(a13 ^ a23 | b13 ^ b23) &"
         "(a14 ^ a24 | b14 ^ b24) &"
         "(a14 ^ a23 | b14 ^ b23) &"
         "(a23 ^ a24 | b23 ^ b24)) &"

         "((a31 ^ a32 | b31 ^ b32) & "
         "(a31 ^ a41 | b31 ^ b41) &"
         "(a31 ^ a42 | b31 ^ b42) &"
         "(a32 ^ a41 | b32 ^ b41) &"
         "(a32 ^ a42 | b32 ^ b42) &"
         "(a41 ^ a42 | b41 ^ b42)) &"

         "((a33 ^ a34 | b33 ^ b34) & "
         "(a33 ^ a43 | b33 ^ b43) &"
         "(a33 ^ a44 | b33 ^ b44) &"
         "(a34 ^ a43 | b34 ^ b43) &"
         "(a34 ^ a44 | b34 ^ b44) &"
         "(a43 ^ a44 | b43 ^ b44)) &"


         "((a11 ^ a22 | b11 ^ b22) & "
         "(a11 ^ a33 | b11 ^ b33) &"
         "(a11 ^ a44 | b11 ^ b44) &"
         "(a22 ^ a33 | b22 ^ b33) &"
         "(a22 ^ a44 | b22 ^ b44) &"
         "(a33 ^ a44 | b33 ^ b44)) &"

         "((a14 ^ a23 | b14 ^ b23) & "
         "(a14 ^ a32 | b14 ^ b32) &"
         "(a14 ^ a41 | b14 ^ b41) &"
         "(a23 ^ a32 | b23 ^ b32) &"
         "(a23 ^ a41 | b23 ^ b41) &"
         "(a32 ^ a41 | b32 ^ b41))"
         )

print(f.satisfy_one())
print(list(f.satisfy_all()))
print(len(list(f.satisfy_all())))
