import json

from models.book import Book
from models.member import NormalMember, VipMember


class LibraryService:
    """
    图书管理系统服务类

    负责：
    1.加载图书数据
    2.加载会员数据
    3.会员登录
    4.借书
    5.还书
    6.查看借阅
    """


    def __init__(self):
        # 保存所有图书对象
        self.books = []

        # 保存所有会员对象
        self.members = []

        # 当前登录会员
        self.current_member = None


    def load_books(self, file_path: str):
        """
        从json文件加载图书数据

        json数据:
        dict

        转换:

        Book对象
        """

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


        for item in data:

            book = Book.from_dict(item)

            self.books.append(book)



    def load_members(self, file_path: str):
        """
        从json文件加载会员数据

        自动判断：
        VIP会员
        普通会员
        """


        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)



        for item in data:

            # VIP会员卡号以V开头
            if item["卡号"].startswith("V"):

                member = VipMember.from_dict(item)


            else:

                member = NormalMember.from_dict(item)


            self.members.append(member)



    def login(
        self,
        card_id: str,
        password: str
    ) -> bool:
        """
        会员登录

        根据卡号和密码验证
        """


        for member in self.members:

            if (
                member.card_id == card_id
                and
                member.password == password
            ):

                self.current_member = member

                print(
                    "登录成功:",
                    member.name
                )

                return True



        print(
            "卡号或密码错误"
        )

        return False



    def find_book(
        self,
        book_id: str
    ):
        """
        根据编号查找图书
        """


        for book in self.books:

            if book.book_id == book_id:

                return book


        return None



    def borrow_book(
        self,
        book_id: str
    ):
        """
        借书功能
        """


        # 判断是否登录

        if self.current_member is None:

            print(
                "请先登录"
            )

            return



        book = self.find_book(book_id)


        if book is None:

            print(
                "没有找到该图书"
            )

            return



        self.current_member.borrow_book(book)



    def return_book(
        self,
        book_id: str
    ):
        """
        还书功能
        """


        if self.current_member is None:

            print(
                "请先登录"
            )

            return



        book = self.find_book(book_id)


        if book is None:

            print(
                "没有找到该图书"
            )

            return



        self.current_member.return_book(book)



    def show_books(self):
        """
        查看所有图书
        """


        for book in self.books:

            book.show_info()



    def show_my_books(self):
        """
        查看我的借阅
        """


        if self.current_member is None:

            print(
                "请先登录"
            )

            return


        self.current_member.show_borrowed_books()



    def logout(self):
        """
        退出登录
        """


        self.current_member = None

        print(
            "退出成功"
        )