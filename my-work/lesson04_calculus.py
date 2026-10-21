# Lesson 4: Calculus for ML (my own implementation, written from scratch)
# Run with: python my-work/lesson04_calculus.py




# Step 1: Numerical derivative

def f(x):
    return x*x
def numerical(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

x=1.0
h=0.0001
for x in range(-2,3):
    print(x,numerical(f,x,h))

def f2(x,y):
    return x*x+y*y+3*y*x

def partialx(f2,x,y,h):
    return (f2(x+h,y)-f2(x-h,y))/(2*h)
def partialy(f2,x,y,h):
    return (f2(x,y+h)-f2(x,y-h))/(2*h)


def gradient(f2,x,y,h):
    return (partialx(f2,x,y,h),partialy(f2,x,y,h))
print(gradient(f2,1,2,0.0001))
    