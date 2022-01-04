import easytello as tello
from pyPS4Controller.controller import Controller


drone = tello.Tello()
    
class MyController(Controller):
    
    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        drone.forward(40)

        
    def on_down_arrow_press(self):
        drone.back(40)

        
    def on_right_arrow_press(self):
        drone.right(40)
        
        
    def on_left_arrow_press(self):
        drone.left(40)

        
    def on_circle_press(self):
        drone.land()
        
    def on_x_press(self):
        drone.takeoff()
        
    def on_R1_press(self):
        drone.up(40)
		
    def on_L1_press(self):
        drone.down(40)
		
    def on_square_press(self):
	drone.cw(90)
		
    def on_triangle_press(self):
	drone.ccw(90)
		
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)



