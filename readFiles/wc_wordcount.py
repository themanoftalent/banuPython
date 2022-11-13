import sys
import os


def main():
    if len(sys.argv) < 2:
        filepath = input("Enter file path here:")
    else:
        filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting ...".format(filepath))
        sys.exit()

    bag_of_words = {}
    with open(filepath) as fp:
        cnt = 1
        for line in fp:
            cnt += 1
            print("line {} contents {}".format(cnt, line))


if __name__ == '__main__':
    main()
