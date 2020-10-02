def eatString(givenString):
     string = givenString
     print(string)

     while(len(string) > 0):
         string = string[0:len(string)-1]

         print(string)

eatString('Hoii hoe gaat het ermee')