class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while len(sandwiches) > 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = 0
            else:
                s = students.pop(0)
                students.append(s)
                counter += 1

            if counter >= len(students):
                break

        return len(students)

