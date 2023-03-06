
def check_ip(ip_num):
    checkResult = False

    try:
        ip_num = int(ip_num)

        if 0 <= ip_num < 256:
            checkResult = True

        return checkResult

    # When param 'ip_num' is not of type 'int' an error will be thrown
    # With the 'try-except' this will be prevented
    except ValueError:
        return False


def check_prefix(pre_num):
    checkResult = False

    try:
        pre_num = int(pre_num)

        if 1 <= pre_num <= 31:
            checkResult = True

        return checkResult

    except ValueError:
        return checkResult


def calculate_binary(ip_elements):
    for ip_element in ip_elements:
        modulo = 0,


ip_elements = []
ip_in_binary = []

while True:
    counter = 1

    while len(ip_elements) < 4:
        ip_number = input()

        if check_ip(ip_number):
            ip_elements.append(ip_number)
            print('Element ' + str(counter) + ' eingefügt')
            counter += 1
        else:
            print('Die Eingabe war falsch. Bitte wiederholen:')

    resultString = None

    for index, value in enumerate(ip_elements):
        if resultString is None:
            resultString = value + '.'
            continue

        if index != 3:
            resultString += value + '.'
        else:
            resultString += value

    print(resultString)
    break

print('Wie lautet der Präfix?')

checkedPrefix = None

while True:
    prefix_number = input()

    if check_prefix(prefix_number):
        checkedPrefix = int(prefix_number)
        break
    else:
        print('Der Prefix ist Falsch. Wiederhole die Eingabe!')

print('Der Prefix lautet ' + str(checkedPrefix))
