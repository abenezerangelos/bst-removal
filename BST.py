# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
import math


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        print("INSERT", value)
        # Write your code here.
        # Do not edit the return statement of this method.
        print(self.value, "beginning")
        while self is not None:
            print(self.value, "amidst")
            if value < self.value:
                if self.left is None:
                    self.left = BST(value)
                    break
                else:
                    self = self.left
            elif value >= self.value:
                if self.right is None:
                    self.right = BST(value)

                    break
                else:
                    self = self.right

        print(self.value, 'end')

        return self

    def contains(self, value):
        # Write your code here.
        print("CONTAINS", value)
        while self is not None:
            print(f"this {self.value}, {value}")

            self.printer(self, [])
            if value < self.value:
                self = self.left
            elif value > self.value:
                print("Raise flag")

                print("Executed")
                self = self.right
            else:
                print(True)
                return True
        print(False)
        return False

    # because this is already the answer to an even harder question
    # def turn_to_list_object(self, start, lister):

    #     lister.append(start)
    #     if start.left is not None:
    #         self.turn_to_list_object(start.left,lister)
    #     if start.right is not None:
    #         self.turn_to_list_object(start.right,lister)
    #     print([i.value for i in lister])
    #     return lister
    def printer(self, start, lister):
        lister.append(start.value)
        if start.left is not None:
            self.printer(start.left, lister)
        if start.right is not None:
            self.printer(start.right, lister)
        print(lister)
        return lister

    def find_replacement(self, obj, value):
        replacement = 0
        store = [[], []]
        temp = [obj]
        while len(temp) != 0:
            obj = temp[0]
            temp.remove(obj)
            while obj is not None:
                print("FOCUS", obj.value)
                if obj.right is not None and obj.left is not None:
                    print("Object has both")
                    if abs(obj.right.value - value) < abs(obj.left.value - value):
                        print("!!!!!!!!", obj.value, obj.right.value, obj.left.value)
                        store[0].append(obj.value)
                        store[1].append(obj)
                        obj = obj.right


                    elif abs(obj.right.value - value) > abs(obj.left.value - value):
                        print("@@@@@@@@@@@", obj.value, obj.left.value, obj.right.value)
                        store[0].append(obj.value)
                        store[1].append(obj)
                        obj = obj.left

                    else:
                        print("############")
                        print("Object is confused")
                        temp.append(obj.left)
                        temp.append(obj.right)

                if obj.right is not None and obj.left is None:
                    print("Object has left but not right")
                    store[0].append(obj.value)
                    store[1].append(obj)
                    obj = obj.right

                if obj.left is not None and obj.right is None:
                    print("Object has right but not left!")
                    store[0].append(obj.value)
                    store[1].append(obj)
                    obj = obj.left


                else:
                    store[0].append(obj.value)
                    store[1].append(obj)
                    obj = obj.left
                print(store)

        saver = [0]
        for i in range(len(store[0])):
            print(f"OTHER DEBUG{i}", store[1][i])
            print(store[1][i] is not store[1][0])
            if store[1][i] is not store[1][0]:
                if abs(store[0][i] - value) <= abs(replacement - value):
                    print("BIG DEBUG", store[0][i], store[1][i], store[1][i].value, store[1][0], store[1][0].value,
                          replacement)
                    replacement = store[0][i]
                    saver[0] = i

            print("This shit right here:", replacement)
        print("Replacement", replacement)
        if replacement == 0:
            replacement = value
        for i in range(len(store[1])):

            if replacement != 0:
                print("Crucial2", saver[-1], store[0][saver[-1]], store[1][saver[-1]])
                if store[1][i].left is store[1][saver[0]]:
                    print("Crucial3")
                    if store[1][i].left.left is None and store[1][i].left.right is None:
                        store[1][i].left = None
                    elif store[1][i].left.left is not None and store[1][i].left.right is None:
                        store[1][i].left = store[1][i].left.left
                    elif store[1][i].left.left is None and store[1][i].left.right is not None:
                        store[1][i].left = store[1][i].left.right
                    else:
                        print("REally scary situation")
                        replacer = self.find_replacement(store[1][saver[0]], store[0][saver[0]])

                if store[1][i].right is store[1][saver[0]]:
                    print("Crucial4")
                    if store[1][i].right.left is None and store[1][i].right.right is None:
                        store[1][i].right = None
                    elif store[1][i].right.left is not None and store[1][i].right.right is None:
                        store[1][i].right = store[1][i].right.left
                    elif store[1][i].right.left is None and store[1][i].right.right is not None:
                        store[1][i].right = store[1][i].right.right
                    else:
                        print("REally scary situation")
                        replacer = self.find_replacement(store[1][saver[0]], store[0][saver[0]])

        # in here we will set the replacement from the parent node to Null
        return replacement

    def remove(self, value):
        print("REMOVE", value)
        # Write your code here.
        # Do not edit the return statement of this method.
        # mem=self.turn_to_list_object(self,[])
        # if self.right is not None:
        #     if value is self.right.value:
        #         if self.right.right is not None:
        #             self.right=self.right.right
        #         else:
        #             self.right=None
        # if self.left is not None:
        #     if value is self.left.value:
        #         if self.left.left is not None:
        #             self.left=self.left.left
        #         self.left=None
        if self.right is None and self.left is None:
            print("returned Nothing")
            return
        tracker = []
        while self is not None:
            print("Line 177:", self.printer(self, []))
            if value > self.value:
                tracker.append(self)
                self = self.right

            elif value < self.value:
                tracker.append(self)
                self = self.left

            elif value is self.value:
                tracker.append(self)
                if self.right is not None or self.left is not None:
                    replacement = self.find_replacement(self, value)
                    print("Repetition", self.value, replacement)
                    self.value = replacement
                    break
                else:
                    for i in tracker:
                        print("BBD", i.right, self, i.left, [i.value for i in tracker], tracker)
                        print("right under", i.value, self.value)
                        if i.right is not None:
                            print(i.right is self, i.right, self)
                            if i.right is self:
                                print("Something please")
                                i.right = None
                                return
                        if i.left is not None:
                            print(i.left is self, i.left, self)
                            if i.left is self:
                                print("Anything")
                                i.left = None
                                return

        return


# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
import math


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        print("INSERT", value)
        # Write your code here.
        # Do not edit the return statement of this method.
        print(self.value, "beginning")
        while self is not None:
            print(self.value, "amidst")
            if value < self.value:
                if self.left is None:
                    self.left = BST(value)
                    break
                else:
                    self = self.left
            elif value >= self.value:
                if self.right is None:
                    self.right = BST(value)

                    break
                else:
                    self = self.right

        print(self.value, 'end')

        return self

    def contains(self, value):
        # Write your code here.
        print("CONTAINS", value)
        while self is not None:
            print(f"this {self.value}, {value}")

            self.printer(self, [])
            if value < self.value:
                self = self.left
            elif value > self.value:
                print("Raise flag")

                print("Executed")
                self = self.right
            else:
                print(True)
                return True
        print(False)
        return False

    # because this is already the answer to an even harder question
    # def turn_to_list_object(self, start, lister):

    #     lister.append(start)
    #     if start.left is not None:
    #         self.turn_to_list_object(start.left,lister)
    #     if start.right is not None:
    #         self.turn_to_list_object(start.right,lister)
    #     print([i.value for i in lister])
    #     return lister
    def printer(self, start, lister):
        lister.append(start.value)
        if start.left is not None:
            self.printer(start.left, lister)
        if start.right is not None:
            self.printer(start.right, lister)
        print(lister)
        return lister

    def find_replacement(self, obj, value):
        replacement = 0
        store = [[], []]
        temp = [obj]
        while len(temp) != 0:
            obj = temp[0]
            temp.remove(obj)
            while obj is not None:
                print("FOCUS", obj.value)
                if obj.right is not None and obj.left is not None:
                    print("Object has both")
                    if abs(obj.right.value - value) < abs(obj.left.value - value):
                        print("!!!!!!!!", obj.value, obj.right.value, obj.left.value)
                        store[0].append(obj.value)
                        store[1].append(obj)
                        obj = obj.right


                    elif abs(obj.right.value - value) > abs(obj.left.value - value):
                        print("@@@@@@@@@@@", obj.value, obj.left.value, obj.right.value)
                        store[0].append(obj.value)
                        store[1].append(obj)
                        obj = obj.left

                    else:
                        print("############")
                        print("Object is confused")
                        temp.append(obj.left)
                        temp.append(obj.right)

                if obj.right is not None and obj.left is None:
                    print("Object has left but not right")
                    store[0].append(obj.value)
                    store[1].append(obj)
                    obj = obj.right

                if obj.left is not None and obj.right is None:
                    print("Object has right but not left!")
                    store[0].append(obj.value)
                    store[1].append(obj)
                    obj = obj.left


                else:
                    store[0].append(obj.value)
                    store[1].append(obj)
                    obj = obj.left
                print(store)

        saver = [0]
        for i in range(len(store[0])):
            print(f"OTHER DEBUG{i}", store[1][i])
            print(store[1][i] is not store[1][0])
            if store[1][i] is not store[1][0]:
                if abs(store[0][i] - value) <= abs(replacement - value):
                    print("BIG DEBUG", store[0][i], store[1][i], store[1][i].value, store[1][0], store[1][0].value,
                          replacement)
                    replacement = store[0][i]
                    saver[0] = i

            print("This shit right here:", replacement)
        print("Replacement", replacement)
        if replacement == 0:
            replacement = value
        for i in range(len(store[1])):

            if replacement != 0:
                print("Crucial2", saver[-1], store[0][saver[-1]], store[1][saver[-1]])
                if store[1][i].left is store[1][saver[0]]:
                    print("Crucial3")
                    if store[1][i].left.left is None and store[1][i].left.right is None:
                        store[1][i].left = None
                    elif store[1][i].left.left is not None and store[1][i].left.right is None:
                        store[1][i].left = store[1][i].left.left
                    elif store[1][i].left.left is None and store[1][i].left.right is not None:
                        store[1][i].left = store[1][i].left.right
                    else:
                        print("REally scary situation")
                        replacer = self.find_replacement(store[1][saver[0]], store[0][saver[0]])

                if store[1][i].right is store[1][saver[0]]:
                    print("Crucial4")
                    if store[1][i].right.left is None and store[1][i].right.right is None:
                        store[1][i].right = None
                    elif store[1][i].right.left is not None and store[1][i].right.right is None:
                        store[1][i].right = store[1][i].right.left
                    elif store[1][i].right.left is None and store[1][i].right.right is not None:
                        store[1][i].right = store[1][i].right.right
                    else:
                        print("REally scary situation")
                        replacer = self.find_replacement(store[1][saver[0]], store[0][saver[0]])

        # in here we will set the replacement from the parent node to Null
        return replacement

    def remove(self, value):
        print("REMOVE", value)
        # Write your code here.
        # Do not edit the return statement of this method.
        # mem=self.turn_to_list_object(self,[])
        # if self.right is not None:
        #     if value is self.right.value:
        #         if self.right.right is not None:
        #             self.right=self.right.right
        #         else:
        #             self.right=None
        # if self.left is not None:
        #     if value is self.left.value:
        #         if self.left.left is not None:
        #             self.left=self.left.left
        #         self.left=None
        if self.right is None and self.left is None:
            print("returned Nothing")
            return
        tracker = []
        while self is not None:
            print("Line 177:", self.printer(self, []))
            if value > self.value:
                tracker.append(self)
                self = self.right

            elif value < self.value:
                tracker.append(self)
                self = self.left

            elif value is self.value:
                tracker.append(self)
                if self.right is not None or self.left is not None:
                    replacement = self.find_replacement(self, value)
                    print("Repetition", self.value, replacement)
                    self.value = replacement
                    break
                else:
                    for i in tracker:
                        print("BBD", i.right, self, i.left, [i.value for i in tracker], tracker)
                        print("right under", i.value, self.value)
                        if i.right is not None:
                            print(i.right is self, i.right, self)
                            if i.right is self:
                                print("Something please")
                                i.right = None
                                return
                        if i.left is not None:
                            print(i.left is self, i.left, self)
                            if i.left is self:
                                print("Anything")
                                i.left = None
                                return

        return
