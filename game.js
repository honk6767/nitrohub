console.log("🏎️ Game engine warming up...");
console.log("⛽ Fuel injected.");
console.log("😈 INSANE‑GEN MODE READY.");

let speed = 0;

function accelerate() {
    speed += 50;
    console.log("VROOOOM! Speed:", speed);
    if (speed > 9000) {
        console.log("🚓 Physics police are after you.");
    }
}

setInterval(accelerate, 1000);
