let canvas = document.querySelector("canvas");


canvas.width = innerWidth;
canvas.height = innerHeight;
const c = canvas.getContext('2d');

class Player {
    constructor(x, y, color)
    {
        this.x = x 
        this.y = y
        this.color = color
    }
    draw()
    {
    
        
    }
}

const x = canvas.width / 2;
const y = canvas.height / 2;

const player = new Player(x,y, 'black');
player.draw()
console.log(player);

