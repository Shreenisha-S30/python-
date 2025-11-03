try:
    numbers = [10,20,30,40,50]
    index = int(input("Enter an index (0-4):"))
    print("Value at index: ",numbers[index])
except IndexError:
    print("❌ warning! number should between 0-4")
except ValueError:
    print("❌ Value should be only numbers")
finally:
    print("program ended")