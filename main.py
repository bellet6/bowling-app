def conv_input_to_throws(input):
    frames = input.split('-')
    res = []
    for i in frames:
        if len(i)==1:
            if i=='X':
                res.append(10)
        if len(i)==2:
            if i[1]=='/':
                #Spare
                first_throw = int(i[0])
                res.append(first_throw)
                res.append(10-first_throw)
            else:
                first_throw = int(i[0])
                second_throw = int(i[1])
                res.append(first_throw)
                res.append(second_throw)
        if len(i)==3:
            if i[0]=='X':
                if i[1]=='X':
                    res.append(10)
                    if i[2]=='X':
                        res.append(10)
                
    
    return res


def calculate_score(throw_sequence,frame_number,total_score, index):
    if frame_number>10 or index>=len(throw_sequence):
        return total_score
    
    #Strike calculations
    if throw_sequence[index] == 10:
        #bonus = total of next two throws
        bonus = 0
        if len(throw_sequence) - index-1 >= 2:
            #X-4-5
            bonus = bonus+throw_sequence[index+1]
            bonus = bonus + throw_sequence[index+2]
        elif (len(throw_sequence)) - index-1 ==1:
            bonus = bonus+throw_sequence[index+1]
        return calculate_score(throw_sequence,frame_number+1,total_score+10+bonus,index+1)
    
    #Spare calculations
    if throw_sequence[index]+throw_sequence[index+1]==10:
        bonus=0
        #Only 1 bonus throw
        if (len(throw_sequence)) - index-1 >=2:
            #[3,7,5]
            bonus = bonus+throw_sequence[index+2]
        return calculate_score(throw_sequence,frame_number+1,total_score+10+bonus,index+2)

    #Open frame calculations
    else:
        #No bonus
        score = int(throw_sequence[index]) + int(throw_sequence[index+1])
        return calculate_score(throw_sequence,frame_number+1,total_score+score,index+2)


if __name__ == "__main__":
    input = input('Enter throw sequence: ')
    throws = conv_input_to_throws(input)
    print(calculate_score(throws,0,0,0))