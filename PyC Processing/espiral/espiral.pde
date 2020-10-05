void setup(){
  size(500,500);
}

void draw(){



String str = "              asdflkkjsahfdlkadshflkahdslkfasdfsdfsadfsdfasdfasdfsadfsadfsd,fbasdljfhasldjfhlsdkjfhlsdjfhlskadjfhldkasjfhlasjkdasjldhlaksjdfhjlaskdasldkajsdf";
float radius = 0;
//so we are rotating around the center, rather than (0,0):
translate(width/2, height/2); 
for (int i = 0; i < str.length(); i++) {
  radius += 1;
  // taken out because of non-constant spacing at large radius:
  //rotate(0.5);
  // this should give constant spacing, no matter the radius
  // change 10 to some other number for a different spacing. 
  rotate(12/radius);
  // drawing at (0,radius) because we're drawing onto a rotated canvas
  text(str.charAt(i), 0, radius);
}
}
