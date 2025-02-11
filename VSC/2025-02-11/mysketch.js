function setup() {
    createCanvas(windowWidth, windowHeight);
    background(255,255,255);
    
    angle = 0;
    R = 130;
    r = 51;
    i = 0;

    xp = (R-r)*cos(angle) + r*cos((R-r)/r*angle) + windowWidth/2;
    yp = (R-r)*sin(angle) - r*sin((R-r)/r*angle) + windowHeight/2;
}

function draw() {
    i++;
    angle = i*3.141592/180;
    xn = (R-r)*cos(angle) + r*cos((R-r)/r*angle) + windowWidth/2;
    yn = (R-r)*sin(angle) - r*sin((R-r)/r*angle) + windowHeight/2;
    line(xp,yp,xn,yn);
    xp = xn;
    yp = yn;
}