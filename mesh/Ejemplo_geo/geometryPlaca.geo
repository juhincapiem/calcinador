Point(0)={0,0,0};
Point(1)={1,0,0};
Point(2)={1,1,0};
Point(3)={0,1,0};
Point(4)={0,0,0.1};
Point(5)={1,0,0.1};
Point(6)={1,1,0.1};
Point(7)={0,1,0.1};
//===============================================
Line(1)={0,1};
Line(2)={1,2};
Line(3)={2,3};
Line(4)={3,0};
Line(5)={4,5};
Line(6)={5,6};
Line(7)={6,7};
Line(8)={7,4};
Line(9)={0,4};
Line(10)={1,5};
Line(11)={2,6};
Line(12)={3,7};
//===============================================
Curve Loop(1)={1,2,3,4};
Surface(1)={1};
Curve Loop(2)={5,6,7,8};
Surface(2)={2};
Curve Loop(3)={9,5,-10,-1};
Surface(3)={3};
Curve Loop(4)={10,6,-11,-2};
Surface(4)={4};
Curve Loop(5)={11,7,-12,-3};
Surface(5)={5};
Curve Loop(6)={12,8,-9,-4};
Surface(6)={6};

//===============================================
Transfinite Line{1,-3,5,-7}=100 Using Progression 0.98;
Transfinite Line{2,-4,6,-8}=100 Using Progression 0.98;
Transfinite Line{9,10,11,12}=2 Using Progression 1;

Transfinite Surface{1,2,3,4,5,6};
Surface Loop(1)={1,2,3,4,5,6};
Recombine Surface{1,2,3,4,5,6};
Volume(1)={1};

Transfinite Volume {1};
Coherence;
//
Physical Surface("arriba") = {5};
Physical Surface("abajo") = {3};
Physical Surface("derecha") = {4};
Physical Surface("izquierda") = {6};
Physical Surface("frontAndBack") = {1,2};
Physical Volume("volume")={1};

