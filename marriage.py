class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg

class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg

class JobSecureException(Exception):
    def __init__(self, arg):
        self.msg = arg

class IslamicReligionException(Exception):
    def __init__(self, arg):
        self.msg = arg

class PhysicalDesirabilityException(Exception):
    def __init__(self, arg):
        self.msg = arg

try:
    age = int(input("Enter Age:"))
    if age > 40:
        raise TooOldException("With your age you need special attention...consult the counselling unit, dial +2348072889844 for more guidance")
    elif age < 18:
        raise TooYoungException("Please wait for a few more years, concentrate on your studies, get a suitable and a secure a job before setting up for marriage, Dial this Whatapp +2348072889844 for more counselling")
    else:
        job_secure = input("Is your job secure? (yes or no): ").lower()
        if job_secure != 'yes':
            raise JobSecureException("Your job is not secure, and that may affect your marriage prospects. Try to secure a job and intensify your Prayer, HASBUNALLAHU WANE'EMAL WAKIL")
        
        religion = input("What is your religion? ").strip()
        if religion.lower() != 'islam':
            raise IslamicReligionException("We are sorry, but our services are only available for those of the Islamic faith.")
        
        physical_desirability = input("Are you physically desirable? (yes or no): ").lower()
        if physical_desirability != 'no':
            raise PhysicalDesirabilityException("Physical desirability is an important factor in finding a match. Take steps to improve your physical well-being, Dial +2348072889844 for more on health counselling")
        else:
            print("You will get match details soon by email, Contact this number +2348072889844 on WhatsApp for more guidance")

except TooYoungException as e:
    print(e.msg)

except TooOldException as e:
    print(e.msg)

except JobSecureException as e:
    print(e.msg)

except IslamicReligionException as e:
    print(e.msg)

except PhysicalDesirabilityException as e:
    print(e.msg)  

