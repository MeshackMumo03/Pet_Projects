

let bob;
let anchor;
let spring;

let gravity;

function setup() {
  createCanvas(900, 700);
  bob = new Particle(400, 190);
  anchor = new Particle(200, 210);
  spring = new Spring(0.01, 200, bob, anchor);
  gravity = createVector(0, 0.1);
}

function draw() {
  background(112, 50, 126);
  spring.show();
  spring.update();

  bob.show();
  bob.update();
  anchor.show();
  anchor.update();

  if (mouseIsPressed) {
    bob.position.set(mouseX, mouseY);
    bob.velocity.set(0, 0);
  }
}
