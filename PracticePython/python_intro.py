def hi():
    print('Hi there!')
    print('How are you?')

hi()
def hi(name):
    if name == 'Kauser':
        print('Hi Kauser!')
    elif name == 'Peeps':
        print('Hi Peeps!')
    else:
        print('Hi anon!')
hi('Kauser')

def hi(name):
    print('Hi '+name+'!')

hi('Rachel')
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Kauser']

for name in girls:
    hi(name)
    print('Next girl')

for i in range(1,6):
    print(i)
