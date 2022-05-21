import math
import matplotlib.pyplot as plt

# constants
g = 9.806  # gravity
rho = 1.225  # densty of air
A = 5  # cross sectional area
C_d = 0.012  # drag coefficient of air
k = rho * A * C_d / 2



#
# Decimal Range Function
def d_range(i, f, f_i):
    while i < f:
        yield i
        i += f_i

print("------------------------------")
h0 = int(input("Height (m) : "))
v0 = int(input("Initial Velocity (m/s) : "))
mass = int(input("mass (kg) : "))





vf = math.sqrt(mass * g / k)  # Terminal Velocity
t = 0  # starting time
time_step = 0.0001  # time steps
tmax = (vf / g) * math.atan(v0 / vf)  # different measures of final time
tmax1 = (vf / g) * math.acosh(math.exp(h0 * g / (vf ** 2)))
tmax2 = (vf / g) * (math.acosh(math.exp(g * h0 / (vf ** 2) + math.log(abs(math.cosh(math.atan(v0 / vf)))))) - math.atan(
    v0 / vf))


# lists for our data
time = []
velocity = []
height = []


if v0 < 0:  # if our starts with negative speed
    for t in d_range(0, tmax2 + time_step, time_step):
        v = vf * math.tanh(t * (-g / vf) + math.atanh(v0 / vf))
        h = h0 + (vf ** 2 / -g) * (math.log(abs(math.cosh(math.atan(v0 / vf) - g * t / vf))) - math.log(
            abs(math.cosh(math.atan(v0 / vf)))))
        if h >= 0:
            time.append(t)
            velocity.append(v)
            height.append(h)

else:
    if v0 == 0:  # if our starts with no speed
        for t in d_range(0, tmax1 + time_step, time_step):
            v = vf * math.tanh(t * (-g / vf))
            h = h0 - ((vf ** 2) / g) * math.log(math.cosh(t * -g / vf))
            if h >= 0:
                time.append(t)
                velocity.append(v)
                height.append(h)

    elif v0 > 0:   # if our starts with negative speed
        for t in d_range(0, tmax, time_step):
            v = vf * math.tan(math.atan(v0 / vf) - g * t / vf)
            h = h0 - (mass / k) * math.log((math.cos(math.atan(v0 / vf))) / (math.cos(math.atan(v0 / vf) - g * t / vf)))
            hmax = h
            ft0 = (vf / g) * math.acosh(math.exp(hmax * g / (vf ** 2)))
            time.append(t)
            velocity.append(v)
            height.append(h)
        for t in d_range(tmax, tmax + ft0 + time_step, time_step):
            v = vf * math.tanh((t - tmax) * (-g / vf))
            h = hmax - ((vf ** 2) / g) * math.log(math.cosh((t - tmax) * -g / vf))
            if h >= 0:
                time.append(t)
                velocity.append(v)
                height.append(h)






file = open("results.dat", "w")  # writes results in new file
for n in range(len(time)):
    file.write("{0:0.3f} {1:10.3f} {2:15.3f}\n".format(time[n], height[n], velocity[n]))
file.close()




# Reading the File
file = open("results.dat", "r")
f = file.read()
print(f)




# plot our data
plt.plot(time, height, "b", label="Position [m]")
plt.xlabel('Time [s]')
plt.ylabel('Position [m]')
plt.title('Height vs Time')
plt.legend()
plt.minorticks_on()
plt.grid()
plt.show()

plt.plot(time, velocity, "k", label="Velocity [m/s]")
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.title('Velocity vs Time')
plt.legend()
plt.minorticks_on()
plt.grid()
plt.show()

plt.plot(time, height, "b", label="Height [m]")
plt.plot(time, velocity, "k", label="Velocity [m/s]")
plt.xlabel('Time [s]')
plt.title('Position & Velocity vs Time')
plt.legend()
plt.minorticks_on()
plt.grid()
plt.show()
