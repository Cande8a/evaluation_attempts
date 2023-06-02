import os
import datetime
import argparse
import time 


def fotoMachen():
    parser = argparse.ArgumentParser(
        description='Long exposure with libcamera')
    parser.add_argument('--o', type=str, default='/home/XXXXX/Desktop/pictures', help='output folder')
    parser.add_argument('--g', type=int, default=5, help='gain')
    parser.add_argument('--t', type=int, default=2, help='shutterspeed') #in seconds
    parser.add_argument('--b', type=int, default=50, help='brightness')
    parser.add_argument('--sa', type=int, default=0, help='saturation')
    parser.add_argument('--c', type=int, default=0, help='contrast')
    parser.add_argument('--iso', type=int, default=800, help='iso')
    parser.add_argument('--sh', type=int, default=0, help='sharpness')
    parser.add_argument('--d', type=str, default='off', help='drc')
    parser.add_argument('--w', type=str, default='incandescent', help='white balance')

    args = parser.parse_args()
    print(args)

    folder = '{}/{}/'.format(args.o,datetime.datetime.now().strftime("%d.%m.%y"))
    os.makedirs(folder, exist_ok=True)
    print('Saving to {}'.format(folder))
    filename = folder + datetime.datetime.now().strftime("%d%m%y_%H%M%S") + '.jpg'
    os.system('libcamera-still -t {} -g {} -b {} -sa {} -c {} -iso {} -sh {} -d {} -w {} -o {}'.format(float(args.t) * 1000000, args.g, args.b, args.sa, args.c, args.iso, args.sh, args.d, args.w, filename))
    
while True:
    fotoMachen()
    end = input("Do you want to leave? Y/N ")
    if(end == 'Y' or end == 'y'):
        break
    else:
        continue
