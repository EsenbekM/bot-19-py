from decouple import config

passw = config("PASSWORD", cast=int)
login = config("LOGIN")

print(type(passw))
print(login)
