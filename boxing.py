import arcade
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

class boxing(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.score = 0
        self.score_text = None
        self.times = 0.0

        self.is_game_over = False
        self.punch_frame_count = 0
        self.girl_frame_count = 0

        self.sprites_list = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.punch_list = arcade.SpriteList()
        self.girl_list = arcade.SpriteList()
        self.grade_list = arcade.SpriteList()
        self.prototype_list = arcade.SpriteList()
        self.fire_list = arcade.SpriteList()

        self.character = arcade.Sprite("images/boy.png")
        self.sprites_list.append(self.character)
        self.character_list.append(self.character)

        for i in range(8):
            self.prototype = arcade.Sprite("images/girl.png", 0.5)
            self.prototype.center_x = SCREEN_WIDTH - 70*i
            self.prototype.center_y = SCREEN_HEIGHT + 50
            self.prototype.angle = 0
            self.sprites_list.append(self.prototype)
            self.prototype_list.append(self.prototype)

        for j in range(8):
            self.fire = arcade.Sprite("images/f.png", 0.7)
            self.fire.center_x = SCREEN_WIDTH - 70*j
            self.fire.center_y = SCREEN_HEIGHT + 60
            self.fire.angle = 0
            self.sprites_list.append(self.fire)
            self.fire_list.append(self.fire)

        self.coin = arcade.Sprite('images/score.png',0.35)
        self.coin.set_position(430 , 670)

    def on_draw(self):
        arcade.start_render()

        if self.is_game_over:
            self.draw_game_over()
            return None
        self.sprites_list.draw()

        output = "{}".format(self.score)
        if not self.score_text or output != self.score_text.text:
            self.score_text = arcade.create_text(output, arcade.color.GOLD, 16)
        arcade.render_text(self.score_text, 450,662)
        self.coin.draw()

    def draw_game_over(self):
        output = "Score : {}".format(self.score)
        arcade.draw_text(output, 160, 440, arcade.color.WHITE, 40)
        output1 = "Game Over"
        arcade.draw_text(output1, 150, 370, arcade.color.WHITE, 35)
        output2 = "Click Play Again"
        arcade.draw_text(output2, 150, 290, arcade.color.WHITE, 24)

    def update(self, delta_time):
        if self.is_game_over:
            self.draw_game_over()
            return None

        self.times += delta_time
        self.punch_frame_count += 1

        for character in self.character_list:
            if self.punch_frame_count % 10 == 0:
                punch = arcade.Sprite("images/punch.png",0.7)
                punch.center_x = self.character.center_x
                punch.angle = 0
                punch.top = self.character.top
                punch.change_y = 5
                self.punch_list.append(punch)
                self.sprites_list.append(punch)

        self.girl_frame_count += 1
        if self.times < 20:
            for self.prototype in self.prototype_list:
                if self.girl_frame_count % 180 == 0:
                    girl = arcade.Sprite("images/girl.png",0.7)
                    girl.center_x = self.prototype.center_x
                    girl.angle = 0
                    girl.top = self.prototype.bottom
                    girl.change_y = -3
                    self.girl_list.append(girl)
                    self.sprites_list.append(girl)
        if self.times > 20 and self.times < 40:
            for self.prototype in self.prototype_list:
                if self.girl_frame_count % 100 == 0:
                    girl = arcade.Sprite("images/girl.png",0.7)
                    girl.center_x = self.prototype.center_x
                    girl.angle = 0
                    girl.top = self.prototype.bottom
                    girl.change_y = -3
                    self.girl_list.append(girl)
                    self.sprites_list.append(girl)
        if self.times >40 and self.times < 45:
            for self.prototype in self.prototype_list:
                if self.girl_frame_count % 20 == 0:
                    girl = arcade.Sprite("images/coin.png")
                    girl.center_x = self.prototype.center_x
                    girl.angle = 0
                    girl.top = self.prototype.bottom
                    girl.change_y = -3
                    self.girl_list.append(girl)
                    self.sprites_list.append(girl)
        if self.times > 45:
            for self.prototype in self.prototype_list:
                if random.randrange(100) == 0:
                    girl = arcade.Sprite("images/girl.png",0.7)
                    girl.center_x = self.prototype.center_x
                    girl.angle = 0
                    girl.top = self.prototype.bottom
                    girl.change_y = -3
                    self.girl_list.append(girl)
                    self.sprites_list.append(girl)

        if self.times < 30:
            for self.fire in self.fire_list:
                if random.randrange(3000) == 0:
                    grade = arcade.Sprite("images/f.png",0.8)
                    grade.center_x = self.fire.center_x
                    grade.angle = 180
                    grade.top = self.fire.bottom
                    grade.change_y = -9
                    self.grade_list.append(grade)
                    self.sprites_list.append(grade)
        if self.times > 30:
            for self.fire in self.fire_list:
                if random.randrange(1000) == 0:
                    grade = arcade.Sprite("images/f.png",0.8)
                    grade.center_x = self.fire.center_x
                    grade.angle = 180
                    grade.top = self.fire.bottom
                    grade.change_y = -9
                    self.grade_list.append(grade)
                    self.sprites_list.append(grade)

        for punch in self.punch_list:
            if punch.top < 0:
                punch.kill()

        for girl in self.girl_list:
            if girl.bottom < 0:
                girl.kill()

        self.punch_list.update()
        self.girl_list.update()
        self.sprites_list.update()

        for punch in self.punch_list:
            hit_list = arcade.check_for_collision_with_list(punch,self.girl_list)
            if len(hit_list) > 0:
                punch.kill()
            for girl in hit_list:
                girl.texture = arcade.load_texture("images/coin.png")
                girl.change_y = -4
                for character in self.character_list:
                    keep_list = arcade.check_for_collision_with_list(character,self.girl_list)
                    for girl in keep_list:
                        girl.kill()
                        self.score += 1

        for grade in self.grade_list:
            game_list = arcade.check_for_collision_with_list(grade,self.character_list)
            for grade in game_list:
                self.is_game_over = True
                break

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.character.center_x = x
        self.character.center_y = 100

def main():
    window = boxing(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
