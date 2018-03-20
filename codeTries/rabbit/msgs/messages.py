class messages:
    @staticmethod
    def dequeueOrder():
        location=(1,2)
        numberOfPassengers=3
        destination=(7,7)
        return(location,numberOfPassengers,destination)

    @staticmethod
    def orderToCar(location,numberOfPassengers,destination):
        return(location,numberOfPassengers,destination)


    @staticmethod
    def strToPoint(string):
        i=1
        j=i

        char=string[j]
        while char!=',' and char!=')':
            j+=1
            char=string[j]

        x=float(string[i:j]) #position x

        if char==')':
            return(x,0)

        j+=1
        i=j
        char=string[j]
        while char!=',' and char!=')':
            j+=1
            char=string[j]

        print("X: " + str(x))

        y=float(string[i:j]) #position y

        return(x,y)
