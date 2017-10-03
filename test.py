import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class boxing(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0

        self.sprites_list = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.character = arcade.Sprite("images/boy.png")

        self.sprites_list.append(self.character)
        self.character_list.append(self.character)

    def on_draw(self):
        arcade.start_render()
        self.sprites_list.draw()

    def update(self, delta_time):
        self.frame_count += 1

        for character in self.character_list:
            if self.frame_count % 10 == 0:
                bullet = arcade.Sprite("images/punch.png",0.7)
                bullet.center_x = self.character.center_x
                bullet.angle = 0
                bullet.top = self.character.top
                bullet.change_y = 5
                self.bullet_list.append(bullet)
                self.sprites_list.append(bullet)

        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.kill()

        self.bullet_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.character.center_x = x
        self.character.center_y = 50


window = boxing(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()