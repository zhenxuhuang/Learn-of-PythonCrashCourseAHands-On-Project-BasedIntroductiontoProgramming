"""
Python编程：从入门到实践
第8章 函数

8.2
"""


def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# 位置实参
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 设置默认值(注意先列出没有默认值的形参)
def describe_pet_new(pet_name, animal_type='dog'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet_new(pet_name='willie')
describe_pet_new('willie')
