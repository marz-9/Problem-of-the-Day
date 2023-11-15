list1=[7,8,3,1,6,22,10,25,9,15,1]
list2=[2,11,0,6,3,20,7,25,6,7]

sum1_l1=sum(list1[:5])
sum2_l1=sum(list1[5:8])
sum3_l1=sum(list1[8:])

sum4_l2=sum(list2[:4])
sum5_l2=sum(list2[4:8])
sum6_l2=sum(list2[8:])

if (sum1_l1 < sum4_l2 and sum2_l1 < sum5_l2 and sum3_l1 < sum6_l2):
    total=sum1_l1+sum2_l1+sum3_l1
    print("Shortest path is: ", list1)
    print("Sum= "+str(total))
elif  (sum4_l2 < sum3_l1 and sum5_l2 < sum2_l1 and sum6_l2 < sum3_l1):
    total=sum4_l2+sum5_l2+sum6_l2
    print("Shortest path is: ", list2)
    print("Sum= "+str(total))