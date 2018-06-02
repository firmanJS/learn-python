from passlib.hash import django_pbkdf2_sha256
hashs = 'pbkdf2_sha256$20000$3RFHVUvhZbu5$llCkkBhVqeh69KSETtH8gK5iTQVy2guwSSyTeGyguxE='
user_input = 'password'
# print (django_pbkdf2_sha256.verify(user_input, hashs))

hash = 'pbkdf2_sha256$20000$3RFHVUvhZbu5$llCkkBhVqeh69KSETtH8gK5iTQVy2guwSSyTeGyguxE='
user_inputs = 'password'
print(django_pbkdf2_sha256.verify(user_inputs, hash))
