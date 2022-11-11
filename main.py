import stableDiffusion2



def main():
    image = stableDiffusion2.theAlgo(512,640)# 384, 384)
    image.generate("hello")

    image.generate("hello1")

    image.generate("hello2")


if __name__ == '__main__':
    main()
