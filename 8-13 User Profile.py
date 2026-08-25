def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile = build_profile('Christopher', 'White',
                        Game='Madden',
                        QB='Patrick Mahomes',)
            

print(profile)
