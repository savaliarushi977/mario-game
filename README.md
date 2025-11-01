# 🎮 Super Mario 2D Platformer Game

A classic 2D side-scrolling platformer game inspired by the legendary Super Mario, built from scratch using Python and Pygame. Navigate through challenging levels, avoid obstacles, reach checkpoints, and prove your skills!

## 🌟 Features

### Core Gameplay
- **Classic Mario Character**: Pixel-art styled Mario with authentic red hat, blue overalls, and nostalgic appearance
- **Smooth 2D Movement**: Responsive left/right movement with arrow keys
- **Jump Mechanics**: Space bar jumping with realistic gravity physics
- **Side-Scrolling Camera**: Smooth camera tracking that follows Mario through the level

### Game Mechanics
- **4 Checkpoint System**: Progress through 4 strategically placed checkpoints
- **Respawn System**: Die and respawn at your last checkpoint reached
- **Lives System**: Start with 3 lives - lose them all and it's game over
- **Obstacle Challenges**: 
  - **Pits**: Deadly gaps that cause instant death if you fall
  - **Enemies**: Orange enemies patrolling platforms
  - **Platforming**: Precise jumps required between platforms

### Level Design
- **Extended Level**: 4000 pixels of side-scrolling adventure
- **Multiple Platforms**: 20+ platforms with varying heights and gaps
- **Strategic Checkpoints**: 4 checkpoints marking major progress points
- **6 Enemies**: Placed at challenging locations
- **4 Pit Obstacles**: Test your jumping skills

### UI & Polish
- **Score System**: Earn 100 points for each checkpoint reached
- **Lives Display**: Always know how many chances you have left
- **Checkpoint Counter**: Track your progress (0/4 to 4/4)
- **Winner Screen**: Celebratory screen when you complete all checkpoints
- **Restart Option**: Play again after winning or press ESC to quit
- **Clean Retro Aesthetic**: Sky blue background, brick-textured platforms

## 🎯 Objective

Your mission is to guide Mario through the entire level and reach all 4 checkpoints without losing all your lives. Each checkpoint you reach becomes your new respawn point if you die, but lose all 3 lives and it's game over!

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Clone or download this repository**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

Alternatively, install Pygame directly:
```bash
pip install pygame
```

## 🎮 How to Play

### Starting the Game

**Easy Way (Recommended):**

Mac/Linux:
```bash
./run.sh
```

Windows:
```bash
run.bat
```

**Manual Way:**
```bash
python3 mario_game.py
```

### Controls
| Key | Action |
|-----|--------|
| **Left Arrow** | Move Mario left |
| **Right Arrow** | Move Mario right |
| **Space Bar** | Jump |

### Gameplay Tips
1. **Reach Checkpoints**: Yellow flags turn green when activated - these are your respawn points
2. **Avoid Enemies**: Orange creatures will kill you on contact
3. **Mind the Gaps**: Black pits mean instant death
4. **Time Your Jumps**: Some platforms require precise jumping
5. **Watch Your Lives**: You have 3 chances - use them wisely

### Winning the Game
- Clear all 4 checkpoints to see the **WINNER!** screen
- Press **ENTER** to play again or **ESC** to quit

## 🛠️ Technical Details

### Built With
- **Python 3**: Core programming language
- **Pygame**: Game development framework for graphics, input, and physics

### Game Architecture
- **Object-Oriented Design**: Separate classes for Mario, Platforms, Enemies, Pits, and Checkpoints
- **Sprite-Based Rendering**: All game objects use Pygame sprite system
- **Collision Detection**: Pixel-perfect collision for platforms and obstacles
- **Camera System**: Smooth scrolling camera follows player position
- **State Management**: Game states for playing, death, and victory

### Key Components
- **Mario Class**: Player character with movement, jumping, gravity, collision detection
- **Platform Class**: Brick-textured ground and platforms
- **Enemy Class**: Orange hostile characters
- **Pit Class**: Deadly gap obstacles
- **Checkpoint Class**: Flag system that changes color when activated
- **Level Creation**: Function that builds the entire game world
- **Winner Screen**: Victory display with restart functionality

## 🎨 Visual Design

The game features a retro pixel-art aesthetic inspired by classic NES-era Mario games:
- **Mario**: 32x48 pixels with red hat, skin-tone face, mustache, red shirt, and blue overalls
- **Platforms**: Brown brick-textured platforms with visible brick patterns
- **Enemies**: Orange 32x32 pixel creatures with simple face design
- **Checkpoints**: Yellow flags that turn green when activated
- **Background**: Classic sky blue (#5C94FC)

## 🎲 Game Flow

1. **Start**: Mario begins at position (100, 450) with 3 lives
2. **Navigate**: Use arrow keys and space to jump through the level
3. **Checkpoint 1** (at x=750): First safety point
4. **Checkpoint 2** (at x=1850): Quarter progress
5. **Checkpoint 3** (at x=2650): Halfway mark
6. **Checkpoint 4** (at x=3700): Final checkpoint = WINNER!
7. **Death**: Respawn at last checkpoint with -1 life
8. **Game Over**: All lives lost = restart from beginning
9. **Victory**: Complete all checkpoints to see winner screen

## 🏗️ Level Layout

The game features a carefully designed 4000-pixel level with:
- **6 ground segments** with strategic gaps (pits)
- **16 floating platforms** at various heights
- **4 deadly pits** requiring precision jumps
- **6 enemy placements** in challenging positions
- **4 checkpoint flags** marking progress milestones

## 🔧 Customization

Want to modify the game? Key variables to adjust:
- `LEVEL_WIDTH`: Extend or shorten the level (default: 4000)
- `lives`: Starting lives (default: 3)
- `mario.speed`: Movement speed (default: 5)
- `mario.jump_power`: Jump height (default: -15)
- `mario.gravity`: Fall speed (default: 0.8)

## 🐛 Troubleshooting

### Game won't start
- Ensure Pygame is installed: `pip install pygame`
- Verify Python 3.7+ is installed: `python3 --version`

### Controls not responsive
- Make sure the game window has focus (click on it)
- Check keyboard is properly connected

### Performance issues
- Close other applications to free up system resources
- Adjust `FPS` constant in code (default: 60)

## 📝 Future Enhancements

Potential features for future versions:
- Power-ups (mushrooms, stars)
- Coin collection system
- Moving enemies with AI
- Multiple levels
- Sound effects and background music
- High score leaderboard
- Different difficulty modes

## 👨‍💻 Development

Created as a learning project to demonstrate:
- Game loop implementation
- Sprite-based game development
- Physics simulation (gravity, jumping)
- Collision detection algorithms
- Camera scrolling systems
- State management in games
- User input handling
- UI rendering and game screens

## 📄 License

This project is created for educational purposes. Feel free to use, modify, and learn from the code!

## 🎉 Credits

Inspired by the legendary Super Mario Bros. by Nintendo. This is a fan project created for learning purposes.

---

**Enjoy the game and see if you can reach all 4 checkpoints! 🏁**
