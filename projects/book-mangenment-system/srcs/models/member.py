class Member:
    """
    会员基类

    保存所有会员共有的信息
    """

    def __init__(
        self,
        card_id: str,
        name: str,
        password: str
    ):
        # 会员卡号
        self.card_id = card_id

        # 会员姓名
        self.name = name

        # 登录密码
        self.password = password

        # 当前借阅图书列表
        self.borrowed_books = []


    def get_borrow_limit(self) -> int:
        """
        获取最大借书数量

        基类默认没有具体规则
        子类需要重写
        """

        return 0


    def can_borrow(self) -> bool:
        """
        判断是否还能继续借书
        """

        return len(self.borrowed_books) < self.get_borrow_limit()


    def borrow_book(self, book) -> bool:
        """
        借阅图书

        参数:
            book: Book对象

        返回:
            True  成功
            False 失败
        """

        # 判断借书数量是否达到限制
        if not self.can_borrow():
            print("已经达到最大借书数量")
            return False


        # 调用Book对象的借书方法
        if book.borrow():

            # 加入自己的借阅列表
            self.borrowed_books.append(book)

            print(
                self.name,
                "借阅",
                book.title,
                "成功"
            )

            return True


        print("图书库存不足")
        return False


    def return_book(self, book) -> bool:
        """
        归还图书
        """

        # 判断是否借阅过该书
        if book in self.borrowed_books:

            # 从借阅列表删除
            self.borrowed_books.remove(book)

            # 增加库存
            book.return_book()

            print(
                self.name,
                "归还",
                book.title,
                "成功"
            )

            return True


        print("未借阅该图书")
        return False


    def show_borrowed_books(self):
        """
        查看当前借阅图书
        """

        if len(self.borrowed_books) == 0:
            print("当前没有借阅图书")
            return


        print(
            self.name,
            "当前借阅:"
        )

        for book in self.borrowed_books:
            print(
                book.title
            )


    @classmethod
    def from_dict(cls, data: dict):
        """
        根据json数据创建会员对象

        由子类重写
        """

        return cls(
            data["卡号"],
            data["姓名"],
            data["密码"]
        )



class NormalMember(Member):
    """
    普通会员类

    最大借书数量:
    3本
    """


    def get_borrow_limit(self) -> int:
        """
        普通会员借书权限
        """

        return 3



class VipMember(Member):
    """
    VIP会员类

    最大借书数量:
    6 + VIP等级
    """


    def __init__(
        self,
        card_id: str,
        name: str,
        password: str,
        vip_level: int
    ):

        # 调用父类初始化
        super().__init__(
            card_id,
            name,
            password
        )

        # VIP等级
        self.vip_level = vip_level



    def get_borrow_limit(self) -> int:
        """
        VIP借书权限
        """

        return 6 + self.vip_level



    @classmethod
    def from_dict(cls, data: dict):
        """
        从json创建VIP对象
        """

        return cls(
            data["卡号"],
            data["姓名"],
            data["密码"],
            data["会员等级"]
        )