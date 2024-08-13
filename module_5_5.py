from time import sleep
class User:
    def __init__(self,nickname:str,password:str,age:int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
class Video:
    def __init__(self, title:str,duration:int,adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

class Urtube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def register(self,nickname:str,password:str,age:int):
        nick_users = []
        for us in self.users:
            nick_users.append(us.nickname)
        if nickname in nick_users:
            print(f'Пользователь уже существует!')
        else:
            new_user = User(nickname,password,age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f'Пользователь {nickname} зарегистрирован!')

    def log_out(self):
        self.current_user = None

    def log_in(self, login:str,password:str):
        for user in self.users:
            if user.nickname == login and hash(password) == user.password:
                self.current_user = user
                print('вы вошли в систему')

    def add(self,*args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)


    def get_videos(self ,search_word):
        search_word = search_word.lower()
        title_list = []
        for video in self.videos:
            if search_word in video.title.lower():
                title_list.append(video.title)
        return title_list

    def watch_video(self, movie: str):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
        else:
            for video in self.videos:
                if movie in video.title:
                    if video.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                        break
                    else:
                        for i in range(1, video.duration):
                            print(i, end='.')
                            sleep(1)
                        print('Конец видео')
                        video.time_now = 0
                        break
            else:
                print('Такого видео не существует')


ur = Urtube()
v1 = Video('Лучший язык программирования 2024 года', 20)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin','lolkekcheburek',13)
print()
ur.log_in('vasya_pupkin','lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist','iScX4vIJClb9YQavjAgF',25)
print()
ur.watch_video('Для чего девушкам парень программист?')
ur.watch_video('Лучший язык программирования 2024 года')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)
print()
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')