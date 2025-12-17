print("project-xyz-instance")  # case1

ec2_instance_name = "project-xyz-instance"

print(ec2_instance_name)  # case2



a=10 # global variables
b=5

def addition():
    c = 10 # local variables
    print(a+b+c)

    def sub():
        print(a-b)

        addition()
        sub()