from Linked_List import Linked_List


def Josephus(ll):
  while (len(ll)>1):
      ll.rotate_left()
      ll.remove_element_at(0)
      print(ll.__str__())
  print("The survivor is:"+str(ll.get_element_at(0)))
  


if __name__ == '__main__':
  n = int(input("Input the total number of people: "))
  ll=Linked_List()
  for i in range(1,n+1):
      ll.append_element(i)
  # create a new doubly linked list object called ll
  # with n elements named 1 to n.
  # TODO insert your implementation before the print statement  
  print("Initial order:", ll)
  Josephus(ll)
