import arcade
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

class Model_S:
    def __init__(self, picture, size, speed):
        self.model_list = arcade.SpriteList()
        self.picture = picture
        self.speed = {}
        self.tag = {}
        self.size = size
        self.tempSpeed = speed
    def generate(self):
        for i in range(8):
            girl = arcade.Sprite(self.picture, self.size)
            girl.center_x = SCREEN_WIDTH - 70*i
            girl.center_y = SCREEN_HEIGHT + 50
            self.model_list.append(girl)
            self.speed[girl.center_x] = self.tempSpeed
            self.tag[girl.center_x] = "girl"
            
    def run(self):
        for girl in self.model_list:
            girl.center_y -= self.speed[girl.center_x]
    def draw(self):
        for girl in self.model_list:
            girl.draw()
class Knife_S:
    def __init__(self, picture, size, speed):
        self.model_list = arcade.SpriteList()
        self.picture = picture
        self.speed = {}
        self.size = size
        self.tempSpeed = speed
    def generate(self):
        prototype = arcade.Sprite(self.picture, self.size)
        prototype.center_x = random.randrange(500)
        prototype.center_y = SCREEN_HEIGHT + 60
        prototype.angle = 180 
        self.model_list.append(prototype)
        self.speed[prototype.center_x] = self.tempSpeed            
    def run(self):
        for prototype in self.model_list:
            prototype.center_y -= self.speed[prototype.center_x]
    def draw(self):
        for prototype in self.model_list:
            prototype.draw()

class Basket_S:
    def __init__(self, picture, size, speed):
        self.model_list = arcade.SpriteList()
        self.picture = picture
        self.speed = {}
        self.size = size
        self.tempSpeed = speed
    def generate(self):
        basket = arcade.Sprite(self.picture, self.size)
        basket_half_width = basket.width // 2
        basket.center_x = random.randint(basket_half_width, SCREEN_WIDTH - basket_half_width)
        basket.center_y = SCREEN_HEIGHT + 70
        self.model_list.append(basket)
        self.speed[basket.center_x] = self.tempSpeed            
    def run(self):
        for basket in self.model_list:
            basket.center_y -= self.speed[basket.center_x]
    def draw(self):
        for basket in self.model_list:
            basket.draw()

