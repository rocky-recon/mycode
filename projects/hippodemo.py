
#Garden:
    #pic: "hippo.txt"



def hippo_pic(filename):
    with open("/home/student/mycode/projects/"+filename, "r") as hippo:
        print(hippo.read())

hippo_pic("start_game.txt")
