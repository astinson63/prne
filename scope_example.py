myvar = 'Global Scope'


def scope_test(myvar='function Scope'):
    return myvar


print(f'Global: {myvar}')
print(f'Function_Scope: {scope_test()}')

myvar = scope_test("Assigned new value")
print(f'myvar = scope_test: {myvar}')

