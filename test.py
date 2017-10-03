import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700


class boxing(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0
        self.frame_count1 = 0

        self.sprites_list = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.character = arcade.Sprite("images/boy.png")
        self.sprites_list.append(self.character)
        self.character_list.append(self.character)

        for i in range(8):
            self.enemy = arcade.Sprite("images/girl.png", 0.5)
            self.enemy.center_x = SCREEN_WIDTH - 70*i
            self.enemy.center_y = SCREEN_HEIGHT + 50
            self.enemy.angle = 0
            self.sprites_list.append(self.enemy)
            self.enemy_list.append(self.enemy)

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

        self.frame_count1 += 1

        for self.enemy in self.enemy_list:
            if self.frame_count1 % 180 == 0:
                bullet1 = arcade.Sprite("images/girl.png",0.7)
                bullet1.center_x = self.enemy.center_x
                bullet1.angle = 0
                bullet1.top = self.enemy.bottom
                bullet1.change_y = -3
                self.bullet_list.append(bullet1)
                self.sprites_list.append(bullet1)

        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.kill()

        self.bullet_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.character.center_x = x
        self.character.center_y = 50


window = boxing(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()