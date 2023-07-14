try:
    if True:
        raise("someError")
    else:
        print("aa")

except "someError":
    print("meow")