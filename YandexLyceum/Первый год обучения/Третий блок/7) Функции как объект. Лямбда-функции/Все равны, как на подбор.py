def same_by(characteristic, objects):
    if not objects:
        return True
    example = characteristic(objects[0])
    for i in range(1, len(objects)):
        if example != characteristic(objects[i]):
            return False
    return True
