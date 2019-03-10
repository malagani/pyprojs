class Linked_List:

  class __Node:

    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.val=val
      self.prev=None
      self.next=None


  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
    self.__header = self.__Node(None)
    self.__trailer = self.__Node(None)
    self.__header.next = self.__trailer # trailer is after header
    self.__trailer.prev = self.__header # header is before trailer
    self.__size = 0


  def __len__(self):
    # return the number of value-containing nodes in
    # this list.
    # TODO replace pass with your implementation
    ##??????SHOULD THIS WALK THROUGH
    return self.__size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    new_node = Linked_List.__Node(val)

    self.__trailer.prev.next = new_node
    new_node.next=self.__trailer
    new_node.prev=self.__trailer.prev
    self.__trailer.prev = new_node

    self.__size = self.__size + 1

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the
    # specified index. If the index is not a valid
    # position within the list, raise an IndexError
    # exception. This method cannot be used to add an
    # item at the tail position.
    # TODO replace pass with your implementation
    if index >= self.__size:
      raise IndexError
    if index < 0:
      raise IndexError

    new_node = Linked_List.__Node(val)
    current = self.__header
    for i in range(0, index):
      current = current.next

    new_node.next = current.next
    new_node.prev = current
    current.next = new_node
    new_node.next.prev = new_node

    self.__size = self.__size + 1

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored
    # in the node at the specified index. If the index
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    if index >= self.__size:
      raise IndexError
    if index < 0:
      raise IndexError
    if self.__size == 0:
      raise IndexError

    current = self.__header
    for i in range(0, index):
      current = current.next

    valremoved=current.next.val
    current.next=current.next.next
    current.next.prev=current

    self.__size = self.__size - 1
    return valremoved

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node
    # at the specified index, but do not unlink it from
    # the list. If the specified index is invalid, raise
    # an IndexError exception.
    # TODO replace pass with your implementation
    if index >= self.__size:
      raise IndexError
    if index < 0:
      raise IndexError
    if self.__size == 0:
      raise IndexError

    current = self.__header
    for i in range(0, index):
      current = current.next

    return current.next.val #####CHECK CORRECT SYNTAX FOR THIS

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    if self.__size==0:
      raise IndexError
    self.__trailer.prev.next = self.__header.next
    self.__header.next = self.__header.next.next
    self.__header.next.prev=self.__header
    self.__trailer.prev.next.prev=self.__trailer.prev
    self.__trailer.prev.next.next=self.__trailer
    self.__trailer.prev=self.__trailer.prev.next




  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    current = self.__header.next
    stringlist = list()
    stringlist.append("[")
    if self.__size==0:
      stringlist.append(" ")
    else:
      while(current != self.__trailer):
        element = str(current.val)
        stringlist.append(" " + element)
        if current.next != self.__trailer:
          stringlist.append(",")
        else:
          stringlist.append(" ")
        current = current.next
    
    stringlist.append("]")
    stringlist = "".join(stringlist)
    return stringlist

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    self.__iter_index = 0
    self.__current = self.__header
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    if self.__iter_index == self.__size:
      raise StopIteration
    self.__current = self.__current.next
    self.__iter_index = self.__iter_index + 1
    return self.__current.val

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
  list1 = Linked_List()

  list1.append_element(5)
  list1.append_element(6)
  list1.append_element(3)
  list1.append_element(-7)

  print("Original List:")
  print(list1.__str__())
  print("Original Length:")
  print(list1.__len__())

  ##Testing Insert-SHOULD WORK
  print("Testing Insert With Valid Index")
  try:
      list1.insert_element_at(-2, 0)
  except IndexError:
      print("Invalid index!!")
  
  print("New List:")
  print(list1.__str__())
  print("New Length:")
  print(list1.__len__())

  ##Testing Insert-SHOULD GIVE ERROR
  print("Testing Insert With Invalid Index")
  try:
      list1.insert_element_at(9,7)
  except IndexError:
      print("Invalid index!!")

  print(list1.__str__())

  ##Testing Insert-SHOULD GIVE ERROR
  print("Testing Insert With Invalid Index")
  try:
      list1.insert_element_at(9,-1)
  except IndexError:
      print("Invalid index!!")

  print(list1.__str__())

  ##Testing Remove-SHOULD WORK
  print("Testing Remove With Valid Index")
  try:
      list1.remove_element_at(2)
  except:
      print("Invalid index!!")

  print("New List:")
  print(list1.__str__())
  print("New Length:")
  print(list1.__len__())

  ##Testing Remove-SHOULD GIVE ERROR
  print("Testing Remove With Invalid Index")
  try:
    list1.remove_element_at(-1)
  except:
      print("Invalid index!!")

  print(list1.__str__())

  ##Testing Remove-SHOULD GIVE ERROR
  print("Testing Remove With Invalid Index")
  try:
      list1.remove_element_at(10)
  except:
      print("Invalid index!!")

  print(list1.__str__())

  ##Testing Get element at-SHOULD WORK
  print("Testing Get Element With Valid Index")
  try:
      list1.get_element_at(1)
  except:
      print("Invalid index!!")

  print(list1.get_element_at(1))

  ##Testing Get element at-SHOULD GIVE ERROR
  print("Testing Get Element With Invalid Index")
  try:
      list1.get_element_at(-1)
  except:
      print("Invalid index!!")


  ##Testing Get element at-SHOULD GIVE ERROR
  print("Testing Get Element With Invalid Index")
  try:
      list1.get_element_at(19)
  except:
      print("Invalid index!!")

  
  print("Rotate Left Output")
  list1.rotate_left()
  print(list1.__str__())
  
  print("Size:")
  print(list1.__len__())
  
  print("Iterator:")
  for val in list1:
    print(val)

  ##empty list
  list2 = Linked_List()

  print("Original List:")
  print(list2.__str__())
  print("Original Length:")
  print(list2.__len__())
  
  ##testing insert-should give error
  print("Testing Insert With Invalid Index")
  try:
      list2.insert_element_at(9,0)
  except IndexError:
      print("Invalid index!!")

  print(list2.__str__())

  ##testing remove-SHOULD GIVE ERROR
  print("Testing Remove With Invalid Index")
  try:
    list2.remove_element_at(1)
  except:
      print("Invalid index!!")

  print(list2.__str__())

  ##Testing Get element at-SHOULD GIVE ERROR
  print("Testing Get Element With Invalid Index")
  try:
      list2.get_element_at(0)
  except:
      print("Invalid index!!")

  print(list2.__str__())

  print("Trying an incorrect use of rotate left:")
  try:
    list2.rotate_left()
  except IndexError:
    print("Rotate left doesn't work on an empty list!")

  list2.append_element(2)
  list2.append_element(6)
  list2.append_element(8)

  print("New List:")
  print(list2.__str__())
  print("New Length:")
  print(list2.__len__())

  
