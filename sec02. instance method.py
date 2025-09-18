class User:

    def __init__(self, name, email, password): #그냥 기본적인 임플란트
        self.name = name
        self.email = email
        self.password = password

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def login(self, email, password):
        if self.email == email and self.password == password:
            print('로그인 성공, 환영합니다')
            self.say_hello()
        else:
            print('로그인 실패, 없는 정보야')

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}"

user1 = User("Mike", "miky@gmail.com", "123456")

# user1.name = "Mike"
# user1.email = "miky@gmail.com"
# user1.password = "123456"

# user1.initialize("Mike", "miky@gmail.com", "123456")

print(user1) # magic string이 있으면 자동으로 user datatype을 str로 바꿔줌

user1.login("miky@gmail.com", "123456") # 첫번째 아규먼트는 빼고 넘겨주기