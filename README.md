# Airplane Game

Airplane Game is a shooting operation game developed by Tencent's WeChat team. It is equipped on the WeChat platform, which is easy to operate and has many players. The overall environment of the game is mainly around space. What the player has to do in the game is to drive the latest fighter to the enemy's headquarters.

# How To Get Started
After the game is loaded, click the Start icon to start the game.

# How To Operate
Use the keyboard direction keys ↑↓←→ keys to control the movement of the aircraft. The space bar is the launching bullet. 

# Game Rules
When hitting the middle enemey aircraft, it increases by 20 points;
When hitting the large enemy aircraft, it increases by 50 points.
When you are hit by one of the enemy aircrafts, the game ends.

# Game Goal
Eliminate more enemy planes and win higher scores to compare with other players.

# V0.1
1. Encapsulates the base class of the aircraft and our aircraft class
2. Game framework structure
3. Game start interface
4. Our plane can fly, can be controlled by keyboard, can fire bullets
5. Bullet packaging

# V0.2
1. Encapsulated enemy small aircraft
2. Package reset() so that instances of the aircraft can be reused
3. Encapsulate update() to enable the aircraft to be in a random position and arrive at the battlefield at random times.

# V0.3
1. Realize the random effect of enemy small aircraft
2. Rewrite main.py with object-oriented ideas, abstracting to war.py

# V0.4
1. Collision detection of bullets
2. Aircraft collision crash
3. Game status judgment

# V0.5
1. Package classification
2. Add statistics after hitting the enemy plane
3. Display game scores after the game is over

# V0.6
1. Record the historical results of the game
2. Show historical results
3. Optimization of game keyboard events

# V1.0 (Coming Up...)
1. Add middle and large enemy aircrafts.
2. Optimized UI
