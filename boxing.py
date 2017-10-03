import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700


class boxing(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.score = 0
        self.score_text = None

        self.punch_frame_count = 0
        self.girl_frame_count = 0

        self.sprites_list = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.punch_list = arcade.SpriteList()
        self.girl_list = arcade.SpriteList()
        self.prototype_list = arcade.SpriteList()

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

    def on_draw(self):
        arcade.start_render()
        self.sprites_list.draw()

        output = f"Score: {self.score}"
        if not self.score_text or output != self.score_text.text:
            self.score_text = arcade.create_text(output, arcade.color.WHITE, 14)
        arcade.render_text(self.score_text, 400,660)

    def update(self, delta_time):
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

        for self.prototype in self.prototype_list:
            if self.girl_frame_count % 180 == 0:
                girl = arcade.Sprite("images/girl.png",0.7)
                girl.center_x = self.prototype.center_x
                girl.angle = 0
                girl.top = self.prototype.bottom
                girl.change_y = -3
                self.girl_list.append(girl)
                self.sprites_list.append(girl)

        for punch in self.punch_list:
            if punch.top < 0:
                punch.kill()

        self.punch_list.update()
        self.girl_list.update()
        self.sprites_list.update()

        for girl in self.girl_list:

            hit_list = arcade.check_for_collision_with_list(punch,
                                                            self.girl_list)

            if len(hit_list) > 0:
                punch.kill()

            for girl in hit_list:
                girl.kill()
                self.score += 1

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.character.center_x = x
        self.character.center_y = 50


window = boxing(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()