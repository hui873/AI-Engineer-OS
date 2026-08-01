class Book:
    """
    图书类

    用于保存一本图书的信息

    属性：
        book_id : 图书编号
        title   : 图书名称
        author  : 作者
        stock   : 库存数量
    """


    def __init__(
        self,
        book_id: str,
        title: str,
        author: str,
        stock: int
    ):
        """
        初始化图书对象
        """
        if not self.check_stock(stock):
            raise ValueError("图书库存不能小于 0")
        # 图书编号
        self.book_id = book_id
        # 图书标题
        self.title = title
        # 作者
        self.author = author
        # 图书库存
        self.stock = stock



    def borrow(self) -> bool:
        """
        借书

        库存大于0才能借

        返回：
            True  借书成功
            False 库存不足
        """
        if self.stock > 0:
            self.stock -= 1
            return True
        return False



    def return_book(self):
        """
        还书
        库存增加1
        """
        self.stock += 1


    def show_info(self):
        """
        展示图书信息
        """
        print(
            f"""
编号: {self.book_id}
书名: {self.title}
作者: {self.author}
库存: {self.stock}
"""
        )

    @classmethod
    def from_dict(
        cls,
        data: dict
    ):
        """
        类方法

        作用：
        将json里面的一条数据
        转换成Book对象
        例如：
        json:
        {
            "编号":"AI001",
            "标题":"LangChain入门与实践",
            "作者":"李智慧",
            "数量":8
        }
        转换:
        Book对象
        """
        return cls(
            data["编号"],
            data["标题"],
            data["作者"],
            data["数量"]
        )
    
    @staticmethod
    def check_stock(stock: int) -> bool:
        """
        静态方法

        判断库存是否合法
        """


        return stock >= 0