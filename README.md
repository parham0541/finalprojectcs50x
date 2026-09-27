# 👼 Harvard Angels

<div align="center">

<img src="assets/img/message.png" alt="Harvard Angels" width="180">

### 🎮 A 2D Side-Scrolling Game Built with Python & Pygame

Inspired by **Flappy Bird** and developed as my final project for
**Harvard University's CS50x — Introduction to Computer Science**

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-00A86B?style=for-the-badge)](https://www.pygame.org/)
[![CS50x](https://img.shields.io/badge/Harvard-CS50x-A51C30?style=for-the-badge\&logo=harvard\&logoColor=white)](https://cs50.harvard.edu/x/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)

<br>

### 🎬 Video Demo

<a href="https://youtu.be/JpfO9euS6OM?si=KZiYgod9IEvc-HDL">
  <img src="https://img.youtube.com/vi/JpfO9euS6OM/maxresdefault.jpg" alt="Harvard Angels Video Demo" width="750">
</a>

<br><br>

**▶️ Click the image to watch the gameplay demo**

</div>

---

## 🪽 About the Game

**Harvard Angels** is a 2D side-scrolling arcade game developed in **Python using Pygame**.

The gameplay is inspired by the classic **Flappy Bird** formula, but the project was designed from scratch with its own visual assets, sounds, animations, scoring system, game states, and gameplay mechanics.

The main goal is simple:

> **Fly as far as possible, avoid the obstacles, and achieve the highest score.**

This project was created as the culmination of my learning journey through **CS50x**, applying programming concepts such as game loops, events, collision detection, timers, object movement, animation, sound management, and state handling.

---

# 🎮 Gameplay

The player controls an angel flying through a continuously scrolling environment.

Pressing **SPACE** applies upward thrust while gravity continuously pulls the character downward.

The challenge is to maintain the correct altitude while passing through randomly generated obstacles.

```text
             🪽 ANGEL
                ↑
                │ SPACE
                │
        ┌───────┴───────┐
        │               │
        │      🪽       │
        │               │
        │   ┌───────┐   │
        │   │       │   │
        │   │       │   │
        │   │       │   │
        │   └───────┘   │
        │               │
        └───────────────┘
                 →
              Movement
```

### 🎯 Objective

* Fly through the obstacles.
* Avoid collisions.
* Survive as long as possible.
* Increase your score.
* Beat your previous high score.

---

# ✨ Features

### 🪽 Player Physics

The angel uses simple gravity-based movement.

```text
SPACE
  ↓
Upward Thrust
  ↓
Vertical Velocity
  ↓
Gravity
  ↓
Continuous Falling
```

The player must repeatedly control the angel's vertical position to remain inside the safe areas between obstacles.

---

### 🚧 Random Obstacles

Obstacles are generated dynamically during gameplay.

Their positions are randomized to make every session slightly different.

```text
      ┌─────────────┐
      │             │
      │    PIPE     │
      │             │
      └─────────────┘

            GAP

      ┌─────────────┐
      │             │
      │    PIPE     │
      │             │
      └─────────────┘
```

---

### 🏆 Scoring System

The game keeps track of the player's score in real time.

A dedicated `can_score` flag prevents the same obstacle from being counted multiple times.

```text
Obstacle Passed
       ↓
 can_score?
    ↙    ↘
  YES     NO
   ↓
Score +1
   ↓
Disable Scoring
```

---

### 🎞️ Wing Animation

The angel uses a **3-frame animation cycle** to simulate wing movement.

```text
Frame 1 → Frame 2 → Frame 3
   ↑                    ↓
   └────────────────────┘
```

This creates a simple but effective flying animation while keeping the game lightweight.

---

### 🔊 Sound & Music

The game includes:

* 🎵 Background music
* 🪽 Flying / movement effects
* 💥 Collision sounds
* 🎯 Gameplay sound effects

Audio is managed directly through Pygame.

---

### ⏸️ Pause System

Press:

```text
P
```

to pause or resume the game.

This allows the game loop to temporarily stop gameplay actions while keeping the application running.

---

### 🔄 Restart System

Press:

```text
R
```

to restart the game after a game-over state.

---

### 💥 Collision Detection

The project uses Pygame's rectangle collision system:

```python
colliderect()
```

This allows the game to detect collisions between:

* Player
* Obstacles
* Ground
* Ceiling

When a collision occurs, the game enters the **Game Over** state.

---

# 🧠 Game Architecture

The core gameplay follows a continuous game loop:

```text
┌──────────────────────┐
│      Start Game      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Handle Events      │
│  Keyboard / Events   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Update Physics     │
│ Gravity / Movement   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Generate Obstacles   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Collision Detection  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Update Score         │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Render Everything    │
└──────────┬───────────┘
           │
           └──────────→ Game Loop
```

---

# 🕹️ Controls

| Key     | Action                    |
| ------- | ------------------------- |
| `SPACE` | Fly / Apply upward thrust |
| `P`     | Pause / Resume            |
| `R`     | Restart                   |
| `ESC`   | Exit                      |

---

# 📊 Game States

The game is organized around different gameplay states.

```text
             ┌───────────┐
             │   START   │
             └─────┬─────┘
                   ↓
             ┌───────────┐
             │   PLAY    │
             └─────┬─────┘
                   │
          ┌────────┴────────┐
          ↓                 ↓
      PAUSED            COLLISION
          │                 │
          ↓                 ↓
       RESUME          GAME OVER
                            │
                            ↓
                         RESTART
                            │
                            └──→ PLAY
```

---

# 📁 Project Structure

```text
Harvard-Angels/
│
├── main.py
│
├── assets/
│   ├── img/
│   │   ├── ...
│   │
│   ├── sound/
│   │   ├── ...
│   │
│   └── font/
│       ├── ...
│
├── README.md
├── requirements.txt
│
└── LICENSE
```

---

# 🛠️ Technologies

| Technology      | Usage                          |
| --------------- | ------------------------------ |
| 🐍 Python       | Main programming language      |
| 🎮 Pygame       | Game engine / multimedia       |
| 🎨 Image Assets | Game graphics                  |
| 🔊 Audio Assets | Music & sound effects          |
| 🧠 Python Logic | Physics, scoring & game states |

---

# 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone <YOUR-REPOSITORY-URL>
cd Harvard-Angels
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start the game

```bash
python main.py
```

---

# 🎓 CS50x Certificate

<div align="center">

### Harvard University — CS50x

**Introduction to Computer Science**

<br>

<a href="https://certificates.cs50.io/85d77c33-8777-4d94-a5b3-dcbae08a3cdc.png?size=letter">

<img src="https://certificates.cs50.io/85d77c33-8777-4d94-a5b3-dcbae08a3cdc.png?size=letter" alt="CS50x Certificate" width="750">

</a>

<br><br>

🏆 **CS50x — Introduction to Computer Science**

<br>

<sub>Click the certificate to view the official certificate image.</sub>

</div>

---

# 🎬 Video Demo

<div align="center">

<a href="https://youtu.be/JpfO9euS6OM?si=KZiYgod9IEvc-HDL">

<img src="https://img.youtube.com/vi/JpfO9euS6OM/maxresdefault.jpg" alt="Harvard Angels Gameplay Demo" width="800">

</a>

<br>

### ▶️ Watch Harvard Angels in action

</div>

---

# 💡 What I Learned

Building this project helped me move from writing small Python programs to building a complete interactive application.

During development, I worked with:

* Game loops
* Event handling
* Object movement
* Gravity and basic physics
* Collision detection
* Randomized obstacle generation
* Animation
* Sound management
* Timers
* Score systems
* Game states
* Asset management
* Debugging
* Project organization

More importantly, I learned how different programming concepts can work together to create an actual playable application.

---

# 🔮 Future Improvements

Possible future versions could include:

* 🌎 Multiple environments
* 👼 Additional playable characters
* 🏆 Global leaderboard
* 💾 Persistent high scores
* 🎨 More animations
* 🌙 Different game themes
* 🎯 Difficulty progression
* 🪙 Collectible items
* ⚡ Power-ups
* 📱 Mobile version
* 🎮 Controller support

---

# 📜 CS50x

This project was developed as my **CS50x Final Project**, applying concepts learned throughout Harvard University's **Introduction to Computer Science** course.

CS50x provided the foundation for understanding:

```text
Programming
     ↓
Algorithms
     ↓
Data Structures
     ↓
Memory
     ↓
Software Engineering
     ↓
Problem Solving
     ↓
Real Project
```

---

# 👨‍💻 Developer

<div align="center">

### Parham Shyasi

**Computer Science Student • Developer • Linux & Cybersecurity Enthusiast**

<br>

> Built with Python, Pygame, curiosity, and a lot of debugging. 🐍❤️

</div>

---

# ⭐ Support

If you found this project interesting, consider giving the repository a ⭐

It helps support the project and encourages me to build more.

---

<div align="center">

### 👼 Harvard Angels

**Fly. Dodge. Score. Repeat.**

<br>

`Python` • `Pygame` • `CS50x`

</div>
