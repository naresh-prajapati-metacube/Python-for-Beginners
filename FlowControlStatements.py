marksInMaths = int(input('Please Enter Maths Marks: '))
marksInPhysics = int(input('Please Enter Physics Marks: '))
marksInChemistry = int(input('Please Enter Chemistry Marks: '))

if (marksInMaths < 35 or marksInMaths < 35 or marksInMaths < 35):
    print('Failed')
else:
    averageMarks = (marksInMaths + marksInPhysics + marksInChemistry) / 3
    if(averageMarks <= 59):
        print('C grade')
    elif(averageMarks <= 69):
        print('B grade')
    else:
        print('A grade')