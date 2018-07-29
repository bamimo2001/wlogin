def about():
    '''
    输出关于这个程序的信息
    :return:
    '''
    of = open("{}/bin/about.dat".format(path))
    rf = of.read()
    try:
        info = eval(rf)
        os.system("clear")
        print("================About osnssh================")
        for k,v in info.items():
            print("{}: {}".format(k, v))
    except:
        print("For failure.")
    return