def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    if fastest == True:
        return getfastestSpeed(redShirtSpeeds,blueShirtSpeeds)
    else:
        return getslowestSpeed(redShirtSpeeds,blueShirtSpeeds)
        
def getfastestSpeed(redShirtsSpeeds,blueShirtSpeeds):
    redShirtsSpeeds.sort(reverse=True)
    blueShirtSpeeds.sort()

    fastestSpeed = 0
    for redspeed, bluespeed in zip(redShirtsSpeeds, blueShirtSpeeds):
            fastestSpeed += max(redspeed, bluespeed)
    return fastestSpeed

def getslowestSpeed(redShirtsSpeeds,blueShirtSpeeds):
    redShirtsSpeeds.sort()
    blueShirtSpeeds.sort()

    slowestSpeed = 0
    for redspeed, bluespeed in zip(redShirtsSpeeds, blueShirtSpeeds):
            slowestSpeed += max(redspeed, bluespeed)
    return slowestSpeed











