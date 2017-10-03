import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyApplication(arcade.Window):
    """ Main application class """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0

        self.all_sprites_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.enemy = arcade.Sprite("images/cat.png", 0.5)
        self.all_sprites_list.append(self.enemy)
        self.enemy_list.append(self.enemy)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()

        self.all_sprites_list.draw()
        # Draw the text
        arcade.draw_text("This is a simple template to start your game.",
                         10, SCREEN_HEIGHT // 2, arcade.color.BLACK, 20)

    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        self.frame_count += 1

        for enemy in self.enemy_list:
            if self.frame_count % 10 == 0:
                bullet = arcade.Sprite("images/punch.png",0.5)
                bullet.center_x = self.enemy.center_x
                bullet.center_y = self.enemy.center_y + 5
                bullet.angle = 0
                bullet.top = self.enemy.bottom
                bullet.change_y = 5
                self.bullet_list.append(bullet)
                self.all_sprites_list.append(bullet)

        # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.kill()

        self.bullet_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.enemy.center_x = x
        self.enemy.center_y = 20


window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()