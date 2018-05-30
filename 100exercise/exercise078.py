if __name__ == '__main__':
    person = {'l':20,'w':30,'f':45}
    m = ''
    age = 0
    for key in person.keys():
        if(person.get(key)>age):
            m = key
            age = person.get(key)

    print(m + " : "+ str(age))


