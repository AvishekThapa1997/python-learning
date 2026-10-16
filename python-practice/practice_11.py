class UserProfileCache(dict):
    def __missing__(self, key):
        profile = {
            "user_id":key,
            "status":"new"
        }
        self[key] = profile
        return profile

profiles = UserProfileCache()
print(profiles[101])    