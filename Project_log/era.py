ERA = 9 * (float(input("Earned innings allowed: ")) / float(input("Innings Pitched: ")))
if(ERA > 5 and ERA <= 6):
    print("Era is worse than average")
if ERA < 2:
    print(ERA, ": Considered exceptional and is rare")
if ERA > 2 and ERA <= 3:
    print(ERA, ": Excellent, only achieved by the best pitchers in the league")
if ERA > 3 and ERA <= 4:
    print(ERA, ": Better than average")
if ERA > 4 and ERA <= 5:
    print(ERA, ": Average")
if ERA > 5 and ERA <= 6 :
    print(ERA, ": Worse than average")
if ERA > 6:
    print(ERA, ": Consistently having this ERA risks high risks demotion to the bulletpen, or lower league")