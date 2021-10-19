#version 3.6;
global_settings {  assumed_gamma 1.0 }
//---------------------------------------
 //...
 // a basic background scene
 //...
//----------------------------------- end
#declare Nr = clock ;

cylinder{ <0,0.01,0>,<0,2.01*Nr,0>, 0.30
          texture {
             pigment { color rgb<1,1,1> }
             finish  { phong 0.5 reflection 0.00 }
                  } // end of texture
          translate<0.4,0,-0.3>
        } // end of cylinder ---------------------

