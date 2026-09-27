<div align="center">

# 👼 Harvard Angels

### A Python + Pygame 2D Arcade Game

**Fly. Dodge. Survive. Beat your High Score.**

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2D_Game_Engine-00A86B?style=for-the-badge)](https://www.pygame.org/)
[![CS50x](https://img.shields.io/badge/Harvard-CS50x-A51C30?style=for-the-badge\&logo=harvard\&logoColor=white)](https://cs50.harvard.edu/x/)
[![Status](https://img.shields.io/badge/Status-Completed-2ea44f?style=for-the-badge)]()

<br>

### 🎮 Play the Demo

[![Watch the Demo](https://img.shields.io/badge/▶_WATCH_GAMEPLAY-FF0000?style=for-the-badge\&logo=youtube\&logoColor=white)](https://youtu.be/JpfO9euS6OM?si=KZiYgod9IEvc-HDL)

  

### 🎓 CS50x Certificate

[![View Certificate](https://img.shields.io/badge/🎓_VIEW_CS50x_CERTIFICATE-8B0000?style=for-the-badge)](https://certificates.cs50.io/b8e2ba21-12c3-4e9f-8e3b-69f7060eb213.pdf?size=letter)

</div>

---

# 👼 About The Game

**Harvard Angels** is a 2D side-scrolling arcade game built from scratch with **Python** and **Pygame** as my **CS50x Final Project**.

Inspired by the gameplay concept of *Flappy Bird*, the game puts you in control of a small flying angel. Your goal is simple:

> **Fly through the obstacles, survive as long as possible, and beat your high score.**

But behind the simple gameplay is a complete game loop containing physics, gravity, collision detection, animation, procedural obstacle generation, scoring, audio, game states, pause functionality and restart mechanics.

<br>

<div align="center">

### ☁️ FLAP

⬇️

### 🏛️ DODGE

⬇️

### 👼 SURVIVE

⬇️

### 🏆 BEAT YOUR SCORE

</div>

---

# 🎮 Gameplay

The game begins with a welcome screen.

Press **SPACE** and the angel takes flight.

Gravity continuously pulls the player downward while each press of **SPACE** provides upward thrust.

The obstacles are generated dynamically, meaning every run can create a different challenge.

### Your mission:

* 👼 Control the flying angel
* 🪽 Keep the angel in the air
* 🏛️ Navigate through randomly generated pipes
* 💥 Avoid collisions
* 🏆 Increase your score
* 🔥 Beat your previous high score
* 🎵 Experience sound effects and background music
* ⏸️ Pause the game whenever necessary
* 🔄 Restart instantly after Game Over

---

# ✨ Features

| Feature                    | Description                                                                  |
| -------------------------- | ---------------------------------------------------------------------------- |
| 👼 **Animated Player**     | 3-frame wing animation creates a smoother flying effect                      |
| 🏛️ **Random Obstacles**   | Pipes are generated dynamically for different gameplay every run             |
| 🎯 **Collision Detection** | Uses Pygame's `colliderect()` for reliable collision handling                |
| 🏆 **Scoring System**      | Points are awarded once for every successfully passed obstacle               |
| 🔊 **Sound System**        | Background music and gameplay sound effects                                  |
| ⏸️ **Pause System**        | Press `P` to pause or resume the game                                        |
| 🔄 **Quick Restart**       | Press `R` after Game Over to restart                                         |
| ⏱️ **Custom Timers**       | Obstacle generation and animation are controlled independently of frame rate |
| 🌍 **Game States**         | Welcome, gameplay, pause and Game Over states                                |
| 💾 **High Score**          | Highest score is maintained throughout the game session                      |

---

# 🕹️ Controls

|   Key   | Action                  |
| :-----: | ----------------------- |
| `SPACE` | Start / Fly upward      |
|   `P`   | Pause / Resume          |
|   `R`   | Restart after Game Over |

---

# 🧠 How It Works

At the heart of Harvard Angels is a continuously running **game loop**.

```text
                 ┌─────────────────┐
                 │   Start Game    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Handle Events   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Update Physics  │
                 │ Gravity + Flap  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Move Obstacles  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Check Collision │
                 └────────┬────────┘
                          │
                  ┌───────┴───────┐
                  │               │
                HIT             SAFE
                  │               │
                  ▼               ▼
          ┌─────────────┐   ┌─────────────┐
          │  Game Over  │   │ Update Score│
          └─────────────┘   └──────┬──────┘
                                   │
                                   ▼
                            ┌─────────────┐
                            │ Draw Frame  │
                            └──────┬──────┘
                                   │
                                   └──────► LOOP
```

This structure allows the game to continuously process:

**Input → Physics → Obstacles → Collision → Score → Rendering**

---

# 🪽 Player Physics

The angel is affected by gravity every frame.

When the player presses `SPACE`, an upward velocity is applied.

Conceptually:

```text
SPACE
  │
  ▼
Upward Velocity
  │
  ▼
     👼
      \
       \
        ↓
      Gravity
        ↓
     Collision
```

This creates the familiar **rise-and-fall** gameplay mechanic while allowing the player to control the angel's vertical position.

---

# 🏛️ Procedural Obstacles

The pipe obstacles aren't simply placed in one fixed position.

Their positions are generated dynamically, creating different obstacle layouts during gameplay.

```text
       █████
       █████
       █████
       
          👼
          
       █████
       █████
       █████
```

The player must continuously adjust their movement to pass through the gap.

This makes every run slightly different and prevents the game from becoming a completely predictable sequence.

---

# 🎯 Scoring System

The scoring system uses a `can_score` flag to ensure that the player receives points **only once per obstacle**.

Conceptually:

```text
Obstacle approaching
        │
        ▼
   Player passes it
        │
        ▼
 can_score == True ?
       / \
     YES  NO
      │    │
      ▼    ▼
   +1 Point
      │
      ▼
can_score = False
```

This prevents the score from increasing multiple times while the player remains near the same obstacle.

---

# 🪽 Animation System

The angel uses a **3-frame wing animation**.

```text
Frame 1        Frame 2        Frame 3

   👼             👼             👼
  /│\            /│\            /│\
   │              │              │
  / \            / \            / \
```

The animation is controlled using timed events rather than depending directly on how fast the computer renders frames.

This keeps the animation consistent across different frame rates.

---

# 🔊 Audio

Harvard Angels includes multiple layers of audio:

* 🎵 Background music
* 🏆 Score sound
* 💥 Collision sound
* 🎮 Gameplay feedback

Audio is integrated directly into the gameplay loop to provide feedback when important events occur.

---

# ⏸️ Game States

The game isn't just a single screen.

It contains several gameplay states:

```text
┌──────────────┐
│ Welcome      │
└──────┬───────┘
       │ SPACE
       ▼
┌──────────────┐
│ Playing      │◄─────────┐
└──────┬───────┘          │
       │                   │
       │ P                │ Resume
       ▼                   │
┌──────────────┐           │
│ Paused       │───────────┘
└──────────────┘

       │
       │ Collision
       ▼

┌──────────────┐
│ Game Over    │
└──────┬───────┘
       │ R
       ▼
┌──────────────┐
│ Restart      │
└──────────────┘
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
│   │   └── ...
│   │
│   ├── sound/
│   │   ├── ...
│   │   └── ...
│   │
│   └── font/
│       └── ...
│
├── README.md
│
└── requirements.txt
```

### `main.py`

The main application containing:

* Game initialization
* Game loop
* Player movement
* Physics
* Animation
* Collision detection
* Obstacle generation
* Score management
* Audio
* Game states
* Rendering

### `assets/`

Contains the visual, audio and font resources used by the game.

### `requirements.txt`

Contains the Python dependencies required to run the project.

---

# ⚙️ Built With

<div align="center">

| Technology                    | Purpose                            |
| ----------------------------- | ---------------------------------- |
| 🐍 **Python**                 | Core programming language          |
| 🎮 **Pygame**                 | Game engine / multimedia framework |
| 🖼️ **Pygame Surface & Rect** | Rendering and collision handling   |
| 🔊 **Pygame Mixer**           | Music and sound effects            |
| ⏱️ **Pygame Events & Timers** | Animation and obstacle timing      |

</div>

---

# 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Harvard-Angels.git
cd Harvard-Angels
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the game

```bash
python main.py
```

---

# 🎓 CS50x Final Project

Harvard Angels was created as my **Final Project for Harvard University's CS50x — Introduction to Computer Science**.

The project represents the practical application of concepts learned throughout the course, including:

* Programming fundamentals
* Algorithms
* Data structures
* Problem solving
* Python
* Debugging
* Software design
* Event-driven programming

### 🎓 Certificate

**CS50x Certificate of Completion**

[**View my official CS50 certificate →**](https://certificates.cs50.io/b8e2ba21-12c3-4e9f-8e3b-69f7060eb213.pdf?size=letter)

---

# 🎬 Video Demo

<div align="center">

## 👼 Harvard Angels — Gameplay Demo

[![Watch the Gameplay Demo](https://img.youtube.com/vi/JpfO9euS6OM/maxresdefault.jpg)](https://youtu.be/JpfO9euS6OM?si=KZiYgod9IEvc-HDL)

### ▶️ [Watch the full gameplay on YouTube](https://youtu.be/JpfO9euS6OM?si=KZiYgod9IEvc-HDL)

</div>

---

# 💡 What I Learned

Building Harvard Angels was more than simply creating a Flappy Bird-style game.

It taught me how individual programming concepts come together to create an actual interactive application.

I learned how to structure a real-time game loop, manage user input, work with coordinates and physics, detect collisions, create animations, manage audio, generate obstacles dynamically and organize multiple gameplay states.

Most importantly, the project gave me experience turning an idea into a complete working application instead of writing isolated pieces of code.

---

# 🔮 Possible Future Improvements

The current version is complete, but the project could be expanded with:

* 🌎 Multiple environments
* 👼 Multiple playable characters
* 🏆 Persistent leaderboard
* 💾 Save system
* ❤️ Lives / health system
* ⚡ Difficulty progression
* 🏛️ More Harvard-themed environments
* 🎨 Additional animations
* 🌐 Online leaderboard
* 🏅 Achievement system
* 🎮 Controller support

---

# ❤️ Credits

Inspired by the gameplay concept of **Flappy Bird**.

Developed from scratch as my **CS50x Final Project** using **Python + Pygame**.

---

<div align="center">

# 👼 Harvard Angels

### Built with Python. Powered by Pygame. Created for CS50x.

**Fly higher. Dodge smarter. Beat your score.**

<br>

[🎬 Demo](https://youtu.be/JpfO9euS6OM?si=KZiYgod9IEvc-HDL)
  •  
[🎓 Certificate](https://certificates.cs50.io/b8e2ba21-12c3-4e9f-8e3b-69f7060eb213.pdf?size=letter)

<br><br>

⭐ **If you found the project interesting, consider starring the repository!**

</div>
