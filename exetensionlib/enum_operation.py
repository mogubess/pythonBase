import enum

db = {
    'stack1':1,
    'stack2':2,
}

@enum.unique #enumの重複を許可しない
#class Status(enum.Enum):    #int値がとれない
class Status(enum.IntEnum):  #int値がとれす
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3

print(Status.ACTIVE)
print(type(Status.ACTIVE))
print(Status.ACTIVE == Status(1))

