class Task:
    def __init__(self, name, completed, max_score):
        self.name = name
        self.completed = completed
        self.max_score = max_score


class AllOrNothing(Task):
    def __init__(self, name, completed, max_score):
        super().__init__(name, completed, max_score)


class FasterIsBetter(Task):
    def __init__(self, name, completed, max_score, time_to_solve, score_for_task, percent, time_of_participant):
        super().__init__(name, completed, max_score)
        self.time_to_solve = time_to_solve
        self.score_for_task = score_for_task
        self.percent = percent
        self.time_of_participant = time_of_participant


class Participant:
    def __init__(self, name, tasks, total):
        self.name = name
        self.tasks = tasks
        self.total = total

    def total_score(self):
        for i in self.tasks:
            if i.completed and isinstance(i, AllOrNothing):
                self.total += i.max_score
            if i.completed and isinstance(i, FasterIsBetter):
                self.total += i.score_for_task


def check_time_of_all(participants):
    all_time = []
    for i in participants:
        for j in i.tasks:
            if isinstance(j, FasterIsBetter) and j.completed:
                all_time.append(j.time_of_participant)
    return min(all_time)


def set_score_FasterIsBetter(participants):
    min_ = check_time_of_all(participants)
    for p in participants:
        for t in p.tasks:
            if isinstance(t, FasterIsBetter):
                if t.completed and t.time_of_participant <= t.time_to_solve:
                    if t.time_of_participant == min_:
                        t.score_for_task = t.max_score
                        # print(t.time_of_participant)
                    else:
                        t.score_for_task = t.max_score - (t.max_score * t.percent / 100) * (t.time_of_participant - min_)
                        # print(t.score_for_task)
                else:
                    t.score_for_task = 0