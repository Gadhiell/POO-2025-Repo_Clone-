import  pygame as pg

pg.init()

#configuracion de ventana(tamaño y nombre)
Window = pg.display.set_mode((800,600))
pg.display .set_caption("Nombre de ventana")

#variables de colores (formato RGB)
background = (0,0,0)
yellow = (235,255,0)
light_Blue = (0,255,255)
pink = (255,0,255)

clock = pg.time.Clock()
FPS = 30
running = True

while True:
    dt = clock.tick(FPS) / 1000.0
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    Window.fill(background)   #añadir el color del fondo 
    
    #Dibujo de figuras
    pg.draw.circle(Window,light_Blue, (400,400), 80)
    pg.draw.rect(Window,pink, (200,250,80,50))
    
    #vertices 
    v = [(400,110),(350,200),(450,200)]
    
    pg.draw.polygon(Window, yellow, v)
    
    
    pg.display.update()
    
    pg.display.flip()
    
pg.quit()