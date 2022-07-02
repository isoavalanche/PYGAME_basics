# PYTHON GAMES: I made this with Pygame module

1. References
    1. Pygame Page: http://pygame.org
    2. documentation: http://pygame.org/docs/ref/
    3. Icon Archive: https://iconarchive.com/
    4. Leshy SFMaker: https://www.leshylabs.com/apps/sfMaker/
    5. ~~XXXXXXX forgotten~~ <br><br>

------


**_What is Pygame:_**
  * Pygame provides help in display, sound, music, image, text, event
  * You can make 2D mini games with it
  * Pygame detects keyboard, joystick, and mouse <br><br>

**_3. PYGame Basics:_**
| name | Description |
|:-----:|:----------:|
| _1.py_ | Create my game surface, game loop and drawing.|
| _2.py_ | Blit text, font, sound and image objects.   |
| _3.py_ | Getting user keyboard and collision dection.|

**_4. Code snippet_**
```python
#Create game display
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Angry Bird!")

```
```python
#Blit image object and setting its rec.
player_image = pygame.image.load("angry_bird.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2
displayscreen.blit(player_image, player_rect)
```
**_5. Game Assets:_** <br>
[Icon Archive:](https://iconarchive.com/) mini game characters download <br>
[Leshy SFMaker:](https://www.leshylabs.com/apps/sfMaker/) sounds <br>

![Screenshot](https://github.com/isoavalanche/PYGAME_basics/blob/main/1.png)
