# My arcade plan (example)

This is what a filled-in arcade plan looks like. It uses the supplied example
game so you can see the level of detail that works. Your plan covers your two
chosen games from the list instead, one section each, plus any bonus game. The
example game does not count toward the two, and a hand-drawn plan, scanned or
photographed, is just as good as this one. If you pitch a game of your own
design, use the pitch section as well.

## Guess the number (the example game)

**Difficulty.** Easy (the example game, which does not count toward the two).

**Rules, in a few sentences.** The program picks a secret number between 1 and
20, and the player has five guesses to find it. After each guess the program
answers too low, too high, or you got it. The session ends when the secret is
found or the guesses run out.

**What one turn looks like.** One turn is one guess. The player types a whole
number, and the program prints one answer line: too low, too high, or you got
it.

**How it ends.** The session ends two ways: the player guesses the secret, or
five guesses are spent. Either way the game prints the outcome and the score,
and returns one score to the menu.

**How a score is earned.** A correct guess on attempt one earns 50. Every extra
guess costs 10 points, so a win on guess five earns 10, and running out of
guesses earns 0. Fewer guesses always means more points, so higher is better.

**Game settings.** Secret number between 1 and 20, with five guesses.

## Scoreboard fields

Every finished game records the player's name and the score. This plan keeps
the default layout, with the game's module name as the key, so each game's
records sit under its own name and the scoreboard screen shows each game's best
score and who set it:

```json
{
  "example_game": [
    {"player": "Sam", "score": 40},
    {"player": "Ada", "score": 30}
  ]
}
```
