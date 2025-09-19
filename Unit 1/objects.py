# object is a construct for storing data and functions.

class instaProfile:
     def __int__(self,username,email,profileImg,password,bio):
        self.username = username
        self.email = email
        self.profileImg = profileImg
        self.password = password
        self.bio = bio

     

              #Objects are construct for storing data and functions togther
              #when creating an object we start with the class keyword
              #This acts like our object maker/our blueprint
class CarMaker:
     def __init__(self,name,color,seating,year,model,miles):
                        self.name = name
                        self.color = color
                        self.seating = seating
                        self.year = year
                        self.model = model
                        self.miles = miles

     def printInfo(self):
                             print('heres your car FAQS')
                             print('name:'+ self.name)
                             print ('year:'+ str(self.year))
                             print ('miles:'+ str(self.miles))

     def windshieldwipers(self):
                             
      def airbag():
                                  print('when driving a certain speed and a collision happens;open')

     def turnsignals(up,down):
                                       if up:
                                            print("turn left")
                                       elif down:
                                            print("turn right")
                                       else:
                                            print("dont turn signals on")

def bluetooth(year):
                                                 if year > 2020:
                                                      print('you have bluetooth')
                                                 else:
                                                      print("no bluetooth on this model")

carOption1 =CarMaker('carolla,''black','2,''2024','corolla,''2000','year,''model','miles')      

print(carOption1)  #shows the location in computer memory

carOption1.printInfo() #shows me actual data






class Phone:
        def __int__(self,name,model,size,number):
                self.name= name
                self.model = model
                self.size =size
                self.number=number

                


                def phoneName(IPhone16,number):
                        number= 215-345-4545
                        IPhone16 = phoneName(IPhone16)
                        a = number
                        b = IPhone16
                        if number==IPhone16:
                                print ('ring ring ring')
                                



                        




