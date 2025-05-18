class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points
    def __str__(self):
        return f"{self.__class__.__name__} (examinee: {self.examinee}, points: {self.points})"

def passed(submissions: list, lowest_passing: int):
    passing_submissions = []
    for s in submissions:
        if s.points >= lowest_passing:
            passing_submissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 .append(s)
        else:
            pass
    return passing_submissions

if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)