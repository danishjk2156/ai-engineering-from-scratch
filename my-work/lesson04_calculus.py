# Lesson 4: Calculus for ML (my own implementation, written from scratch)
# Run with: python my-work/lesson04_calculus.py




# Step 1: Numerical derivative

def f(x):
    return x*x
def numerical(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)
def f3(x):
    return x*x+x

x=1.0
h=0.0001
for x in range(-2,3):
    print(x,numerical(f,x,h))

def f2(x,y):
    return x*x+y*y+3*y*x

def partialx(f,x,y,h):
    return (f(x+h,y)-f(x-h,y))/(2*h)
def partialy(f,x,y,h):
    return (f(x,y+h)-f(x,y-h))/(2*h)


def gradient(f,x,y,h):
    return (partialx(f,x,y,h),partialy(f,x,y,h))
print(gradient(f2,1,2,0.0001))


x=5.0
lr=0.1
def gradientds(x,lr):
    return x-lr*(numerical(f3,x,h))

lr=[0.1,0.5,1.0,1.1]
for l in lr:
    print(f"learning rate: {l}")
    x=5.0
    for i in range(20):
        x=gradientds(x,l)
        print(x,f3(x))
def bowl(x,y):
    return x**2+y**2

def gradientds2d(x,y,lr,f):
    gx,gy=gradient(f,x,y,h)
    return (x-lr*gx,y-lr*gy)

x=4
y=3
for i in range(10):
    x,y=gradientds2d(x,y,0.1,bowl)
    if i % 5 == 0:
        print(x,y,bowl(x,y))
print(x,y,bowl(x,y))
x=4
y=3
for i in range(30):
    x,y=gradientds2d(x,y,0.1,f2)
    if i % 5 == 0:
        print(x,y,f2(x,y))
print(x,y,f2(x,y))
