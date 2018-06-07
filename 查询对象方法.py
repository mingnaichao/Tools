def info(object, spacing=10, collapse=1):
    '''
    Print methods and doc strings. Take module,class,dictionary,or string.
    '''
    # 遍历一遍object对象，把里面的可以被调用的方法提取出来
    methodList = [method for method in dir(
        object) if callable(getattr(object, method))]
    # 把要提取出来的方法以更好看的字符串呈现出来，多行变单行
    # collapse可以控制打印的信息是否换行
    # collapse=1,并行
    # collapse=0,换行
    processFunc = collapse and (lambda s: ''.join(s.split())) or (lambda s: s)
    # 让左侧打印的是方法名，右侧打印的是方法的doc名称
    print('\n'.join(
        ['%s %s' % (str(method.ljust(spacing)), processFunc(str(getattr(object, method).__doc__))) for method in
         methodList]))


a = 'requests'
info(a)
