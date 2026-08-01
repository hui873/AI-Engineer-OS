from services.library_service import LibraryService


def show_menu():
    """
    显示系统菜单
    """

    print("""
========================
      AI图书管理系统
========================

1. 查看所有图书
2. 借阅图书
3. 归还图书
4. 查看我的借阅
5. 退出系统

========================
""")


def main():
    """
    程序入口
    """

    # 创建图书管理服务对象
    service = LibraryService()

    # 加载图书数据
    # service.load_books(
    #     "../data/book.json"
    # )

    # # 加载会员数据
    # service.load_members(
    #     "../data/members.json"
    # )
    service.load_books(
    "data/book.json"
    )

    service.load_members(
    "data/members.json"
    )


    # 登录

    print("======会员登录======")

    card_id = input(
        "请输入卡号:"
    )

    password = input(
        "请输入密码:"
    )


    # 登录失败直接退出

    if not service.login(
        card_id,
        password
    ):
        return



    # 登录成功后的菜单循环

    while True:

        show_menu()

        choice = input(
            "请选择功能:"
        )


        if choice == "1":

            # 查看所有图书

            service.show_books()


        elif choice == "2":

            # 借书

            book_id = input(
                "请输入图书编号:"
            )

            service.borrow_book(
                book_id
            )


        elif choice == "3":

            # 还书

            book_id = input(
                "请输入归还图书编号:"
            )

            service.return_book(
                book_id
            )


        elif choice == "4":

            # 查看自己的借阅

            service.show_my_books()


        elif choice == "5":

            # 退出

            service.logout()

            break


        else:

            print(
                "输入错误，请重新选择"
            )


if __name__ == "__main__":
    main()