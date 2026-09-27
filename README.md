### Harvard Angels game

### Video Demo: <https://youtu.be/JpfO9euS6OM?si=KZiYgod9IEvc-HDL>

---

##  Description
**Harvard Angels** is a modern **2D side-scrolling game** developed in **Python** using the **Pygame** library, directly inspired by the timeless mobile phenomenon **Flappy Bird**.

This project is the culmination of my journey through the **CS50x course**, serving as a comprehensive demonstration of my programming skills.

The objective is to guide a small angel through randomly generated pipe obstacles and achieve the highest score possible. Along the way, the game demonstrates:
- Efficient game loop management
- Responsive event handling
- Smooth animations
- Precise collision detection
- Seamless sound and music integration

---

## Gameplay
- Press **SPACE** to start the game from the welcome screen.
- **SPACE** controls the angel’s upward thrust.
- Gravity pulls the angel downward, requiring balance between ascent and descent.
- The angel’s movement is animated with a **3-frame wing cycle** for realism.
- **Randomly generated obstacles** ensure no two playthroughs are the same.
- Scores update in real time, and the **high score** is saved during the session.
- Collisions with pipes, the ground, or the ceiling end the game with a distinct sound effect.

---

##  Features
- **Accurate Scoring:** Points awarded once per obstacle using a `can_score` flag.
- **Immersive Audio:** Background music plus unique sound effects for scoring and collisions.
- **Pause Functionality:** Press **P** to pause/resume at any time.
- **Quick Restart:** Press **R** after game-over to restart instantly.
- **Custom Event Timers:** Smooth obstacle generation and animation, independent of frame rate.
- **Efficient Collision Detection:** Implemented with Pygame’s `colliderect` method.

---

##  Project Structure
```
project/
│
├── main.py # Core game logic
│
├── assets/
│   ├── img/ # Visual assets
│   ├── sound/ # Audio
│   └── font/ # Custom font
│
├── README.md
└── requirements.txt # Python dependencies
```

---

##  How to Run

1. Ensure **Python 3** is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the game:
   ```bash
   python main.py
   ```

---

##  Final Notes
This project goes **beyond a simple clone** by integrating polished animations, robust collision handling, background music, and extra features like pause/resume and quick restart.

It represents a cohesive and enjoyable **Python + Pygame** game, proudly presented as my **CS50x final project**.
