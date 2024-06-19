# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

# Extra:

# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.


with open('20_data.txt', mode='r') as file:
    # data2 = list(file.readlines()) # note that this leave in the \n at the end of each line.

    # doing it this way there is no \n at end of line.
    data2 = []
    line = file.readline()
    while line:
        line = line.strip()
        data2.append(line)
        line = file.readline()


def count_categories(data):
    categories = {}
    for line in data:
        li = line.split('/')
        li.pop(0)
        cat_name = li[1]
        if cat_name in categories:
            categories[cat_name] += 1
        else:
            categories[cat_name] = 1
    return categories


category_count = count_categories(data2)
