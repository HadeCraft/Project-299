from controller import Robot

bot = Robot()

timestep = 64

left_wheel = bot.getDevice('left_front_wheel')
right_wheel = bot.getDevice('right_front_wheel')
l_steer = bot.getDevice('left_steer')
r_steer = bot.getDevice('right_steer')

left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))

l_steer.setPosition(0)
r_steer.setPosition(0)
left_wheel.setVelocity(0)
right_wheel.setVelocity(0)

while bot.step(timestep) != -1:
    
    left_wheel.setVelocity(10)
    right_wheel.setVelocity(10)
    
    
    
    
