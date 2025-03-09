Ping Pong Game with AI Opponent
--------------------------------
Description:
This is a fully functional Ping Pong game built in Python using the `turtle` graphics module for visuals,
`pygame` for background music, and `winsound` for sound effects. The game is a classic two-player match
with one paddle controlled by the player and the other by an AI opponent. The goal is to score points
by getting the ball past your opponent's paddle.

Features:
1. Dynamic Gameplay:
   - The ball moves and bounces off walls and paddles.
   - Speed increases upon paddle collisions, adding difficulty over time.

2. Player vs AI Opponent:
   - Player controls the left paddle (`madrab1`) using the "Up" and "Down" keys.
   - The AI opponent controls the right paddle (`madrab2`), dynamically tracking the ball's position.

3. Scorekeeping:
   - A scoreboard displays real-time updates for both players.
   - The game ends when either player reaches the predefined winning score.

4. Sound Effects:
   - Background music plays continuously during the game.
   - Unique sound effects play for paddle collisions and scoring events.

Customization Options:
- Sounds: Replace background music or sound effects by updating the file paths.
- Winning Score: Adjust the `winning_score` variable to change the number of points required to win.
- Difficulty: Modify the AI's responsiveness and speed in the AI logic section.
