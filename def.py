def function():
    x = "local variable"
    print(x)

    print(x)


x = "global variable"
function()
print(x)