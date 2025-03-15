from abc import ABCMeta, abstractmethod
from user.domain.user import User

#객체지향 인터페이스로 선언하기 위해 ABCMeta 클래스를 이용한다
class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User):
        raise NotImplemented
    
    @abstractmethod
    def find_by_email(self, email:str) -> User:
        """
        이메일로 유저 검색
        없을 경우 422 에러 발생
        """

        raise NotImplementedError