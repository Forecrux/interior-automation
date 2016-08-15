# coding: utf-8
INPUT = "in"
OUTPUT = "out"
true = 1
false = 0
#location = "/sys/class/gpio/"

#def sunxi(path, var):
def write_gpio_file(path, var):
     doc = open(path, 'w')
     doc.write(str(var))
     doc.close()

def setup(pinnumber,mode):
    if mode == "out" or "in":
        write_gpio_file("/sys/class/gpio/export", str(pinnumber))
        if mode == OUTPUT:
            write_gpio_file("/sys/class/gpio/gpio" + str(pinnumber) + "/direction", "out")
        elif mode == INPUT:
            write_gpio_file("/sys/class/gpio/gpio" + str(pinnumber) + "/direction", "in")
    else:
        print ("Pin direction: in/out")

def clear(pinnumber):
    write_gpio_file("/sys/class/gpio/unexport", str(pinnumber))

def output(pinnumber, value):
    if value == "0" or "1":
        write_gpio_file("/sys/class/gpio/gpio" + str(pinnumber) + "/value", value)
    else:
        print ("Pin value: 1/0 1=True 0=False")
