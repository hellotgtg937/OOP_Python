class User:
    
    def say_hello(some_user):
        print(f"안녕하세요! 저는 {some_user.name}입니다!")

user1 = User()
user2 = User()

print(type(user1))
print(type(user2))

user1.name = "mike"
user1.email = 'zzzhi7@naver.com'
user1.password = '12345'

user2.name = "kyle"
user2.email = 'ehehei@naver.com'
user2.password = '12345'

print(user1.email)

User.say_hello(user1)
User.say_hello(user2) # 클래스 안에 메서드
user1.say_hello() # 인스턴스로 메서드 호출 가능

# user1.say_hello(user1) == User.say_hello(user1, user1)