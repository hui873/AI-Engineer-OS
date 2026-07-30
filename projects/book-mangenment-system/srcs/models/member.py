#7.30日

class Member:
    """ 会员类 """
    def __init__(self, card_id, password,name):
        """ 初始化会员 
        params:
            card_id: 会员卡号
            password: 会员密码
            name: 会员姓名
        """
        self.card_id = card_id
        self.password = password
        self.name = name

class NormalMember(Member):
    """ 普通会员类 """
    def __init__(self, card_id, password,name):
        """ 初始化普通会员 
        params:
            card_id: 会员卡号
            password: 会员密码
            name: 会员姓名
        """
        super().__init__(card_id, password,name)
    