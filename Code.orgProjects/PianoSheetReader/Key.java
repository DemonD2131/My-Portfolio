import org.code.theater.*;
import org.code.media.*;

public class Key{

  int x = 10;
  int y = 150;
  int KEYWIDTH = 17;
  int KEYHEIGHT = 50;
  Scene scene;
  public Key(Scene scene){
    this.scene = scene;

  }
  public void createBackground(){
    this.createKey(48, false);
    this.createKey(49, false);
    this.createKey(50, false);
    this.createKey(51, false);
    this.createKey(52, false);
    this.createKey(53, false);
    this.createKey(54, false);
    this.createKey(55, false);
    this.createKey(56, false);
    this.createKey(57, false);
    this.createKey(58, false);
    this.createKey(59, false);
    this.createKey(60, false);
    this.createKey(61, false);
    this.createKey(62, false);
    this.createKey(63, false);
    this.createKey(64, false);
    this.createKey(65, false);
    this.createKey(66, false);
    this.createKey(67, false);
    this.createKey(68, false);
    this.createKey(69, false);
    this.createKey(70, false);
    this.createKey(71, false);
    this.createKey(72, false);
    this.createKey(73, false);
    this.createKey(74, false);
    this.createKey(75, false);
    this.createKey(76, false);
    this.createKey(77, false);
    this.createKey(78, false);
    this.createKey(79, false);
    this.createKey(80, false);
    this.createKey(81, false);
    this.createKey(82, false);
    this.createKey(83, false);
    this.createKey(84, false);
  }
  public void createKey(int index, boolean color){
    x = 10;
    if(color){
      scene.setFillColor("red");
    }
    if(!color){
      scene.setFillColor("black");
    }

if(index==48){
int[] points={x,y,x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}
else if(index==49){
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};
if(color){
scene.setFillColor("blue");
}

scene.drawShape(points,true);
}else if(index==50){
int[] points={x+KEYWIDTH+(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y};
if(color){

scene.drawShape(points,true);

}else{
scene.drawShape(points,false);
}
}else if(index==51){
x+=KEYWIDTH;
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}

scene.drawShape(points,true);
}else if(index==52){
x+=KEYWIDTH*2;
int[] points={x+(KEYWIDTH/5),y,x+KEYWIDTH,y,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y+KEYHEIGHT/2,x+(KEYWIDTH/5),y+KEYHEIGHT/2,x+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==53){
x+=KEYWIDTH*3;
int[] points={x,y,x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==54){
x+=KEYWIDTH*3;
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}
scene.drawShape(points,true);
}else if(index==55){
x+=KEYWIDTH*3;
int[] points={x+KEYWIDTH+(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==56){
x+=KEYWIDTH*4;
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}
scene.drawShape(points,true);
}else if(index==57){
x+=KEYWIDTH*4;
int[] points={x+KEYWIDTH+(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==58){
x+=KEYWIDTH*5;
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}
scene.drawShape(points,true);
}else if(index==59){
x+=KEYWIDTH*6;
int[] points={x+(KEYWIDTH/5),y,x+KEYWIDTH,y,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y+KEYHEIGHT/2,x+(KEYWIDTH/5),y+KEYHEIGHT/2,x+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==60){
x+=KEYWIDTH*7;
int[] points={x,y,x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}
else if(index==61){
x+=KEYWIDTH*7;
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};
if(color){
scene.setFillColor("blue");
}

scene.drawShape(points,true);
}else if(index==62){
x+=KEYWIDTH*7;
int[] points={x+KEYWIDTH+(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==63){
x+=KEYWIDTH*8;
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}

scene.drawShape(points,true);
}else if(index==64){
x+=KEYWIDTH*9;
int[] points={x+(KEYWIDTH/5),y,x+KEYWIDTH,y,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y+KEYHEIGHT/2,x+(KEYWIDTH/5),y+KEYHEIGHT/2,x+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==65){
x+=KEYWIDTH*10;
int[] points={x,y,x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==66){
x+=KEYWIDTH*10;
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}
scene.drawShape(points,true);
}else if(index==67){
x+=KEYWIDTH*10;
int[] points={x+KEYWIDTH+(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==68){
x+=KEYWIDTH*11;
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}
scene.drawShape(points,true);
}else if(index==69){
x+=KEYWIDTH*11;
int[] points={x+KEYWIDTH+(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==70){
x+=KEYWIDTH*12;
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}
scene.drawShape(points,true);
}else if(index==71){
x+=KEYWIDTH*13;
int[] points={x+(KEYWIDTH/5),y,x+KEYWIDTH,y,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y+KEYHEIGHT/2,x+(KEYWIDTH/5),y+KEYHEIGHT/2,x+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==72){
x+=KEYWIDTH*(7+7);
int[] points={x,y,x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}
else if(index==73){
x+=KEYWIDTH*(7+7);
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};
if(color){
scene.setFillColor("blue");
}

scene.drawShape(points,true);
}else if(index==74){
x+=KEYWIDTH*(7+7);
int[] points={x+KEYWIDTH+(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==75){
x+=KEYWIDTH*(8+7);
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}

scene.drawShape(points,true);
}else if(index==76){
x+=KEYWIDTH*(9+7);
int[] points={x+(KEYWIDTH/5),y,x+KEYWIDTH,y,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y+KEYHEIGHT/2,x+(KEYWIDTH/5),y+KEYHEIGHT/2,x+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==77){
x+=KEYWIDTH*(10+7);
int[] points={x,y,x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==78){
x+=KEYWIDTH*(10+7);
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}
scene.drawShape(points,true);
}else if(index==79){
x+=KEYWIDTH*(10+7);
int[] points={x+KEYWIDTH+(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==80){
x+=KEYWIDTH*(11+7);
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}
scene.drawShape(points,true);
}else if(index==81){
x+=KEYWIDTH*(11+7);
int[] points={x+KEYWIDTH+(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y,x+(2*KEYWIDTH)-(KEYWIDTH/5),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT/2,x+(2*KEYWIDTH),y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==82){
x+=KEYWIDTH*(12+7);
int[] points={x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH+(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y};;
if(color){
scene.setFillColor("blue");
}
scene.drawShape(points,true);
}else if(index==83){
x+=KEYWIDTH*(13+7);
int[] points={x+(KEYWIDTH/5),y,x+KEYWIDTH,y,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y+KEYHEIGHT/2,x+(KEYWIDTH/5),y+KEYHEIGHT/2,x+(KEYWIDTH/5),y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}else if(index==84){
x+=KEYWIDTH*21;
int[] points={x,y,x+KEYWIDTH-(KEYWIDTH/5),y,x+KEYWIDTH-(KEYWIDTH/5),y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT/2,x+KEYWIDTH,y+KEYHEIGHT,x,y+KEYHEIGHT,x,y};
if(color){
scene.drawShape(points,true);
}else{
scene.drawShape(points,false);
}
}
    
  }
}