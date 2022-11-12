import stableDiffusion2



def main():
    image = stableDiffusion2.theAlgo(512,640)# 384, 384)
    print(image.generate("Benjamin Ashton the Mac lover"))


if __name__ == '__main__':
    main()
