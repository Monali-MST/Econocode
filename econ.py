
print("If Qd = a - bp & Qs = - a + bp, \n")
print("(No need to enter sign of the values) \n\n")
aQd=int(input('Enter the a for Qd: \n'))
bQd=int(input('Enter the b for Qd: \n'))

print('\n Qd=',aQd,'-',bQd,'p')

aQs=int(input('\nEnter the a for Qs:  \n'))
bQs=int(input('Enter the b for Qs:  \n'))

print('\n Qs= -',aQs,'+',bQs,'p\n\n')

print("OUTPUTS")
print("_____________________________________________________________\n")


print("---------------------------------")
print("|    P    |    QD     |    QS    |")
print("---------------------------------")
print("|    0    |   ",aQd,"   |  -",aQs,"   |")
print("|  ",(aQd /bQd)," |     0     |  ",(aQd /bQd) *bQs - aQs," |")
print("---------------------------------")

equiPrice = (aQd + aQs) / (bQd + bQs)
print('\n\nEquilibrium Price=',equiPrice)

equiQuantity = aQd - bQd * equiPrice
print('\nEquilibrium Quantity=',equiQuantity)


ped=bQd*equiPrice/equiQuantity
pes=bQs*equiPrice/equiQuantity
print('\n\nPrice Elasticity of Demand =  -',ped)
print('\nPrice Elasticity of Supply = ', pes)


m=-abs(ped) # -abs converts positive no to negative no
if m==0:
    print("\n\nFor this product, PED is perfectly inelastic") 
if m < 1:
    print("\n\nFor this product, PED is inelastic ")
if m==1:
    print("\n\nFor this product, PED is unitary elastic")
if m > 1:
    print("\n\nFor this product, PED is elastic")
if equiQuantity == 0:
    print("\n\nFor this product, PED is perfectly elastic ")

if pes==0:
    print("\nFor this product, PES is perfectly inelastic") 
if pes < 1:
    print("\nFor this product, PES is inelastic ")
if pes==1:
    print("\nFor this product, PES is unitary elastic")
if pes > 1:
    print("\nFor this product, PES is elastic")
if equiQuantity == 0:
    print("\nFor this product, PES is perfectly elastic ")
    

print('\n\nExd=',(aQd+aQs),'-', (bQd+bQs),'p')
print('\nExs= -',(aQd+aQs),'+', (bQd+bQs),'p')


maxDemandPrice =aQd/bQd
minSupplyPrice =aQs/bQs
print('\n\nMaximum DemandPrice=',maxDemandPrice)
print('\nMinimum SupplyPrice=',minSupplyPrice)

consumeSurplus=(maxDemandPrice-equiPrice)/2*equiQuantity
print('\n\nConsumer surplus=',consumeSurplus)

producerSurplus=(equiPrice-minSupplyPrice)/2*equiQuantity
print('\nProducer surplus=',producerSurplus)

economicSurplus = consumeSurplus+producerSurplus
print('\nEconomic surplus=',economicSurplus)
