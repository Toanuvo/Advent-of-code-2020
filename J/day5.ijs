i =: e.&'BR'  ;._2 getin 20 5
p =: [ { ([/.~ ] >: ] {~ <.@-:@#)@:]
r =: , (i. 128) [F..p"_ 1 ] 7 {."1 i
c =: , (i. 8) [F..p"_ 1 ] _3 {."1 i
p1 =:  >./ c + r*8
mr =: {. (~. #~  8 > #/.~) r
mc =: (i. 8) -. c #~ mr = r
p2 =: mc + 8 * mr
p1;p2