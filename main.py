
from LinkedList import LinkedList

# At this point the list is empty
listOfNumbers = LinkedList()

# # Adding the first node to the list
listOfNumbers.insertLast( 10 )
listOfNumbers.insertLast( 30 )
listOfNumbers.insertLast( 50 )
listOfNumbers.insertLast( 80 )
listOfNumbers.insertLast( 100 )
listOfNumbers.insertLast( 200 )

# listOfNumbers.printList()
# =================================================
found = listOfNumbers.findNode(50)
print(found)
print(found.val)
# ===================================================
listOfNumbers.deleteNode(100)
listOfNumbers.printList()
