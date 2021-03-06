"""

This program is part of an exercise in
Think Python: An Introduction to Software Design
Allen B. Downey

WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!

"""

class Kangaroo(object):u
    """a Kangaroo is a marsupial"""
    
    def __init__(self, contents=None):
        #将[]改为None
        if contents == None:
            contents=[]
        self.pouch_contents = contents

    def __str__(self):
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + str(obj)
            #将object.__str__(obj)改为str(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)

# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.
