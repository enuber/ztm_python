def decode(message_file):
    # step 1: read the file to get the incoming data
    with open(message_file, mode='r') as file:
        lines = file.readlines()

    # step 2: create a dictionary to store each line from the file
    word_dict = {}
    for line in lines:
        number, word = line.strip().split(' ')
        word_dict[int(number)] = word

    # step 3: find the index numbers that end each level of the pyramid
    current_number = 1
    level = 1
    end_number_of_pyramid_level = []
    while current_number <= max(word_dict.keys()):
        end_number_of_pyramid_level.append(current_number + (level - 1))
        current_number += 1
        level += 1

    # step 4: create a list of last word in each level of they pyramid
    final_message_words = [word_dict[i]
                           for i in end_number_of_pyramid_level if i in word_dict]

    # step 5: return the message as a complete sentence
    return (' '.join(final_message_words))


# example of how to call the decode function assuming a file of name 'sample.txt'
print(decode('coding_qual_input.txt'))
