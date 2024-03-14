from string import Template

x = Template('The model of $device is $model with os $os')


x.substitute(device='router1', model='3800', os='IOS-XE')

