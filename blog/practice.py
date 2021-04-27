def minimumDistance(area):
    count=0
    for i in range(len(area)):
        for j in range(len(area[i])):
            el=area[i][j]
    #         if el == 1:
    #             count+=1
    #         elif el == 0:
    #             continue
    #         elif el == 9:
    #             break
    #         else:
    #             return -1
    # print(count)
            print(el)



if __name__ == '__main__':
    # area_rows = int(input().strip())
    # area_columns = int(input().strip())

    area = [[1,0,0],
            [1,0,0],
            [1,9,1],
            [1,2]]

    # for _ in range(area_rows):
    #     area.append(list(map(int, input().rstrip().split())))

    result = minimumDistance(area)



'''
question2:-
import os
# return <-1,-1>
def findSongs(rideDuration, songDurations):
    time_playback = rideDuration - 30
    l=[]
    # return_value
    # i=1
    # for item in songDurations:
    #     for k in range(len(songDurations)-1):
    #         newtime=item+songDurations[i]
    #         print(newtime)
    #         i+=1
    for i in range(len(songDurations)):

        for j in range(i + 1, len(songDurations)):
            newitem = songDurations[i]+songDurations[j]
            if newitem == time_playback:
                l.append(i)
                l.append(j)


    print(l)




# Write your code here [1,10,25,35,60]

if __name__ == '__main__':

    rideDuration = 90

    # songDurations_count = int(input("enter songs duration").strip())

    songDurations = [1,10,25,35,60]

    # for _ in range(songDurations_count):
    #     songDurations_item = int(input().strip())
    #     songDurations.append(songDurations_item)


    result = findSongs(rideDuration, songDurations)

'''
def findSongs(rideDuration, songDurations):
    time_playback = rideDuration-30

    l=[]
    for i in range(len(songDurations)):
        for j in range(i+1,len(songDurations)):
            newitem = songDurations[i]+songDurations[j]
            if newitem == time_playback:
                l.append(i)
                l.append(j)
                print(l)





    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rideDuration = int(input().strip())

    songDurations_count = int(input().strip())

    songDurations = []

    for _ in range(songDurations_count):
        songDurations_item = int(input().strip())
        songDurations.append(songDurations_item)

    result = findSongs(rideDuration, songDurations)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
'''

'''
