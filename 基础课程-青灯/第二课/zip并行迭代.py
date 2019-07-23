names=('熊珍龙','周莉','向天秀')
ages=(18,19,20)
jobs=('老师','公务员','农民')
for name,age,job in zip(names,ages,jobs):
    print('{}---{}---{}'.format(name,age,job))