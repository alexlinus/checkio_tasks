def check_connection(network, first, second):
    connects = []
    for node in network:
        connects.append(set(node.split('-')))
    for i in range(len(connects)-1):
        for j in range(i+1, len(connects)):
            if connects[i] & connects[j]:
                print('Сейчас будет сonnects[i] - {}, а затем connects[j] - {}.'.format(connects[i], connects[j]))
                print(connects[i] & connects[j])
                connects[j] |= connects[i]
                connects[i].clear()
                break

    for connect in connects:
        if first in connect and second in connect:
            return True
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"