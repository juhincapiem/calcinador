Point(11)={0,0,0};
Point(12)={0.5,0,0};
Point(13)={1,0,0};
Point(14)={0,0.5,0};
Point(15)={0,1,0};
Point(16)={0.7071067812,0.7071067812,0};
Point(17)={0.5,0.5,0};

Point(21)={0,0,0.1};
Point(22)={0.5,0,0.1};
Point(23)={1,0,0.1};
Point(24)={0,0.5,0.1};
Point(25)={0,1,0.1};
Point(26)={0.7071067812,0.7071067812,0.1};
Point(27)={0.5,0.5,0.1};

Point(32)={-0.5,0,0};
Point(33)={-1,0,0};
Point(36)={-0.7071067812,0.7071067812,0};
Point(37)={-0.5,0.5,0};

Point(42)={-0.5,0,0.1};
Point(43)={-1,0,0.1};
Point(46)={-0.7071067812,0.7071067812,0.1};
Point(47)={-0.5,0.5,0.1};
//===============================================
Line(11)={11,12};
Line(12)={12,13};
Line(13)={11,14};
Line(14)={14,15};
Line(15)={14,17};
Line(16)={12,17};
Circle(17)={13,11,16};
Circle(18)={15,11,16};
Line(19)={17,16};

Line(21)={21,22};
Line(22)={22,23};
Line(23)={21,24};
Line(24)={24,25};
Line(25)={24,27};
Line(26)={22,27};
Circle(27)={23,21,26};
Circle(28)={25,21,26};
Line(29)={27,26};

Line(31)={11,32};
Line(32)={32,33};
Line(35)={14,37};
Line(36)={32,37};
Circle(37)={33,11,36};
Circle(38)={15,11,36};
Line(39)={37,36};

Line(41)={21,42};
Line(42)={42,43};
Line(45)={24,47};
Line(46)={42,47};
Circle(47)={43,21,46};
Circle(48)={25,21,46};
Line(49)={47,46};

Line(1)={11,21};
Line(2)={12,22};
Line(3)={13,23};
Line(4)={14,24};
Line(5)={15,25};
Line(6)={16,26};
Line(7)={17,27};

Line(20)={32,42};
Line(30)={33,43};
Line(60)={36,46};
Line(70)={37,47};
//===============================================
Curve Loop(1)={11,2,-21,-1};
Surface(1)={1};
Curve Loop(2)={12,3,-22,-2};
Surface(2)={2};
Curve Loop(3)={13,4,-23,-1};
Surface(3)={3};
Curve Loop(4)={14,5,-24,-4};
Surface(4)={4};
Curve Loop(5)={15,7,-25,-4};
Surface(5)={5};
Curve Loop(6)={16,7,-26,-2};
Surface(6)={6};
Curve Loop(7)={17,6,-27,-3};
Surface(7)={7};
Curve Loop(8)={18,6,-28,-5};
Surface(8)={8};
Curve Loop(9)={19,6,-29,-7};
Surface(9)={9};
Curve Loop(10)={11,16,-15,-13};
Surface(10)={10};
Curve Loop(11)={21,26,-25,-23};
Surface(11)={11};
Curve Loop(12)={12,17,-19,-16};
Surface(12)={12};
Curve Loop(13)={22,27,-29,-26};
Surface(13)={13};
Curve Loop(14)={15,19,-18,-14};
Surface(14)={14};
Curve Loop(15)={25,29,-28,-24};
Surface(15)={15};

Curve Loop(101)={31,20,-41,-1};
Surface(101)={101};
Curve Loop(102)={32,30,-42,-20};
Surface(102)={102};
Curve Loop(105)={35,70,-45,-4};
Surface(105)={105};
Curve Loop(106)={36,70,-46,-20};
Surface(106)={106};
Curve Loop(107)={37,60,-47,-30};
Surface(107)={107};
Curve Loop(108)={38,60,-48,-5};
Surface(108)={108};
Curve Loop(109)={39,60,-49,-70};
Surface(109)={109};
Curve Loop(16)={31,36,-35,-13};
Surface(16)={16};
Curve Loop(17)={41,46,-45,-23};
Surface(17)={17};
Curve Loop(18)={32,37,-39,-36};
Surface(18)={18};
Curve Loop(19)={42,47,-49,-46};
Surface(19)={19};
Curve Loop(20)={35,39,-38,-14};
Surface(20)={20};
Curve Loop(21)={45,49,-48,-24};
Surface(21)={21};
//===============================================
Transfinite Line{11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29}=50;
Transfinite Line{31,41,32,42,35,45,36,46,37,47,38,48,39,49}=50;
Transfinite Line{1,2,3,4,5,6,7,20,30,70,60}=2;

Transfinite Surface{1,5,3,6,10,11};
Surface Loop(1)={1,5,3,6,10,11};
Recombine Surface{1,5,3,6,10,11};
Volume(1)={1};

Transfinite Surface{2,9,6,7,12,13};
Surface Loop(2)={2,9,6,7,12,13};
Recombine Surface{2,9,6,7,12,13};
Volume(2)={2};

Transfinite Surface{5,8,4,9,14,15};
Surface Loop(3)={5,8,4,9,14,15};
Recombine Surface{5,8,4,9,14,15};
Volume(3)={3};

Transfinite Surface{16,17,105,101,3,106};
Surface Loop(4)={16,17,105,101,3,106};
Recombine Surface{16,17,105,101,3,106};
Volume(4)={4};

Transfinite Surface{18,19,106,107,102,109};
Surface Loop(5)={18,19,106,107,102,109};
Recombine Surface{18,19,106,107,102,109};
Volume(5)={5};

Transfinite Surface{20,21,4,109,108,105};
Surface Loop(6)={20,21,4,109,108,105};
Recombine Surface{20,21,4,109,108,105};
Volume(6)={6};

Transfinite Volume {1,2,3,4,5,6};
Coherence;

Physical Surface("curve") = {7,8,107,108};
Physical Surface("hor") = {1,2,101,102};
Physical Surface("frontAndBack") = {10,11,12,13,14,15,16,17,18,19,20,21};
Physical Volume("volume")={1,2,3,4,5,6};

