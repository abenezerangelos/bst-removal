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

        while self is not None:

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

        return self

    def contains(self, value):
        # Write your code here.
        print("CONTAINS", value)
        while self is not None:

            self.printer(self, [])
            if value < self.value:
                self = self.left
            elif value > self.value:

                self = self.right
            else:
                print(True)
                return True
        print(False)
        return False

    def printer(self, start, lister):
        lister.append(start.value)
        if start.left is not None:
            self.printer(start.left, lister)
        if start.right is not None:
            self.printer(start.right, lister)

        return lister

    def find_replacement(self, obj, value):
        replacement = math.inf
        store = [[], []]
        temp = [obj]
        while len(temp) != 0:
            obj = temp[0]
            temp.remove(obj)
            while obj is not None:

                if obj.right is not None and obj.left is not None:

                    if abs(obj.right.value - value) < abs(obj.left.value - value):

                        store[0].append(obj.value)
                        store[1].append(obj)
                        obj = obj.right


                    elif abs(obj.right.value - value) > abs(obj.left.value - value):

                        store[0].append(obj.value)
                        store[1].append(obj)
                        obj = obj.left

                    else:

                        temp.append(obj.left)
                        temp.append(obj.right)

                if obj.right is not None and obj.left is None:
                    store[0].append(obj.value)
                    store[1].append(obj)
                    obj = obj.right

                if obj.left is not None and obj.right is None:

                    store[0].append(obj.value)
                    store[1].append(obj)
                    obj = obj.left


                else:
                    store[0].append(obj.value)
                    store[1].append(obj)
                    obj = obj.left

        saver = [0]
        for i in range(len(store[0])):

            if store[1][i] is not store[1][0]:
                # the problem is right here
                if abs(store[0][i] - value) <= abs(replacement - value):
                    replacement = store[0][i]
                    saver[0] = i

        for i in range(len(store[1])):

            if replacement != 0:

                if store[1][i].left is store[1][saver[0]]:

                    if store[1][i].left.left is None and store[1][i].left.right is None:
                        store[1][i].left = None
                    elif store[1][i].left.left is not None and store[1][i].left.right is None:
                        store[1][i].left = store[1][i].left.left
                    elif store[1][i].left.left is None and store[1][i].left.right is not None:
                        store[1][i].left = store[1][i].left.right

                if store[1][i].right is store[1][saver[0]]:

                    if store[1][i].right.left is None and store[1][i].right.right is None:
                        store[1][i].right = None
                    elif store[1][i].right.left is not None and store[1][i].right.right is None:
                        store[1][i].right = store[1][i].right.left
                    elif store[1][i].right.left is None and store[1][i].right.right is not None:
                        store[1][i].right = store[1][i].right.right
        return replacement

    def remove(self, value):
        print("REMOVE", value)
        if self.right is None and self.left is None:
            return
        tracker = []
        while self is not None:

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

                    self.value = replacement
                    break
                else:
                    for i in tracker:

                        if i.right is not None:

                            if i.right is self:
                                i.right = None
                                return
                        if i.left is not None:

                            if i.left is self:
                                i.left = None
                                return

        return
