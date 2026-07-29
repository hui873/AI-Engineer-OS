"""教务管理系统的控制台主菜单。"""

from main import StudentManager


def show_menu():
    """显示系统功能菜单。"""
    print( "=" * 36)
    print("         教务管理系统")
    print("=" * 36)
    print("1. 添加学生成绩")
    print("2. 修改学生成绩")
    print("3. 删除学生成绩")
    print("4. 查询指定学生成绩")
    print("5. 展示全部学生成绩")
    print("0. 退出系统")
    print("=" * 36)


def run_system():
    """启动并持续运行教务管理系统。"""
    manager = StudentManager()

    while True:
        show_menu()

        try:
            choice = input("请输入功能编号：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n系统已退出，再见！")
            break

        try:
            if choice == "1":
                manager.add_student()
            elif choice == "2":
                manager.update_score()
            elif choice == "3":
                manager.delete_score()
            elif choice == "4":
                manager.query_score()
            elif choice == "5":
                if manager.students:
                    manager.display_all_scores()
                else:
                    print("当前还没有学生成绩信息！")
            elif choice == "0":
                print("系统已退出，再见！")
                break
            else:
                print("功能编号无效，请输入 0～5。")
        except ValueError:
            print("成绩输入有误，请输入 0～100 之间的整数！")
        except (EOFError, KeyboardInterrupt):
            print("\n本次操作已取消。")


if __name__ == "__main__":
    run_system()
