input_file = 'd_pet_pictures.txt'
output_file = 'output_d_pet_pictures.txt'

input_val = open(input_file, "r")
each_line = input_val.readlines()

# remove the previous total pictures
photos = each_line[1:]

output = open(output_file, 'w')

# total after getting hotizontal and vertical pictures
after_total = 0
jump_v = 0

print("checking and reordering slides pictures \n")

for a in range(len(photos)):
    new_a = photos[a].split(' ')
    if new_a[0] == 'H':
        """
        #reveal answer
        print("for horizontal data: \n")
        print(new_a[1:])
        output.write(str(a)+",".join(new_a[1:]))
        """
        
        #for hashcode answers
        after_total += 1
        output.write(str(a)+"\n")
        
        print(".")

    if new_a[0] == 'V':
        # start checking vertical slides
        # print("for vertical data: \n")

        # check if this is the end of the file
        if a+1 >= len(photos):
            output.write(str(a)+"\n")
            after_total += 1
            print('file end with slide V')
            break
        else:
            #go to next line
            new_b = photos[a+1].split(' ')

        #check previous line has a vertical picture and jump to the next loop
        prev_b = photos[a-1].split(' ')
        if prev_b[0] == 'V' and jump_v:
            jump_v = 0
            continue
        
        elif new_b[0] == 'V':
            mid_a_data = new_a[2:]
            mid_b_data = new_b[2:]

            #remove new line(\n) in array to check for similar element
            new_a_data = ','.join(mid_a_data).split('\n')[0].split(',')
            new_b_data = ','.join(mid_b_data).split('\n')[0].split(',')
            
            i = 0
            j = 0
            similar = []
            not_similar = []
            while(i < len(new_a_data) and j < len(new_b_data)):
                if new_a_data[i] == new_b_data[j]:
                    similar.append(new_a_data[i])
                    jump_v = 1
                    
                    i += 1
                    j += 1
                elif new_a_data[i] < new_b_data[j]:
                    not_similar.append(new_b_data[j])
                    i += 1
                else:
                    not_similar.append(new_a_data[i])
                    j += 1
            
            #print('similar content: '+",".join(similar)+"\n end similar \n")
            """
            #reveal answer
            print('not similar content: '+",".join(not_similar)+"\n end similar \n")     
            output.write(",".join(similar) +", "+ ",".join(not_similar)+"\n")
            """
            
            #for hashcode answers
            # check if there is similarities
            if len(similar):
                output.write(str(a)+" "+str(a+1)+"\n")
            else:
                output.write(str(a)+"\n")
                
            after_total += 1
            
            print(".")

        else:
            """
            #reveal answer
            print(new_a[1:])
            output.write(",".join(new_a[1:]))
            """
            output.write(str(a)+"\n")
            after_total += 1
            
            print(".")

input_val.close()
output.close()

# get total pictures in the new file
output_read = open(output_file, 'r')
original_output = output_read.read()
output_read.close()

#append total slides at the top
output_read = open(output_file, 'w')
output_read.write(str(after_total)+"\n")
output_read.write(original_output)
output_read.close()


print("\nDone")

