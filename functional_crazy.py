
def get_crazy_functionals():
    from crazy_functions.读文章写摘要 import 读文章写摘要
    from crazy_functions.生成函数注释 import 批量生成函数注释
    from crazy_functions.解析项目源代码 import 解析项目本身
    from crazy_functions.解析项目源代码 import 解析一个Python项目
    from crazy_functions.解析项目源代码 import 解析一个C项目的头文件
    from crazy_functions.高级功能函数模板 import 高阶功能模板函数

    return {
        "[实验] 请解析并解构此项目本身": {
            "Function": 解析项目本身
        },
        "[实验] 解析整个py项目（input输入项目根路径）": {
            "Color": "stop",    # 按钮颜色
            "Function": 解析一个Python项目
        },
        "[实验] 解析整个C++项目（input输入项目根路径）": {
            "Color": "stop",    # 按钮颜色
            "Function": 解析一个C项目的头文件
        },
        "[实验] 读tex论文写摘要（input输入项目根路径）": {
            "Color": "stop",    # 按钮颜色
            "Function": 读文章写摘要
        },
        "[实验] 批量生成函数注释（input输入项目根路径）": {
            "Color": "stop",    # 按钮颜色
            "Function": 批量生成函数注释
        },
        "[实验] 实验功能函数模板": {
            "Color": "stop",    # 按钮颜色
            "Function": 高阶功能模板函数
        },
    }