class boxing(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        #arcade.set_background_color(arcade.color.BLACK
        self.background = arcade.load_texture("images/bgnew.jpg")
        self.score = 0
        self.score_text = None
        self.times = 0.0
        self.state = False

        self.is_game_over = False
        self.punch_frame_count = 0

        self.sprites_list = arcade.SpriteList()
        self.character_list = arcade.SpriteList()
        self.punch_list = arcade.SpriteList()

        self.character = arcade.Sprite("images/boy.png")
        self.character_half_width = self.character.width // 2
        self.sprites_list.append(self.character)
        self.character_list.append(self.character)

        self.coin = arcade.Sprite('images/score.png',0.35)
        self.coin.set_position(430 , 670)

        self.girl = []
        self.girl.append(Model_S("images/girl.png",0.7,3))
        self.girl[0].generate()
        self.girl.append(Model_S("images/girl.png",0.7,3))
        self.girl[1].generate()
        self.check = False
        self.knife = []
        self.knife.append(Knife_S("images/knife.png",0.8,9))
        self.knife[0].generate()
        self.knife.append(Knife_S("images/knife.png",0.8,9))
        self.knife[1].generate()
        self.basket = []
        self.basket.append(Basket_S("images/basket.png",0.8,6))
        self.basket[0].generate()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)

        if self.is_game_over:
            self.draw_game_over()
            return None
        self.sprites_list.draw()

        output = "{}".format(self.score)
        if not self.score_text or output != self.score_text.text:
            self.score_text = arcade.create_text(output, arcade.color.GOLD, 16)
        arcade.render_text(self.score_text, 450,662)
        self.coin.draw()
        self.girl[0].draw()
        self.girl[1].draw()
        self.knife[0].draw()
        self.knife[1].draw()
        self.basket[0].draw()
        #self.basket[1].draw()

    def draw_game_over(self):
        output = "Score : {}".format(self.score)
        arcade.draw_text(output, 155, 440, arcade.color.WHITE, 40)
        output1 = "Game Over"
        arcade.draw_text(output1, 150, 370, arcade.color.WHITE, 35)
        output2 = "Enter Play Again"
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
                punch.top = self.character.top
                punch.change_y = 5
                self.punch_list.append(punch)
                self.sprites_list.append(punch)

        if self.times < 20:
            self.girl[0].run()
            if(self.girl[0].model_list[0].center_y < 20):
                self.girl[0] = Model_S("images/girl.png",0.7,3)
                self.girl[0].generate()
        if self.times >20 and self.times < 40:
            self.girl[0].run()
            if(self.girl[0].model_list[0].center_y < 100):
                self.girl[1] = self.girl[0]
                self.girl[0] = Model_S("images/girl.png",0.7,3)
                self.girl[0].generate()
                self.check = True
            if self.check:
                self.girl[1].run()
        if self.times >40 and self.times < 60:
            self.girl[0].run()
            if(self.girl[0].model_list[0].center_y < 200):
                self.girl[1] = self.girl[0]
                self.girl[0] = Model_S("images/girl.png",0.7,3)
                self.girl[0].generate()
                self.check = True
            if self.check:
                self.girl[1].run()
        if self.times >60:
            self.girl[0].run()
            if(self.girl[0].model_list[0].center_y < 300):
                self.girl[1] = self.girl[0]
                self.girl[0] = Model_S("images/girl.png",0.7,4)
                self.girl[0].generate()
                self.check = True
            if self.check:
                self.girl[1].run()

        for i in [0,1]:
            for punch in self.punch_list:
                hit_list = arcade.check_for_collision_with_list(punch,self.girl[i].model_list)
                if len(hit_list) > 0:
                    punch.kill()
                for girl in hit_list:
                    girl.texture = arcade.load_texture("images/coin.png")
                    self.girl[i].tag[girl.center_x] = "coin"
                    self.girl[i].speed[girl.center_x] = 5
                for character in self.character_list:
                    keep_list = arcade.check_for_collision_with_list(character,self.girl[i].model_list)
                    for girl in keep_list:
                        if self.girl[i].tag[girl.center_x] == "coin":
                            girl.kill()
                            self.score += 1
                        else :
                            self.is_game_over = True
                            self.state = True

        if self.times < 30:
            self.knife[0].run()
            if(self.knife[0].model_list[0].center_y < 20):
                self.knife[0] = Knife_S("images/knife.png",0.8,9)
                self.knife[0].generate()
        if self.times > 30 and self.times < 50:
            self.knife[0].run()
            if(self.knife[0].model_list[0].center_y < 100):
                self.knife[1] = self.knife[0]
                self.knife[0] = Knife_S("images/knife.png",0.8,9)
                self.knife[0].generate()
                self.check = True
            if self.check:
                self.knife[1].run()
        if self.times >50 and self.times < 70:
            self.knife[0].run()
            if(self.knife[0].model_list[0].center_y < 200):
                self.knife[1] = self.knife[0]
                self.knife[0] = Knife_S("images/knife.png",0.8,9)
                self.knife[0].generate()
                self.check = True
            if self.check:
                self.knife[1].run()
        if self.times >70:
            self.knife[0].run()
            if(self.knife[0].model_list[0].center_y < 100):
                self.knife[1] = self.knife[0]
                self.knife[0] = Knife_S("images/knife.png",0.8,9)
                self.knife[0].generate()
                self.check = True
            if self.check:
                self.knife[1].run()

        for punch in self.punch_list:
            if punch.top < 0:
                punch.kill()

        self.punch_list.update()
        self.sprites_list.update()

        for j in [0,1]:
            for character in self.character_list:
                game_list = arcade.check_for_collision_with_list(character,self.knife[j].model_list)
                for knife in game_list:
                    self.is_game_over = True
                    self.state = True
                    #break
        if self.times > 0 and self.times < 10: # 50, 70
            self.basket[0].run()
            self.init_second_basket = True
            #if(self.basket[0].model_list[0].center_y < 30):
                #self.basket[0] = Basket_S("images/basket.png",0.8,6)
                #self.basket[0].generate()
        if self.times > 10 and self.times < 20: # 100 120
            if self.init_second_basket:
                self.basket[0] = Basket_S("images/basket.png",0.8,6)
                self.basket[0].generate()
                self.init_second_basket = False
                self.init_third_basket = True
            self.basket[0].run()

        if self.times > 20 and self.times < 30: # 200 220
            if self.init_third_basket:
                self.basket[0] = Basket_S("images/basket.png",0.8,6)
                self.basket[0].generate()
                self.init_third_basket = False
            self.basket[0].run()

        for k in [0]:
            for punch in self.punch_list:
                hit_list = arcade.check_for_collision_with_list(punch,self.basket[k].model_list)
                if len(hit_list) > 0:
                    punch.kill()
                for basket in hit_list:
                    basket.texture = arcade.load_texture("images/money.png")
                    self.basket[k].speed[basket.center_x] = 7
                for character in self.character_list:
                    keep_list = arcade.check_for_collision_with_list(character,self.basket[k].model_list)
                    for basket in keep_list:
                            basket.kill()
                            self.score += 10


    def on_mouse_press(self, x, y, button, modifiers):
        if self.state == True:
            self.update()
            self.state = False

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        if x < self.character_half_width:
            self.character.center_x = character_half_width
        elif x > SCREEN_WIDTH - self.character_half_width:
            self.character.center_x = SCREEN_WIDTH - self.character_half_width
        else:
            self.character.center_x = x
        self.character.center_y = 100

def main():
    window = boxing(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()

