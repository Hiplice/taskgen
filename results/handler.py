from tests.models import Test, Topic
from account.models import User


class UserTests:

    def __init__(self, user, tests):
        self.name = user.first_name
        self.surname = user.last_name
        self.group = user.study_group.name if user.study_group is not None else '-'
        self.results = tests


def get_subject_results(subject, user_status):

    users = User.objects.filter(testdata__topic__subject=subject).distinct()
    result = []
    if user_status != 1:
        user = user_status
        tests = []
        topics = Topic.objects.filter(subject=subject)

        for topic in topics:
            test_data = Test.objects.filter(user=user, topic=topic)
            for i in range(0, len(test_data)):
                if test_data[i].points > 0:
                    tests.append(test_data[i].points)
                else:
                    tests.append('-')

        result.append(UserTests(user, tests))
    else:
        for user in users:
            tests = []
            topics = Topic.objects.filter(subject=subject)

            for topic in topics:
                test_data = Test.objects.filter(user=user, topic=topic)
                for i in range(0, len(test_data)):
                    if test_data[i].points > 0:
                        tests.append(test_data[i].points)
                    else:
                        tests.append('-')

            result.append(UserTests(user, tests))

    return result
