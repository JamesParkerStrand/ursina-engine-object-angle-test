from ursina import *

app = Ursina()

def update():
    hit = car.intersects()
    if not hit.hit:
        car.y -= time.dt
    if hit.hit:
        ### I need to do calculations between the car and the gyroscope (ballpoint), and determine the angle for x,y and z. Do not change the same angle as the same object. Otherwise you will have entire terrain mesh that wont work this out
        #this should give you the hit point
        zrot = car.position[0] - hit.world_point[0]
        xrot = car.position[2] - hit.world_point[2]
        car.rotation_z += zrot
        car.rotation_x += xrot


car = Entity(model="cube", scale=(6,1,2),position=(2,4,-1), collider="box", color=color.blue)


cube = Entity(model="cube", color=color.yellow, collider="box")
slope = Entity(model="plane", collider="box", scale=20,position=(0,0,0))

EditorCamera()

app.run()
