from tests.models import TestData, Topic
from account.models import User


class UserTests:

    def __init__(self, user, tests):
        self.name = user.first_name
        self.surname = user.last_name
        self.group = user.study_group.name if user.study_group is not None else '-'
        self.results = tests


def get_subject_results(subject):
    users = User.objects.filter(testdata__topic__subject=subject).distinct()
    result = []

    for user in users:
        tests = []
        topics = Topic.objects.filter(subject=subject)

        for topic in topics:
            test_data = TestData.objects.filter(user=user, topic=topic)
            if len(test_data) > 0:
                tests.append(test_data[0].best_result)
            else:
                tests.append('-')

        result.append(UserTests(user, tests))

    return result
