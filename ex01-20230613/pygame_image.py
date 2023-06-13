import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20230613/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    #kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    kk_imgs = [kk_img,pg.transform.rotozoom(kk_img,10,1.0),pg.transform.rotozoom(kk_img,20,1.0),pg.transform.rotozoom(kk_img,30,1.0),pg.transform.rotozoom(kk_img,40,1.0),pg.transform.rotozoom(kk_img,50,1.0),pg.transform.rotozoom(kk_img,60,1.0)]
    bg_imgs = [bg_img,pg.transform.flip(bg_img,True,False)]
    
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x+=1
        if x==3200:
            x=0
        
            
        
        screen.blit(bg_imgs[0], [-x, 0])
        screen.blit(bg_imgs[1], [1600-x, 0])
        screen.blit(kk_imgs[tmr%2],[300,200])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kk_imgs[tmr%2],[300,200])
        
        #kk_rct = kk_img.get_rect()
        #screen.blit(bg_imgs,[-x,200])
        #kk_rct.center = 300,200
        #screen.blit(kk_img,kk_rct)


        pg.display.update()
        tmr += 1        
        clock.tick(500)
        
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()